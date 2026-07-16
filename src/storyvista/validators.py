from __future__ import annotations

import json
import re
from pathlib import Path

from .image_validation import inspect_raster_image


REQUIRED_FILES = [
    "source-index.json", "chunks.json", "language-profile.json", "reader-text.json", "entity-linking.json",
    "character-atlas.json", "relationship-web.json", "location-atlas.json", "map-plan.json",
    "object-lore-codex.json", "visual-evidence.json", "story-atlas.json", "visual-asset-plan.json",
    "image-manifest.json", "spoiler-state.json", "provider-choice-state.json", "theme-profile.json",
    "prompt-pack.md", "manual-generation-instructions.md", "atlas.html",
]
SCHEMA_FILES = {
    "story-atlas.json": "story-atlas.schema.json",
    "image-manifest.json": "image-manifest.schema.json",
}
SCHEMA_DIR = Path(__file__).resolve().parents[2] / "skill" / "templates"
RASTER_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}


def _schema_ref(root_schema: dict, reference: str) -> dict:
    if not reference.startswith("#/"):
        raise ValueError(f"Unsupported schema reference: {reference}")
    current = root_schema
    for part in reference[2:].split("/"):
        current = current[part.replace("~1", "/").replace("~0", "~")]
    return current


def _matches_type(value: object, expected: str) -> bool:
    if expected == "object":
        return isinstance(value, dict)
    if expected == "array":
        return isinstance(value, list)
    if expected == "string":
        return isinstance(value, str)
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "boolean":
        return isinstance(value, bool)
    if expected == "null":
        return value is None
    return True


def _validate_schema(value: object, schema: dict, root_schema: dict, path: str = "$") -> list[str]:
    if "$ref" in schema:
        return _validate_schema(value, _schema_ref(root_schema, schema["$ref"]), root_schema, path)

    errors: list[str] = []
    expected_types = schema.get("type")
    if expected_types:
        allowed = [expected_types] if isinstance(expected_types, str) else expected_types
        if not any(_matches_type(value, item) for item in allowed):
            return [f"{path} must be {' or '.join(allowed)}"]
    if "const" in schema and value != schema["const"]:
        errors.append(f"{path} must equal {schema['const']!r}")
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path} must be one of {schema['enum']!r}")

    if isinstance(value, str):
        if len(value) < schema.get("minLength", 0):
            errors.append(f"{path} is shorter than minLength {schema['minLength']}")
        if schema.get("pattern") and not re.search(schema["pattern"], value):
            errors.append(f"{path} does not match {schema['pattern']!r}")
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if "minimum" in schema and value < schema["minimum"]:
            errors.append(f"{path} is below minimum {schema['minimum']}")
        if "maximum" in schema and value > schema["maximum"]:
            errors.append(f"{path} is above maximum {schema['maximum']}")
    if isinstance(value, list) and isinstance(schema.get("items"), dict):
        for index, item in enumerate(value):
            errors.extend(_validate_schema(item, schema["items"], root_schema, f"{path}[{index}]"))
    if isinstance(value, dict):
        properties = schema.get("properties", {})
        for required in schema.get("required", []):
            if required not in value:
                errors.append(f"{path}.{required} is required")
        for key, item in value.items():
            if key in properties:
                errors.extend(_validate_schema(item, properties[key], root_schema, f"{path}.{key}"))
            elif schema.get("additionalProperties") is False:
                errors.append(f"{path}.{key} is not allowed")
            elif isinstance(schema.get("additionalProperties"), dict):
                errors.extend(_validate_schema(item, schema["additionalProperties"], root_schema, f"{path}.{key}"))
    return errors


def _path_within(root: Path, relative_path: object) -> Path | None:
    if not isinstance(relative_path, str) or not relative_path:
        return None
    candidate = (root / relative_path).resolve()
    try:
        candidate.relative_to(root)
    except ValueError:
        return None
    return candidate


