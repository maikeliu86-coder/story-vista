#!/usr/bin/env python3
"""Render atlas.html from an existing StoryVista output directory."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from storyvista.atlas_renderer import render_atlas  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="Render atlas.html from story-atlas.json and image-manifest.json.")
    parser.add_argument("output")
    args = parser.parse_args()
    out = Path(args.output).resolve()
    atlas = json.loads((out / "story-atlas.json").read_text(encoding="utf-8"))
    manifest = json.loads((out / "image-manifest.json").read_text(encoding="utf-8"))
    render_atlas(atlas, manifest, ROOT / "skill" / "templates" / "atlas.html", out / "atlas.html")
    print(out / "atlas.html")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
