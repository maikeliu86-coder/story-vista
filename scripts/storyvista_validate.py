#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from storyvista.validators import validate_output  # noqa: E402

if __name__ == "__main__":
    passed, warnings = validate_output(sys.argv[1])
    print(f"passed={len(passed)} warnings={len(warnings)}")
    for warning in warnings:
        print(f"WARNING: {warning}")
    raise SystemExit(0 if not warnings else 1)
