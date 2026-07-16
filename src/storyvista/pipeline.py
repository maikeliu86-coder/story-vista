from __future__ import annotations

import json
import shutil
import tempfile
import uuid
from pathlib import Path

from .atlas_renderer import render_atlas
from .alias_resolver import resolve_aliases
from .chunking import chunk_text
from .entity_extraction import extract_story_entities
from .entity_linking import build_entity_linking
from .image_binding import bind_images
from .image_manifest import build_image_manifest
from .ingest import ingest_source
from .i18n import load_all_locales, load_locale
from .language_detection import detect_language_profile
from .location_atlas import build_location_atlas
from .map_planner import build_map_plan
from .object_lore_codex import build_object_lore_codex
from .placeholder_svg import generate_placeholders
from .prompt_export import export_prompts
from .provider_preflight import build_provider_choice_state
from .reader_text import build_reader_text
from .relationship_web import build_relationship_web
from .spoiler import apply_spoiler_mode, build_spoiler_state, redact_locked_directives
from .theme_engine import build_theme_profile
from .validators import REQUIRED_FILES, validate_output, write_verification_report
from .visual_asset_plan import build_visual_asset_plan
from .visual_evidence import build_visual_evidence
from .visual_profile import attach_visual_profiles


MANAGED_OUTPUT_NAMES = set(REQUIRED_FILES) | {
    "assets",
    "binding-report.json",
    "prompts",
    "verification-report.md",
}
OUTPUT_MARKERS = {"source-index.json", "story-atlas.json", "image-manifest.json"}


def write_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _asset_identity(asset: dict) -> tuple[str, str, str]:
    return (
        str(asset.get("asset_id", "")),
        str(asset.get("asset_type", "")),
        str(asset.get("entity_name", "")),
    )


def _preserve_bound_images(existing_out: Path, staging_out: Path) -> int:
    old_manifest_path = existing_out / "image-manifest.json"
    old_plan_path = existing_out / "visual-asset-plan.json"
    new_plan_path = staging_out / "visual-asset-plan.json"
    if not old_manifest_path.exists() or not old_plan_path.exists():
        return 0

    try:
        old_manifest = json.loads(old_manifest_path.read_text(encoding="utf-8"))
        old_plan = json.loads(old_plan_path.read_text(encoding="utf-8"))
        new_plan = json.loads(new_plan_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError, TypeError):
        return 0

    old_manifest_assets = old_manifest.get("assets", [])
    old_plan_assets = old_plan.get("assets", [])
    new_plan_assets = new_plan.get("assets", [])
    if not all(isinstance(items, list) for items in (old_manifest_assets, old_plan_assets, new_plan_assets)):
        return 0
    old_identities = {
        item.get("asset_id"): _asset_identity(item)
        for item in old_plan_assets
        if isinstance(item, dict)
    }
    new_identities = {
        item.get("asset_id"): _asset_identity(item)
        for item in new_plan_assets
        if isinstance(item, dict)
    }
    generated_dir = (existing_out / "assets" / "generated").resolve()
    selected: list[Path] = []
    for asset in old_manifest_assets:
        if not isinstance(asset, dict) or asset.get("status") not in {"generated_external", "user_provided"}:
            continue
        asset_id = asset.get("asset_id")
        if not asset_id or old_identities.get(asset_id) != new_identities.get(asset_id):
            continue
        source = (existing_out / str(asset.get("file_path", ""))).resolve()
        try:
            source.relative_to(generated_dir)
        except ValueError:
            continue
        if source.is_file():
            selected.append(source)

    if not selected:
        return 0

    preserve_dir = staging_out / ".preserved-generated"
    preserve_dir.mkdir()
    try:
        for source in selected:
            shutil.copy2(source, preserve_dir / source.name)
        binding = bind_images(staging_out, preserve_dir)
    finally:
        shutil.rmtree(preserve_dir, ignore_errors=True)
    if binding["matched_count"]:
        binding["preserved_from_previous_build"] = True
        write_json(staging_out / "binding-report.json", binding)
    return binding["matched_count"]


def _copy_preserved_path(source: Path, target: Path) -> None:
    if source.is_symlink():
        return
    if source.is_dir():
        shutil.copytree(source, target, dirs_exist_ok=True, symlinks=True)
    elif source.is_file():
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)


