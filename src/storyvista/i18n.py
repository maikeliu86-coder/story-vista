from __future__ import annotations

import json
from pathlib import Path


def load_locale(repo_root: Path, language: str) -> dict:
    locale_dir = repo_root / "locales"
    fallback = json.loads((locale_dir / "en.json").read_text(encoding="utf-8"))
    path = locale_dir / f"{language}.json"
    if not path.exists():
        return fallback
    selected = json.loads(path.read_text(encoding="utf-8"))
    return {**fallback, **selected}


def load_all_locales(repo_root: Path) -> dict[str, dict]:
    return {
        path.stem: json.loads(path.read_text(encoding="utf-8"))
        for path in sorted((repo_root / "locales").glob("*.json"))
    }
