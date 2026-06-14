from __future__ import annotations


def build_visual_evidence(groups: list[list[dict]]) -> dict:
    records = []
    for group in groups:
        for item in group:
            for field, value in item.get("visual_profile", {}).items():
                records.append({
                    "visual_evidence_id": f"ve_{len(records) + 1:04d}",
                    "entity_id": item["entity_id"], "field": field,
                    "value": value["value"], "status": value["status"],
                    "evidence": value.get("evidence", []),
                    "inference_note": "Role/faction context only; not asserted as physical fact." if value["status"] in {"contextual", "inferred"} else "",
                })
    return {"schema_version": "0.3.0", "allowed_statuses": ["confirmed", "contextual", "inferred", "unknown"], "records": records}