def _preserve_user_files(existing_out: Path, staging_out: Path) -> None:
    for source in existing_out.iterdir():
        if source.name not in MANAGED_OUTPUT_NAMES:
            _copy_preserved_path(source, staging_out / source.name)

    old_assets = existing_out / "assets"
    if not old_assets.is_dir():
        return
    for source in old_assets.iterdir():
        if source.name != "placeholders":
            _copy_preserved_path(source, staging_out / "assets" / source.name)


def _publish_build(staging_out: Path, final_out: Path) -> None:
    if not final_out.exists():
        staging_out.replace(final_out)
        return

    backup = final_out.parent / f".{final_out.name}-backup-{uuid.uuid4().hex}"
    final_out.replace(backup)
    try:
        staging_out.replace(final_out)
    except BaseException:
        backup.replace(final_out)
        raise
    shutil.rmtree(backup, ignore_errors=True)


def _render_payload(out: Path, repo_root: Path) -> None:
    def load(name: str) -> dict:
        return json.loads((out / name).read_text(encoding="utf-8"))

    language_profile = load("language-profile.json")
    render_atlas({
        "atlas": load("story-atlas.json"), "manifest": load("image-manifest.json"),
        "languageProfile": language_profile, "readerText": load("reader-text.json"),
        "entityLinking": load("entity-linking.json"), "characterAtlas": load("character-atlas.json"),
        "relationshipWeb": load("relationship-web.json"), "locationAtlas": load("location-atlas.json"),
        "mapPlan": load("map-plan.json"), "objectLoreCodex": load("object-lore-codex.json"),
        "visualEvidence": load("visual-evidence.json"), "spoilerState": load("spoiler-state.json"),
        "providerState": load("provider-choice-state.json"), "themeProfile": load("theme-profile.json"),
        "visualAssetPlan": load("visual-asset-plan.json"),
        "locale": load_locale(repo_root, language_profile["ui_language"]), "allLocales": load_all_locales(repo_root),
    }, repo_root / "skill" / "templates" / "atlas.html", out / "atlas.html")


def rebuild_atlas(output_dir: str, repo_root: Path) -> dict:
    out = Path(output_dir).resolve()
    _render_payload(out, repo_root)
    passed, warnings = validate_output(out)
    write_verification_report(
        out, passed, warnings, json.loads((out / "story-atlas.json").read_text(encoding="utf-8")),
        json.loads((out / "language-profile.json").read_text(encoding="utf-8")),
        json.loads((out / "entity-linking.json").read_text(encoding="utf-8")),
        json.loads((out / "provider-choice-state.json").read_text(encoding="utf-8")),
        json.loads((out / "theme-profile.json").read_text(encoding="utf-8")),
    )
    return {"output_dir": str(out), "passed": len(passed), "warnings": warnings}


