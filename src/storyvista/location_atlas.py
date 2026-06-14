from __future__ import annotations


def build_location_atlas(locations: list[dict]) -> dict:
    return {"schema_version": "0.3.0", "locations": locations}
