from __future__ import annotations

import re


DIRECTIVE_RE = re.compile(r"^\s*[^:：]+\s*[:：].*[|｜]")


def build_reader_text(text: str, chunks_doc: dict) -> dict:
    paragraphs = []
    cursor = 0
    chapter = None
    for raw in re.split(r"\n\s*\n", text):
        value = raw.strip()
        if not value:
            cursor += len(raw) + 2
            continue
        if value.startswith("#"):
            chapter = value.lstrip("# ").strip()
        elif DIRECTIVE_RE.match(value):
            cursor += len(raw) + 2
            continue
        else:
            chunk = next((item for item in chunks_doc["chunks"] if value[:30] in item["text"]), None)
            paragraphs.append({
                "paragraph_id": f"p_{len(paragraphs) + 1:04d}", "chapter": chapter,
                "text": value, "start_offset": text.find(value, cursor),
                "end_offset": text.find(value, cursor) + len(value),
                "chunk_id": chunk["chunk_id"] if chunk else None,
            })
        cursor += len(raw) + 2
    return {"schema_version": "0.3.0", "paragraphs": paragraphs, "chapter_count": len({item["chapter"] for item in paragraphs if item["chapter"]})}
