from __future__ import annotations

import re
from collections import defaultdict

from .evidence import build_evidence, index_evidence


DIRECTIVES = {
    "人物": "characters",
    "地点": "locations",
    "组织": "organizations",
    "道具": "objects",
    "概念": "concepts",
    "关系": "relations",
    "事件": "events",
    "表演": "actor",
}


def fields(value: str) -> list[str]:
    return [part.strip() for part in re.split(r"[｜|]", value) if part.strip()]


def parse_directives(text: str) -> dict[str, list[list[str]]]:
    parsed: dict[str, list[list[str]]] = defaultdict(list)
    for line in text.splitlines():
        stripped = line.strip()
        for label, key in DIRECTIVES.items():
            prefix = f"{label}："
            if stripped.startswith(prefix):
                parsed[key].append(fields(stripped[len(prefix):]))
                break
    return parsed


def slug_id(prefix: str, index: int) -> str:
    return f"{prefix}_{index:03d}"


def narrative_summary(chunks: list[dict]) -> str:
    for chunk in chunks:
        lines = []
        for line in chunk["text"].splitlines():
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            if any(stripped.startswith(f"{label}：") for label in DIRECTIVES):
                continue
            lines.append(stripped)
        if lines:
            return " ".join(lines)[:220]
    return "No source summary available."


