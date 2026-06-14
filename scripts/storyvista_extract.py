#!/usr/bin/env python3
"""Extract StoryVista JSON artifacts without rendering the atlas page."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from storyvista.chunking import chunk_text  # noqa: E402
from storyvista.entity_model import extract_entities  # noqa: E402
from storyvista.ingest import ingest_source  # noqa: E402
from storyvista.pipeline import write_json  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract StoryVista source, chunk, and atlas JSON files.")
    parser.add_argument("input")
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    out = Path(args.out).resolve()
    out.mkdir(parents=True, exist_ok=True)
    source_index, text = ingest_source(args.input)
    chunks = chunk_text(text)
    atlas = extract_entities(text, chunks, source_index["sources"][0]["title"])
    write_json(out / "source-index.json", source_index)
    write_json(out / "chunks.json", chunks)
    write_json(out / "story-atlas.json", atlas)
    print(json.dumps({"output_dir": str(out), "chunks": len(chunks["chunks"])}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