def validate_output(out_dir: str | Path) -> tuple[list[str], list[str]]:
    root = Path(out_dir).resolve()
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

    for data_name, schema_name in SCHEMA_FILES.items():
        if data_name not in data:
            continue
        schema_path = SCHEMA_DIR / schema_name
        if not schema_path.exists():
            warnings.append(f"Missing schema file: {schema_name}")
            continue
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        schema_errors = _validate_schema(data[data_name], schema, schema)
        if schema_errors:
            warnings.extend(f"Schema {data_name}: {item}" for item in schema_errors)
        else:
            passed.append(f"Schema valid: {data_name}")

    atlas = data.get("story-atlas.json", {})
    manifest = data.get("image-manifest.json", {})
    plan = data.get("visual-asset-plan.json", {})
    entities = atlas.get("entities", {})
    characters = entities.get("characters", [])
    entity_ids = {item.get("entity_id") for group in entities.values() for item in group}
    event_ids = {item.get("event_id") for item in atlas.get("events", [])}
    valid_bindings = entity_ids | event_ids
    content_count = sum(len(group) for group in entities.values() if isinstance(group, list))
    content_count += len(atlas.get("relations", [])) + len(atlas.get("events", []))
    if content_count:
        passed.append("Story atlas contains extracted content")
    elif atlas:
        warnings.append("Story atlas contains no extracted entities, relations, or events")

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
        display_file = _path_within(root, asset.get("file_path", ""))
        fallback_file = _path_within(root, asset.get("placeholder_path", asset.get("file_path", "")))
        if display_file is None or fallback_file is None:
            warnings.append(f"Unsafe display or fallback path: {asset.get('asset_id')}")
            continue
        if display_file.exists() and fallback_file.exists():
            passed.append(f"Display and fallback assets exist: {asset.get('asset_id')}")
        else:
            warnings.append(f"Missing display or fallback asset: {asset.get('asset_id')}")
        if display_file.suffix.lower() in RASTER_EXTENSIONS:
            if inspect_raster_image(display_file):
                passed.append(f"Valid raster image: {asset.get('asset_id')}")
            else:
                warnings.append(f"Invalid raster image: {asset.get('asset_id')}")

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
    manifest_path = root / "image-manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {"assets": []}
    status_counts = {}
    for asset in manifest["assets"]:
        status_counts[asset.get("status", "unknown")] = status_counts.get(asset.get("status", "unknown"), 0) + 1
    binding_path = root / "binding-report.json"
    binding = json.loads(binding_path.read_text(encoding="utf-8")) if binding_path.exists() else {"matched_count": 0, "unmatched": []}
    lines = [
        "# StoryVista Verification Report", "", "## Result",
        f"- Passed checks: {len(passed)}", f"- Warnings: {len(warnings)}",
        f"- Input language: {(language_profile or {}).get('input_language', 'unknown')}",
        f"- UI language: {(language_profile or {}).get('ui_language', 'unknown')}",
        f"- UI locale status: {(language_profile or {}).get('ui_locale_status', 'unknown')}",
        f"- Provider status: {(provider_state or {}).get('status', 'prompt-workflow-ready')}",
        f"- Recommended provider: {(provider_state or {}).get('recommended_provider', 'prompt-pack')}",
        f"- Theme: {(theme_profile or {}).get('theme_id', 'unknown')}",
        "- Atlas generation status: complete" if not warnings else "- Atlas generation status: complete with warnings",
        "", "## Passed Checks", *[f"- {item}" for item in passed],
        "", "## Warnings", *([f"- {item}" for item in warnings] or ["- None"]),
        "", "## Unresolved Evidence", *([f"- {item}" for item in unresolved] or ["- None"]),
        "", "## Ambiguous Entity Links", *([f"- {item['alias']}: {', '.join(item['candidate_entity_ids'])}" for item in (entity_linking or {}).get('ambiguous', [])] or ["- None"]),
        "", "## Missing Optional Assets",
        f"- Manifest status counts: {status_counts}",
        "- Real images may remain pending external generation; semantic placeholders are display fallbacks.",
        "", "## Manual Image Binding",
        f"- Successfully bound: {binding.get('matched_count', 0)}",
        f"- Unmatched files: {binding.get('unmatched', [])}",
        "", "## Next Steps",
        "- Review inferred visual details and ambiguous aliases before publishing.",
        "- Use prompt-pack.md or provider-specific prompt files, then bind generated files with the CLI.",
        "- Review evidence tags before publishing the atlas.",
    ]
    path = root / "verification-report.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path
