#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from storyvista.image_binding import bind_images  # noqa: E402
from storyvista.pipeline import build, rebuild_atlas  # noqa: E402
from storyvista.prompt_export import export_prompts  # noqa: E402
from storyvista.validators import validate_output  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(prog="storyvista", description="Build a multilingual, spoiler-safe StoryVista Reader Visual Codex.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    build_parser = subparsers.add_parser("build", help="Build a Story Atlas from a UTF-8 text file.")
    build_parser.add_argument("input")
    build_parser.add_argument("--out", required=True)
    build_parser.add_argument("--ui-language", default="auto", choices=["auto", "en", "zh-CN", "zh-TW", "ja", "ko", "fr", "es", "de", "ru"])
    build_parser.add_argument("--spoiler-mode", default="safe", choices=["safe", "full"])
    validate_parser = subparsers.add_parser("validate", help="Validate an existing output directory.")
    validate_parser.add_argument("output")
    export_parser = subparsers.add_parser("export-prompts", help="Export provider-specific prompt files.")
    export_parser.add_argument("output")
    export_parser.add_argument("--provider", required=True)
    bind_parser = subparsers.add_parser("bind-images", help="Bind externally generated images into an atlas.")
    bind_parser.add_argument("output")
    bind_parser.add_argument("--assets", required=True)
    rebuild_parser = subparsers.add_parser("rebuild-atlas", help="Re-render atlas.html from output JSON files.")
    rebuild_parser.add_argument("output")
    args = parser.parse_args()

    if args.command == "build":
        result = build(args.input, args.out, ROOT, ui_language=args.ui_language, spoiler_mode=args.spoiler_mode)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0 if not result["warnings"] else 0
    if args.command == "export-prompts":
        written = export_prompts(args.output, args.provider)
        print(json.dumps({"provider": args.provider, "written": [str(path) for path in written]}, ensure_ascii=False, indent=2))
        return 0
    if args.command == "bind-images":
        result = bind_images(args.output, args.assets)
        report_path = Path(args.output).resolve() / "binding-report.json"
        report_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        result["rebuild"] = rebuild_atlas(args.output, ROOT)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    if args.command == "rebuild-atlas":
        result = rebuild_atlas(args.output, ROOT)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0 if not result["warnings"] else 1
    passed, warnings = validate_output(args.output)
    print(json.dumps({"passed": passed, "warnings": warnings}, ensure_ascii=False, indent=2))
    return 0 if not warnings else 1


if __name__ == "__main__":
    raise SystemExit(main())
