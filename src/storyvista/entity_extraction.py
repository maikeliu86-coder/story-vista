from __future__ import annotations

import re
from collections import defaultdict

from .evidence import build_evidence


LABELS = {
    "character": "characters", "人物": "characters",
    "location": "locations", "地点": "locations",
    "organization": "organizations", "组织": "organizations",
    "object": "objects", "item": "objects", "道具": "objects", "物品": "objects",
    "lore": "concepts", "concept": "concepts", "概念": "concepts", "设定": "concepts",
    "relation": "relations", "relationship": "relations", "关系": "relations",
    "event": "events", "事件": "events",
}


def _parts(value: str) -> list[str]:
    return [part.strip() for part in re.split(r"[|｜]", value) if part.strip()]


def parse_directives(text: str) -> dict[str, list[list[str]]]:
    parsed: dict[str, list[list[str]]] = defaultdict(list)
    for line in text.splitlines():
        match = re.match(r"^\s*([^:：]+)\s*[:：]\s*(.+)$", line)
        if not match:
            continue
        key = LABELS.get(match.group(1).strip().lower()) or LABELS.get(match.group(1).strip())
        if key:
            parsed[key].append(_parts(match.group(2)))
    return parsed


def _id(prefix: str, index: int) -> str:
    return f"{prefix}_{index:03d}"


def _csv(value: str) -> list[str]:
    return [item.strip() for item in re.split(r"[,，、;/]", value) if item.strip()]


def extract_story_entities(text: str, chunks_doc: dict) -> dict:
    parsed = parse_directives(text)
    chunks = chunks_doc["chunks"]
    characters = []
    for index, row in enumerate(parsed["characters"], 1):
        name = row[0]
        aliases = _csv(row[4]) if len(row) > 4 else []
        characters.append({
            "entity_id": _id("char", index), "entity_type": "character",
            "canonical_name": name, "name": name, "localized_names": {}, "localized_aliases": {},
            "aliases": aliases, "memory_label": row[5] if len(row) > 5 else (row[1] if len(row) > 1 else name),
            "role_name": row[1] if len(row) > 1 else "unresolved",
            "faction": row[2] if len(row) > 2 else "unresolved",
            "narrative_function": row[3] if len(row) > 3 else "unresolved",
            "importance": "major" if index <= 5 else "supporting",
            "evidence": build_evidence(chunks, [name]),
        })

    name_to_id = {}
    for character in characters:
        for value in [character["canonical_name"], *character["aliases"]]:
            name_to_id[value.casefold()] = character["entity_id"]

    locations = []
    for index, row in enumerate(parsed["locations"], 1):
        name = row[0]
        locations.append({
            "entity_id": _id("loc", index), "entity_type": "location",
            "canonical_name": name, "name": name, "localized_names": {},
            "location_type": row[1] if len(row) > 1 else "unresolved",
            "mood": _csv(row[2]) if len(row) > 2 else [],
            "visual_keywords": _csv(row[3]) if len(row) > 3 else [],
            "spatial_notes": row[4] if len(row) > 4 else "unresolved",
            "evidence": build_evidence(chunks, [name]),
        })

    groups = {}
    for key, prefix, entity_type in (("organizations", "org", "organization"), ("objects", "obj", "object"), ("concepts", "lore", "lore")):
        values = []
        for index, row in enumerate(parsed[key], 1):
            name = row[0]
            values.append({
                "entity_id": _id(prefix, index), "entity_type": entity_type,
                "canonical_name": name, "name": name, "localized_names": {},
                "category": row[1] if len(row) > 1 else entity_type,
                "description": row[2] if len(row) > 2 else (row[1] if len(row) > 1 else "unresolved"),
                "visual_keywords": _csv(row[3]) if len(row) > 3 else [],
                "evidence": build_evidence(chunks, [name]),
            })
        groups[key] = values

    relations = []
    for index, row in enumerate(parsed["relations"], 1):
        pair = re.split(r"\s*(?:->|→)\s*", row[0])
        source, target = (pair + [""])[:2]
        evidence = build_evidence(chunks, [source, target])
        spoiler = row[5].lower() if len(row) > 5 else "visible"
        relations.append({
            "relation_id": _id("rel", index),
            "source_entity_id": name_to_id.get(source.casefold()),
            "target_entity_id": name_to_id.get(target.casefold()),
            "source_name": source, "target_name": target,
            "relation_type": row[1] if len(row) > 1 else "unresolved",
            "polarity": row[2] if len(row) > 2 else "neutral",
            "strength": float(row[3]) if len(row) > 3 and re.fullmatch(r"\d+(?:\.\d+)?", row[3]) else 0.5,
            "stage": row[4] if len(row) > 4 else "current",
            "spoiler_status": "locked" if "lock" in spoiler or "隐藏" in spoiler else "visible",
            "status": "explicit" if evidence else "unresolved", "evidence": evidence,
        })

    events = []
    location_ids = {item["canonical_name"]: item["entity_id"] for item in locations}
    for index, row in enumerate(parsed["events"], 1):
        participants = _csv(row[1]) if len(row) > 1 else []
        events.append({
            "event_id": _id("evt", index), "title": row[0],
            "participants": [name_to_id[name.casefold()] for name in participants if name.casefold() in name_to_id],
            "location_id": location_ids.get(row[2]) if len(row) > 2 else None,
            "summary": row[3] if len(row) > 3 else row[0], "timeline_order": index,
            "spoiler_status": "locked" if len(row) > 4 and ("lock" in row[4].lower() or "隐藏" in row[4]) else "visible",
            "evidence": build_evidence(chunks, [row[0]]) or build_evidence(chunks, participants[:1]),
        })
    return {"characters": characters, "locations": locations, **groups, "relations": relations, "events": events}
