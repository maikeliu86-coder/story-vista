from __future__ import annotations

from datetime import datetime, timezone


def build_image_manifest(plan: dict) -> dict:
    now = datetime.now(timezone.utc).isoformat()
    assets = []
    for item in plan["assets"]:
        bound_to = item["entity_id"] or item["event_id"] or item["location_id"]
        assets.append({
            "asset_id": item["asset_id"], "bound_to": bound_to,
            "file_path": f"assets/placeholders/{bound_to}.svg",
            "provider": "placeholder-svg", "status": "placeholder", "generated_at": now,
            "prompt_ref": item["asset_id"], "alt_text": f"Semantic {item['asset_type']} placeholder for {bound_to}",
            "license_note": "Generated locally by StoryVista; no third-party image used.",
        })
    return {
        "schema_version": "0.2.0", "provider_status": "verified",
        "binding_source": "image-manifest.json", "allow_initials_avatar": False, "assets": assets,
    }
