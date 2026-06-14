from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path


def detect_language(text: str) -> str:
    chinese = sum("\u4e00" <= char <= "\u9fff" for char in text)
    return "zh-CN" if chinese > max(10, len(text) // 20) else "en"


def find_title(text: str, fallback: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
        if stripped.startswith("标题："):
            return stripped.split("：", 1)[1].strip()
    return fallback


def ingest_source(input_path: str) -> tuple[dict, str]:
    path = Path(input_path)
    text = path.read_text(encoding="utf-8")
    source = {
        "source_id": "src_001",
        "path": str(path),
        "type": "text",
        "title": find_title(text, path.stem.replace("-", " ").title()),
        "language": detect_language(text),
        "created_at": datetime.now(timezone.utc).isoformat(),
        "character_count": len(text),
        "notes": "Processed locally by StoryVista v0.2.",
    }
    return {"schema_version": "0.2.0", "sources": [source]}, text
