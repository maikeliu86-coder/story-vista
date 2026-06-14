from __future__ import annotations


def build_spoiler_state(relations: list[dict], events: list[dict], mode: str = "safe") -> dict:
    locked = [item["relation_id"] for item in relations if item.get("spoiler_status") == "locked"]
    locked += [item["event_id"] for item in events if item.get("spoiler_status") == "locked"]
    return {
        "schema_version": "0.3.0", "mode": mode, "enabled": mode != "full",
        "progress": {"type": "uploaded-fragment", "value": "current"},
        "locked_item_ids": locked if mode != "full" else [],
        "reveal_policy": "hide-locked-details" if mode != "full" else "show-all",
    }
