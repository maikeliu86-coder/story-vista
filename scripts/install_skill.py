#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shlex
import shutil
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
IGNORE = shutil.ignore_patterns(
    "__pycache__", "*.pyc", ".DS_Store", ".env", ".env.*", "*.log", ".venv", ".omx", "output", "tmp"
)


def install(target_value: str) -> dict[str, str]:
    target = Path(target_value).expanduser().resolve()
    if target.exists():
        raise FileExistsError(f"Installation target already exists: {target}")

    required = [
        ROOT / "skill" / "SKILL.md",
        ROOT / "skill",
        ROOT / "src",
        ROOT / "locales",
        ROOT / "docs",
        ROOT / "scripts" / "storyvista.py",
    ]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        raise FileNotFoundError(f"Repository is missing required install files: {', '.join(missing)}")

    target.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=f".{target.name}-install-", dir=target.parent))
    try:
        shutil.copy2(ROOT / "skill" / "SKILL.md", staging / "SKILL.md")
        for directory in ("skill", "src", "locales", "docs"):
            shutil.copytree(ROOT / directory, staging / directory, ignore=IGNORE)
        (staging / "scripts").mkdir()
        shutil.copy2(ROOT / "scripts" / "storyvista.py", staging / "scripts" / "storyvista.py")
        if (ROOT / "LICENSE").is_file():
            shutil.copy2(ROOT / "LICENSE", staging / "LICENSE")
        staging.replace(target)
    except Exception:
        shutil.rmtree(staging, ignore_errors=True)
        raise

    return {
        "target": str(target),
        "skill_entry": str(target / "SKILL.md"),
        "command": f"python3 {shlex.quote(str(target / 'scripts' / 'storyvista.py'))} build input.txt --out output/story",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Install a self-contained StoryVista Skill runtime.")
    parser.add_argument("--target", required=True, help="New directory to create for the installed Skill.")
    args = parser.parse_args()
    try:
        report = install(args.target)
    except (OSError, ValueError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