def extract_entities(text: str, chunks_doc: dict, title: str) -> dict:
    chunks = chunks_doc["chunks"]
    parsed = parse_directives(text)
    characters = []
    name_to_id = {}
    for i, row in enumerate(parsed["characters"], 1):
        name = row[0]
        entity_id = slug_id("char", i)
        name_to_id[name] = entity_id
        evidence = build_evidence(chunks, [name])
        characters.append({
            "entity_id": entity_id,
            "name": name,
            "aliases": [],
            "entity_type": "character",
            "importance": "major" if i <= 5 else "supporting",
            "role_name": row[1] if len(row) > 1 else "未标注角色",
            "faction": row[2] if len(row) > 2 else "未标注阵营",
            "narrative_function": row[3] if len(row) > 3 else "unresolved",
            "first_seen": evidence[0]["chunk_id"] if evidence else None,
            "last_seen": evidence[-1]["chunk_id"] if evidence else None,
            "goals": [], "fears": [], "secrets": [], "arc": "",
            "evidence": evidence,
        })

    locations = []
    location_to_id = {}
    for i, row in enumerate(parsed["locations"], 1):
        name = row[0]
        entity_id = slug_id("loc", i)
        location_to_id[name] = entity_id
        locations.append({
            "entity_id": entity_id,
            "name": name,
            "entity_type": "location",
            "location_type": row[1] if len(row) > 1 else "unresolved",
            "mood": row[2].split("、") if len(row) > 2 else [],
            "visual_keywords": row[3].split("、") if len(row) > 3 else [],
            "evidence": build_evidence(chunks, [name]),
        })

    simple_groups = {}
    for key, prefix, entity_type in (("organizations", "org", "organization"), ("objects", "obj", "object"), ("concepts", "concept", "concept")):
        values = []
        for i, row in enumerate(parsed[key], 1):
            name = row[0]
            values.append({
                "entity_id": slug_id(prefix, i), "name": name, "entity_type": entity_type,
                "description": row[1] if len(row) > 1 else "", "evidence": build_evidence(chunks, [name]),
            })
        simple_groups[key] = values

    relations = []
    for i, row in enumerate(parsed["relations"], 1):
        pair = re.split(r"\s*(?:->|→)\s*", row[0])
        source_name = pair[0] if pair else ""
        target_name = pair[1] if len(pair) > 1 else ""
        evidence = build_evidence(chunks, [source_name, target_name])
        relations.append({
            "relation_id": slug_id("rel", i),
            "source_entity_id": name_to_id.get(source_name),
            "target_entity_id": name_to_id.get(target_name),
            "relation_type": row[1] if len(row) > 1 else "unresolved",
            "polarity": row[2] if len(row) > 2 else "neutral",
            "strength": float(row[3]) if len(row) > 3 and row[3].replace(".", "", 1).isdigit() else 0.5,
            "stage": row[4] if len(row) > 4 else "",
            "status": "explicit" if evidence else "unresolved",
            "evidence": evidence,
        })

    events = []
    for i, row in enumerate(parsed["events"], 1):
        title_value = row[0]
        participant_names = re.split(r"[,，、]", row[1]) if len(row) > 1 else []
        location_name = row[2] if len(row) > 2 else ""
        summary = row[3] if len(row) > 3 else title_value
        evidence = build_evidence(chunks, [title_value]) or build_evidence(chunks, [name for name in participant_names if name])
        events.append({
            "event_id": slug_id("evt", i), "title": title_value, "summary": summary,
            "participants": [name_to_id[name] for name in participant_names if name in name_to_id],
            "location_id": location_to_id.get(location_name), "timeline_order": i,
            "status": "explicit" if evidence else "unresolved", "evidence": evidence,
        })

    actor_rows = {row[0]: row for row in parsed["actor"] if row}
    actor_characters = []
    for character in characters:
        row = actor_rows.get(character["name"], [])
        related_events = [event for event in events if character["entity_id"] in event["participants"]]
        event_evidence = [ev for event in related_events for ev in event["evidence"]]
        actor_characters.append({
            "character_id": character["entity_id"], "role_name": character["role_name"],
            "scene_objectives": [row[1]] if len(row) > 1 else ["根据场景证据继续确认目标"],
            "relationship_beats": [relation["relation_id"] for relation in relations if character["entity_id"] in (relation["source_entity_id"], relation["target_entity_id"])],
            "emotional_arc": row[5] if len(row) > 5 else "unresolved",
            "subtext": row[4] if len(row) > 4 else "unresolved",
            "playable_actions": row[6].split("、") if len(row) > 6 else ["观察", "试探"],
            "costume_and_prop_notes": row[7].split("、") if len(row) > 7 else [],
            "voice_and_physicality_notes": row[8].split("、") if len(row) > 8 else [],
            "public_summary": f"{character['name']}：{character['role_name']}，隶属{character['faction']}。",
            "spoiler_sensitive_notes": row[3] if len(row) > 3 else "",
            "status": "inferred" if row else "unresolved",
            "evidence": event_evidence[:2] or character["evidence"][:1],
        })

    all_evidence_items = characters + locations + simple_groups["organizations"] + simple_groups["objects"] + simple_groups["concepts"] + relations + events + actor_characters
    evidence_index = index_evidence(all_evidence_items)

    summary = narrative_summary(chunks)
    themes = [theme for theme in ["权力", "忠诚", "背叛", "误判", "家族命运", "责任"] if theme in text]

    return {
        "schema_version": "0.2.0",
        "metadata": {"title": title, "mode": "reader+actor", "status": "prototype"},
        "summary": summary, "themes": themes,
        "entities": {"characters": characters, "locations": locations, **simple_groups},
        "relations": relations, "events": events,
        "timeline": [{"order": event["timeline_order"], "event_id": event["event_id"], "title": event["title"]} for event in events],
        "actor_mode": {"status": "prototype", "characters": actor_characters},
        "visual_style": {
            "theme": "Cinematic Bible", "palette": ["#101112", "#1b1d1f", "#d2b36b", "#d8d6d0", "#85898f"],
            "materials": ["weathered paper", "charcoal", "brushed brass"],
            "composition": ["cinematic widescreen", "archival index", "restrained card grid"],
            "camera_language": ["measured close-up", "negative space", "low-key lighting"],
            "costume_props": [item["name"] for item in simple_groups["objects"]],
            "avoid": ["neon cyberpunk", "glossy game lobby", "initials-only avatars"],
        },
        "evidence_index": evidence_index,
    }
