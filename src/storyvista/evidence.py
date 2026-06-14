from __future__ import annotations


VALID_STATUSES = {"explicit", "inferred", "ambiguous", "contradictory", "unresolved"}


def excerpt(text: str, terms: list[str], limit: int = 260) -> str:
    positions = [text.find(term) for term in terms if term and text.find(term) >= 0]
    start = max(0, min(positions) - 60) if positions else 0
    value = text[start:start + limit].strip().replace("\n", " ")
    return value


def build_evidence(chunks: list[dict], terms: list[str], status: str = "explicit") -> list[dict]:
    matches = []
    for chunk in chunks:
        if all(term in chunk["text"] for term in terms if term):
            matches.append({
                "source_id": chunk["source_id"],
                "chunk_id": chunk["chunk_id"],
                "quote": excerpt(chunk["text"], terms),
                "summary": f"Source text mentions: {', '.join(terms)}",
                "confidence": "high" if status == "explicit" else "medium",
                "status": status,
            })
            break
    return matches


def index_evidence(items: list[dict]) -> dict:
    index = []
    seen = set()
    for item in items:
        for evidence in item.get("evidence", []):
            key = (evidence["source_id"], evidence["chunk_id"], evidence["quote"], evidence["status"])
            if key in seen:
                continue
            seen.add(key)
            entry = dict(evidence)
            entry["evidence_id"] = f"ev_{len(index) + 1:03d}"
            index.append(entry)
    return {entry["evidence_id"]: entry for entry in index}
