from __future__ import annotations

import re


HEADING_RE = re.compile(r"^(#{1,3})\s+(.+)$")


def chunk_text(text: str, source_id: str = "src_001", max_chars: int = 1200) -> dict:
    chunks = []
    current_heading = None
    offset = 0
    parts = re.split(r"(\n\s*\n)", text)
    buffer = ""
    buffer_start = 0

    def emit(value: str, start: int, heading: str | None) -> None:
        cleaned = value.strip()
        if not cleaned:
            return
        end = start + len(value)
        chunks.append({
            "chunk_id": f"ch_{len(chunks) + 1:03d}",
            "source_id": source_id,
            "start_offset": start,
            "end_offset": end,
            "chapter": heading if heading and ("章" in heading or "幕" in heading) else None,
            "scene": heading if heading and ("场" in heading or "景" in heading) else None,
            "heading": heading,
            "text": cleaned,
            "summary": cleaned[:160],
            "detected_entities": [],
        })

    for part in parts:
        match = HEADING_RE.match(part.strip())
        if match:
            if buffer.strip():
                emit(buffer, buffer_start, current_heading)
                buffer = ""
            current_heading = match.group(2).strip()
            buffer_start = offset
            buffer = part
        elif len(buffer) + len(part) > max_chars and buffer.strip():
            emit(buffer, buffer_start, current_heading)
            buffer = part
            buffer_start = offset
        else:
            if not buffer:
                buffer_start = offset
            buffer += part
        offset += len(part)
    if buffer.strip():
        emit(buffer, buffer_start, current_heading)
    return {"schema_version": "0.2.0", "chunks": chunks}
