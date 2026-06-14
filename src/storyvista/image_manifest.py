from __future__ import annotations

from datetime import datetime, timezone


def build_image_manifest(plan: dict) -> dict:
    now = datetime.now(timezone.utc).isoformat()
    assets = []
    for item in plan["assets"]:
        bound_to = item["entity_id"] or item["event_id"] or item["location_id"] or item["asset_id"]
        placeholder = f"assets/placeholders/{item['asset_id']}.svg"
        assets.append({
            "asset_id": item["asset_id"], "asset_type": item["asset_type"], "bound_to": bound_to,
            "file_path": placeholder, "placeholder_path": placeholder,
            "expected_file_path": item["expected_file_path"], "expected_filename": item["expected_filename"],
            "provider": item["provider_preference"],
            "status": "pending_external_generation" if plan["prompt_only"] else "prompt_only_ready",
            "generated_at": now, "prompt_ref": item["asset_id"], "prompt": item["prompt"],
            "negative_prompt": item["negative_prompt"], "aspect_ratio": item["aspect_ratio"],
            "style_mode": item["style_mode"],
            "alt_text": f"{item['entity_name']} {item['asset_type']} visual; external generation pending",
            "license_note": "Placeholder generated locally. External image provenance must be recorded after binding.",
        })
    return {
        "schema_version": "0.4.0", "provider_status": "prompt-workflow-ready",
        "binding_source": "image-manifest.json", "allow_initials_avatar": False, "assets": assets,
    }
