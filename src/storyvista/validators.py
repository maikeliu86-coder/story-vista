from __future__ import annotations

import json
from pathlib import Path


REQUIRED_FILES = [
    "source-index.json", "chunks.json", "language-profile.json", "reader-text.json", "entity-linking.json",
    "character-atlas.json", "relationship-web.json", "location-atlas.json", "map-plan.json",
    "object-lore-codex.json", "visual-evidence.json", "story-atlas.json", "visual-asset-plan.json",
    "image-manifest.json", "spoiler-state.json", "provider-choice-state.json", "theme-profile.json", "atlas.html",
]


def validate_output(out_dir: str | Path) -> tuple[list[str], list[str]]:
    root = Path(out_dir)
    passed: list[str] = []
    warnings: list[str] = []
    data = {}
    for name in REQUIRED_FILES:
        path = root / name
        if not path.exists():
            warnings.append(f"Missing required file: {name}")
            continue
        passed.append(f"Exists: {name}")
        if path.suffix == ".json":
            try:
                data[name] = json.loads(path.read_text(encoding="utf-8"))
                passed.append(f"Valid JSON: {name}")
            except json.JSONDecodeError as exc:
                warnings.append(f"Invalid JSON {name}: {exc}")

    atlas = data.get("story-atlas.json", {})
    manifest = data.get("image-manifest.json", {})
    plan = data.get("visual-asset-plan.json", {})
    entities = atlas.get("entities", {})
    characters = entities.get("characters", [])
    entity_ids = {item.get("entity_id") for group in entities.values() for item in group}
    event_ids = {item.get("event_id") for item in atlas.get("events", [])}
    valid_bindings = entity_ids | event_ids

    for character in characters:
        if character.get("importance") == "major" and character.get("entity_id"):
            passed.append(f"Major character has entity_id: {character['name']}")
        elif character.get("importance") == "major":
            warnings.append(f"Major character missing entity_id: {character.get('name')}")

    for relation in atlas.get("relations", []):
        source = relation.get("source_entity_id")
        target = relation.get("target_entity_id")
        if source in entity_ids and target in entity_ids:
            passed.append(f"Relation integrity: {relation['relation_id']}")
        else:
            warnings.append(f"Broken relation endpoint: {relation.get('relation_id')}")
        if relation.get("evidence") or relation.get("status") == "unresolved":
            passed.append(f"Relation evidence state recorded: {relation['relation_id']}")
        else:
            warnings.append(f"Relation lacks evidence or unresolved state: {relation.get('relation_id')}")

    asset_ids = [item.get("asset_id") for item in plan.get("assets", [])]
    if len(asset_ids) == len(set(asset_ids)):
        passed.append("Visual asset ids are unique")
    else:
        warnings.append("Duplicate visual asset ids")

    manifest_ids = [item.get("asset_id") for item in manifest.get("assets", [])]
    if len(manifest_ids) == len(set(manifest_ids)):
        passed.append("Manifest asset ids are unique")
    else:
        warnings.append("Duplicate manifest asset ids")

    for asset in manifest.get("assets", []):
        if asset.get("bound_to") not in valid_bindings and not str(asset.get("bound_to", "")).startswith("asset_"):
            warnings.append(f"Manifest binding does not exist: {asset.get('asset_id')}")
        placeholder = root / asset.get("file_path", "")
        if placeholder.exists():
            passed.append(f"Placeholder exists: {asset.get('asset_id')}")
        else:
            warnings.append(f"Missing placeholder: {asset.get('file_path')}")

    major_ids = {item["entity_id"] for item in characters if item.get("importance") == "major"}
    portrait_ids = {item.get("entity_id") for item in plan.get("assets", []) if item.get("asset_type") == "character_portrait"}
    missing_portraits = major_ids - portrait_ids
    if not missing_portraits:
        passed.append("Every major character has a portrait asset")
    else:
        warnings.append(f"Major characters missing portraits: {sorted(missing_portraits)}")

    if manifest.get("allow_initials_avatar") is False:
        passed.append("Initials-only avatars disabled")
    else:
        warnings.append("Initials-only avatar policy is not disabled")
    return passed, warnings


def write_verification_report(out_dir: str | Path, passed: list[str], warnings: list[str], atlas: dict, language_profile: dict | None = None, entity_linking: dict | None = None, provider_state: dict | None = None, theme_profile: dict | None = None) -> Path:
    root = Path(out_dir)
    unresolved = []
    for relation in atlas.get("relations", []):
        if relation.get("status") == "unresolved":
            unresolved.append(relation.get("relation_id"))
    for event in atlas.get("events", []):
        if event.get("status") == "unresolved":
            unresolved.append(event.get("event_id"))
    lines = [
        "# StoryVista Verification Report", "", "## Result",
        f"- Passed checks: {len(passed)}", f"- Warnings: {len(warnings)}",
        f"- Input language: {(language_profile or {}).get('input_language', 'unknown')}",
        f"- UI language: {(language_profile or {}).get('ui_language', 'unknown')}",
        f"- UI locale status: {(language_profile or {}).get('ui_locale_status', 'unknown')}",
        f"- Provider status: {(provider_state or {}).get('status', 'placeholder-svg')}",
        f"- Selected provider: {(provider_state or {}).get('selected_provider', 'placeholder-svg')}",
        f"- Theme: {(theme_profile or {}).get('theme_id', 'unknown')}",
        "- Atlas generation status: complete" if not warnings else "- Atlas generation status: complete with warnings",
        "", "## Passed Checks", *[f"- {item}" for item in passed],
        "", "## Warnings", *([f"- {item}" for item in warnings] or ["- None"]),
        "", "## Unresolved Evidence", *([f"- {item}" for item in unresolved] or ["- None"]),
        "", "## Ambiguous Entity Links", *([f"- {item['alias']}: {', '.join(item['candidate_entity_ids'])}" for item in (entity_linking or {}).get('ambiguous', [])] or ["- None"]),
        "", "## Missing Optional Assets",
        "- API-generated images are optional in v0.3; semantic placeholders are present.",
        "", "## Next Steps",
        "- Review inferred visual details and ambiguous aliases before publishing.",
        "- Replace placeholder assets through image-manifest.json when licensed images are available.",
        "- Review evidence tags before publishing the atlas.",
    ]
    path = root / "verification-report.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path
