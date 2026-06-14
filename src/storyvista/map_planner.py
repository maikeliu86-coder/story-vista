from __future__ import annotations


def build_map_plan(locations: list[dict]) -> dict:
    return {
        "schema_version": "0.3.0", "map_type": "interpretive",
        "canonical_accuracy": "unresolved",
        "disclaimer": "Relative placement is interpretive unless the source explicitly states geography.",
        "nodes": [{"location_id": item["entity_id"], "label": item["canonical_name"], "spatial_notes": item["spatial_notes"]} for item in locations],
        "edges": [],
    }
