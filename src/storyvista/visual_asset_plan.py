from __future__ import annotations


def build_visual_asset_plan(atlas: dict) -> dict:
    assets = []
    for character in atlas["entities"]["characters"]:
        assets.append({
            "asset_id": f"asset_{character['entity_id']}_portrait",
            "entity_id": character["entity_id"], "event_id": None, "location_id": None,
            "asset_type": "character_portrait", "priority": "high" if character["importance"] == "major" else "medium",
            "prompt": f"Cinematic character portrait of {character['name']}, {character['role_name']}, faction {character['faction']}; restrained historical drama lighting; readable face; no text.",
            "negative_prompt": "initials avatar, letters only, watermark, neon UI, generic stock portrait",
            "style_profile": "cinematic-bible", "provider_preference": "placeholder-svg", "status": "placeholder",
        })
    for location in atlas["entities"]["locations"]:
        assets.append({
            "asset_id": f"asset_{location['entity_id']}_keyart",
            "entity_id": location["entity_id"], "event_id": None, "location_id": location["entity_id"],
            "asset_type": "location_keyart", "priority": "medium",
            "prompt": f"Cinematic location key art of {location['name']}; {location['location_type']}; mood: {', '.join(location['mood'])}; historical drama visual bible, no text.",
            "negative_prompt": "letters only, watermark, neon cyberpunk, empty white background",
            "style_profile": "cinematic-bible", "provider_preference": "placeholder-svg", "status": "placeholder",
        })
    for event in atlas["events"]:
        assets.append({
            "asset_id": f"asset_{event['event_id']}_keyframe",
            "entity_id": None, "event_id": event["event_id"], "location_id": event["location_id"],
            "asset_type": "event_keyframe", "priority": "low",
            "prompt": f"Cinematic event keyframe: {event['title']}. {event['summary']}",
            "negative_prompt": "text overlay, watermark, unrelated characters",
            "style_profile": "cinematic-bible", "provider_preference": "placeholder-svg", "status": "placeholder",
        })
    return {"schema_version": "0.2.0", "provider_status": "placeholder-first", "assets": assets}
