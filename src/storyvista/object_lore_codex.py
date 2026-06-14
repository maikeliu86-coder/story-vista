from __future__ import annotations


def build_object_lore_codex(objects: list[dict], concepts: list[dict]) -> dict:
    return {
        "schema_version": "0.3.0",
        "entries": [*objects, *concepts],
        "categories": sorted({item.get("category", item["entity_type"]) for item in [*objects, *concepts]}),
    }
