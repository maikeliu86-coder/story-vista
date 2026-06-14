from __future__ import annotations

import re


def build_entity_linking(reader_text: dict, entities: list[dict], ambiguous_aliases: list[dict]) -> dict:
    links = []
    ambiguous_names = {item["alias"].casefold() for item in ambiguous_aliases}
    for paragraph in reader_text["paragraphs"]:
        occupied: list[tuple[int, int]] = []
        candidates = []
        for entity in entities:
            for name in [entity["canonical_name"], *entity.get("aliases", [])]:
                for match in re.finditer(re.escape(name), paragraph["text"], re.I):
                    candidates.append((match.start(), match.end(), name, entity))
        for start, end, name, entity in sorted(candidates, key=lambda item: (item[0], -(item[1] - item[0]))):
            if any(start < used_end and end > used_start for used_start, used_end in occupied):
                continue
            occupied.append((start, end))
            links.append({
                "link_id": f"link_{len(links) + 1:04d}", "paragraph_id": paragraph["paragraph_id"],
                "entity_id": entity["entity_id"], "entity_type": entity["entity_type"],
                "matched_text": paragraph["text"][start:end], "start": start, "end": end,
                "status": "ambiguous" if name.casefold() in ambiguous_names else "resolved",
                "confidence": 0.5 if name.casefold() in ambiguous_names else 1.0,
            })
    return {"schema_version": "0.3.0", "links": links, "ambiguous": ambiguous_aliases}