def _build_into(
    input_path: str,
    text: str,
    out: Path,
    repo_root: Path,
    ui_language: str,
    spoiler_mode: str,
    existing_out: Path | None,
) -> dict:
    language_profile = detect_language_profile(text, ui_language)
    source_index, text = ingest_source(input_path, language_profile["input_language"])
    extraction_chunks = chunk_text(text)
    extracted = extract_story_entities(text, extraction_chunks)
    characters, ambiguous_aliases = resolve_aliases(extracted["characters"], language_profile)
    extracted["characters"] = attach_visual_profiles(characters)
    spoiler_state = build_spoiler_state(extracted["relations"], extracted["events"], spoiler_mode)
    public_text = redact_locked_directives(text, spoiler_mode)
    chunks = chunk_text(public_text)
    extracted = apply_spoiler_mode(extracted, chunks["chunks"], spoiler_mode)
    reader_text = build_reader_text(public_text, chunks)
    all_entities = [*extracted["characters"], *extracted["locations"], *extracted["organizations"], *extracted["objects"], *extracted["concepts"]]
    entity_linking = build_entity_linking(reader_text, all_entities, ambiguous_aliases)
    relationship_web = build_relationship_web(extracted["relations"], extracted["characters"])
    location_atlas = build_location_atlas(extracted["locations"])
    map_plan = build_map_plan(extracted["locations"])
    object_lore_codex = build_object_lore_codex(extracted["objects"], extracted["concepts"])
    visual_evidence = build_visual_evidence([extracted["characters"]])
    provider_state = build_provider_choice_state(language_profile["input_language"])
    theme_profile = build_theme_profile(public_text)
    atlas = {
        "schema_version": "0.3.0",
        "metadata": {"title": source_index["sources"][0]["title"], "mode": "reader-visual-codex", "status": "runnable-minimum"},
        "summary": next((item["text"][:220] for item in reader_text["paragraphs"]), "No source summary available."),
        "themes": theme_profile["motifs"],
        "entities": {key: extracted[key] for key in ("characters", "locations", "organizations", "objects", "concepts")},
        "relations": extracted["relations"], "events": extracted["events"],
        "timeline": [{"order": item["timeline_order"], "event_id": item["event_id"], "title": item["title"]} for item in extracted["events"]],
        "actor_mode": {"status": "future-extension", "characters": []},
        "evidence_index": {},
        "visual_style": {"theme": theme_profile["theme_id"], "palette": theme_profile["palette"], "materials": theme_profile["motifs"], "composition": ["game codex", "reader companion"], "camera_language": [], "costume_props": [], "avoid": ["spoilers", "unsupported visual facts", "initials-only avatars"]},
    }
    plan = build_visual_asset_plan(atlas, language_profile, provider_state, theme_profile)
    manifest = build_image_manifest(plan)

    write_json(out / "source-index.json", source_index)
    write_json(out / "chunks.json", chunks)
    write_json(out / "language-profile.json", language_profile)
    write_json(out / "reader-text.json", reader_text)
    write_json(out / "entity-linking.json", entity_linking)
    write_json(out / "character-atlas.json", {"schema_version": "0.3.0", "characters": extracted["characters"]})
    write_json(out / "relationship-web.json", relationship_web)
    write_json(out / "location-atlas.json", location_atlas)
    write_json(out / "map-plan.json", map_plan)
    write_json(out / "object-lore-codex.json", object_lore_codex)
    write_json(out / "visual-evidence.json", visual_evidence)
    write_json(out / "story-atlas.json", atlas)
    write_json(out / "visual-asset-plan.json", plan)
    write_json(out / "image-manifest.json", manifest)
    write_json(out / "spoiler-state.json", spoiler_state)
    write_json(out / "provider-choice-state.json", provider_state)
    write_json(out / "theme-profile.json", theme_profile)
    generate_placeholders(atlas, manifest, out)
    preserved_images = _preserve_bound_images(existing_out, out) if existing_out else 0
    if existing_out:
        _preserve_user_files(existing_out, out)
    export_prompts(out)
    _render_payload(out, repo_root)
    passed, warnings = validate_output(out)
    write_verification_report(out, passed, warnings, atlas, language_profile, entity_linking, provider_state, theme_profile)
    return {
        "output_dir": str(out),
        "passed": len(passed),
        "warnings": warnings,
        "preserved_images": preserved_images,
    }


def build(input_path: str, output_dir: str, repo_root: Path, ui_language: str = "auto", spoiler_mode: str = "safe") -> dict:
    text = Path(input_path).read_text(encoding="utf-8")
    if not text.strip():
        raise ValueError("Input text is empty; StoryVista needs narrative or structured source content.")
    out = Path(output_dir).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    if out.exists() and not out.is_dir():
        raise NotADirectoryError(f"Output path is not a directory: {out}")
    if out.exists() and any(out.iterdir()) and not any((out / marker).exists() for marker in OUTPUT_MARKERS):
        raise ValueError(f"Refusing to replace non-StoryVista directory: {out}")

    staging = Path(tempfile.mkdtemp(prefix=f".{out.name}-build-", dir=out.parent))
    try:
        result = _build_into(
            input_path,
            text,
            staging,
            repo_root,
            ui_language,
            spoiler_mode,
            out if out.exists() else None,
        )
        _publish_build(staging, out)
    finally:
        shutil.rmtree(staging, ignore_errors=True)
    result["output_dir"] = str(out)
    result["published"] = True
    return result
