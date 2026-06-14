from __future__ import annotations

import json
from pathlib import Path

from .atlas_renderer import render_atlas
from .chunking import chunk_text
from .entity_model import extract_entities
from .image_manifest import build_image_manifest
from .ingest import ingest_source
from .placeholder_svg import generate_placeholders
from .validators import validate_output, write_verification_report
from .visual_asset_plan import build_visual_asset_plan


def write_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def build(input_path: str, output_dir: str, repo_root: Path) -> dict:
    out = Path(output_dir).resolve()
    out.mkdir(parents=True, exist_ok=True)
    source_index, text = ingest_source(input_path)
    chunks = chunk_text(text)
    atlas = extract_entities(text, chunks, source_index["sources"][0]["title"])
    plan = build_visual_asset_plan(atlas)
    manifest = build_image_manifest(plan)

    write_json(out / "source-index.json", source_index)
    write_json(out / "chunks.json", chunks)
    write_json(out / "story-atlas.json", atlas)
    write_json(out / "visual-asset-plan.json", plan)
    write_json(out / "image-manifest.json", manifest)
    generate_placeholders(atlas, manifest, out)
    render_atlas(atlas, manifest, repo_root / "skill" / "templates" / "atlas.html", out / "atlas.html")
    passed, warnings = validate_output(out)
    write_verification_report(out, passed, warnings, atlas)
    return {"output_dir": str(out), "passed": len(passed), "warnings": warnings}
