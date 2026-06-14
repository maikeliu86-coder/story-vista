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

from storyvista.pipeline import build  # noqa: E402
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
    args = parser.parse_args()

    if args.command == "build":
        result = build(args.input, args.out, ROOT, ui_language=args.ui_language, spoiler_mode=args.spoiler_mode)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0 if not result["warnings"] else 0
    passed, warnings = validate_output(args.output)
    print(json.dumps({"passed": passed, "warnings": warnings}, ensure_ascii=False, indent=2))
    return 0 if not warnings else 1


if __name__ == "__main__":
    raise SystemExit(main())
