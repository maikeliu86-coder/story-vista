from __future__ import annotations


def build_visual_asset_plan(atlas: dict, language_profile: dict | None = None, provider_state: dict | None = None, theme_profile: dict | None = None) -> dict:
    language_profile = language_profile or {"input_language": "unknown", "ui_language": "en"}
    provider_state = provider_state or {"selected_provider": "placeholder-svg", "fallback_provider": "placeholder-svg"}
    theme_profile = theme_profile or {"theme_id": "literary-archive", "background_prompt": "Spoiler-free literary atmosphere"}
    assets = []
    for character in atlas["entities"]["characters"]:
        for asset_type, suffix, framing in (
            ("character_portrait", "portrait", "close portrait"),
            ("character_half_body", "half_body", "half-body character study"),
            ("character_first_scene", "first_scene", "spoiler-safe first appearance scene"),
        ):
            assets.append({
                "asset_id": f"asset_{character['entity_id']}_{suffix}",
                "entity_id": character["entity_id"], "event_id": None, "location_id": None,
                "asset_type": asset_type, "priority": "high" if character["importance"] == "major" else "medium",
                "prompt": f"{framing} of {character['canonical_name']}, role {character['role_name']}, faction {character['faction']}; evidence-aware, unknown physical details left neutral, no text.",
                "negative_prompt": "initials avatar, letters only, watermark, unsupported costume claims",
                "style_profile": theme_profile["theme_id"], "provider_preference": provider_state["selected_provider"], "status": "placeholder",
                "prompt_language": "en", "source_language": language_profile["input_language"], "ui_language": language_profile["ui_language"],
                "evidence_status": "contextual", "inference_note": "Physical details not supported by source remain neutral.",
            })
    for location in atlas["entities"]["locations"]:
        assets.append({
            "asset_id": f"asset_{location['entity_id']}_keyart",
            "entity_id": location["entity_id"], "event_id": None, "location_id": location["entity_id"],
            "asset_type": "location_keyart", "priority": "medium",
            "prompt": f"Location key art of {location['canonical_name']}; {location['location_type']}; mood: {', '.join(location['mood'])}; no invented precise geography, no text.",
            "negative_prompt": "letters only, watermark, neon cyberpunk, empty white background",
            "style_profile": theme_profile["theme_id"], "provider_preference": provider_state["selected_provider"], "status": "placeholder",
            "prompt_language": "en", "source_language": language_profile["input_language"], "ui_language": language_profile["ui_language"],
        })
    for item in [*atlas["entities"].get("objects", []), *atlas["entities"].get("concepts", [])]:
        assets.append({
            "asset_id": f"asset_{item['entity_id']}_codex",
            "entity_id": item["entity_id"], "event_id": None, "location_id": None,
            "asset_type": "object_lore_keyart", "priority": "medium",
            "prompt": f"Game codex object study of {item['canonical_name']}; {item.get('description', '')}; diagrammatic clarity, no text.",
            "negative_prompt": "watermark, unsupported mechanism, unrelated object",
            "style_profile": theme_profile["theme_id"], "provider_preference": provider_state["selected_provider"], "status": "placeholder",
            "prompt_language": "en", "source_language": language_profile["input_language"], "ui_language": language_profile["ui_language"],
        })
    assets.extend([
        {
            "asset_id": "asset_story_map", "entity_id": None, "event_id": None, "location_id": None,
            "asset_type": "interpretive_map", "priority": "high",
            "prompt": "Interpretive story geography map using only stated location relationships; label-free, no invented distances.",
            "negative_prompt": "false precision, invented roads, watermark, text labels",
            "style_profile": theme_profile["theme_id"], "provider_preference": provider_state["selected_provider"], "status": "placeholder",
            "prompt_language": "en", "source_language": language_profile["input_language"], "ui_language": language_profile["ui_language"],
        },
        {
            "asset_id": "asset_atlas_background", "entity_id": None, "event_id": None, "location_id": None,
            "asset_type": "spoiler_safe_background", "priority": "medium",
            "prompt": theme_profile["background_prompt"], "negative_prompt": "characters, plot events, spoilers, text, watermark",
            "style_profile": theme_profile["theme_id"], "provider_preference": provider_state["selected_provider"], "status": "placeholder",
            "prompt_language": "en", "source_language": language_profile["input_language"], "ui_language": language_profile["ui_language"],
        },
    ])
    return {
        "schema_version": "0.3.0", "provider_status": provider_state["status"],
        "selected_provider": provider_state["selected_provider"], "fallback_provider": provider_state["fallback_provider"],
        "prompt_only": provider_state["prompt_only"], "assets": assets,
    }
