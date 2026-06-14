from __future__ import annotations


def build_relationship_web(relations: list[dict], characters: list[dict]) -> dict:
    visible = [relation for relation in relations if relation["spoiler_status"] != "locked"]
    return {
        "schema_version": "0.3.0",
        "nodes": [{"entity_id": item["entity_id"], "label": item["canonical_name"], "faction": item["faction"]} for item in characters],
        "relationships": relations,
        "visible_relationship_ids": [item["relation_id"] for item in visible],
        "views": ["global", "character", "faction", "timeline"],
    }
