from __future__ import annotations


def _asset(
    *, asset_id: str, asset_type: str, entity_id: str | None, location_id: str | None,
    entity_name: str, prompt: str, negative_prompt: str, aspect_ratio: str,
    priority: str, language_profile: dict, provider_state: dict, theme_profile: dict,
    evidence_summary: str, generation_notes: str,
) -> dict:
    localized_prompt = (
        f"{entity_name}，{prompt}，电影感构图，细节丰富，允许基于时代与语境进行合理美术补全。"
        if language_profile["input_language"].startswith("zh")
        else prompt
    )
    return {
        "asset_id": asset_id, "entity_id": entity_id, "event_id": None, "location_id": location_id,
        "entity_name": entity_name, "asset_type": asset_type, "priority": priority,
        "prompt": prompt, "localized_prompt": localized_prompt,
        "negative_prompt": negative_prompt, "aspect_ratio": aspect_ratio,
        "style_mode": "creative-balanced", "style_profile": theme_profile["theme_id"],
        "provider_preference": provider_state["recommended_provider"],
        "status": "prompt_only_ready" if provider_state["prompt_only"] else "pending_generation",
        "prompt_language": "en", "source_language": language_profile["input_language"], "ui_language": language_profile["ui_language"],
        "evidence_status": "contextual", "evidence_summary": evidence_summary,
        "generation_notes": generation_notes,
        "composition_note": "Choose a varied, story-appropriate camera angle; preserve confirmed traits and label stylized additions as inferred.",
        "expected_filename": f"{asset_id}.png",
        "expected_file_path": f"assets/generated/{asset_id}.png",
    }


def _joined(values: list[str] | None) -> str:
    return ", ".join(item for item in (values or []) if item)


def build_visual_asset_plan(atlas: dict, language_profile: dict | None = None, provider_state: dict | None = None, theme_profile: dict | None = None) -> dict:
    language_profile = language_profile or {"input_language": "unknown", "ui_language": "en"}
    provider_state = provider_state or {"recommended_provider": "prompt-pack", "fallback_provider": "placeholder-svg", "prompt_only": True, "status": "prompt-workflow-ready"}
    theme_profile = theme_profile or {"theme_id": "literary-archive", "background_prompt": "Spoiler-free literary atmosphere"}
    assets = []
    for character in atlas["entities"]["characters"]:
        evidence_summary = f"Confirmed identity: {character['canonical_name']}. Context: {character['role_name']} in {character['faction']}. Physical details not stated by the source remain inferred."
        for asset_type, suffix, framing, ratio in (
            ("character_portrait", "portrait", "Expressive character portrait", "4:5"),
            ("character_half_body", "half_body", "Dynamic half-body character study", "3:4"),
            ("character_first_scene", "first_scene", "Spoiler-safe first-appearance scene", "16:9"),
        ):
            assets.append(_asset(
                asset_id=f"asset_{character['entity_id']}_{suffix}", asset_type=asset_type,
                entity_id=character["entity_id"], location_id=None, entity_name=character["canonical_name"],
                prompt=f"{framing} of {character['canonical_name']}, {character['role_name']}, associated with {character['faction']}. Preserve confirmed identity and story context; use plausible period styling and a visually engaging angle without revealing later plot events.",
                negative_prompt="watermark, text overlay, spoiler scene, unrelated character",
                aspect_ratio=ratio, priority="high" if character["importance"] == "major" else "medium",
                language_profile=language_profile, provider_state=provider_state, theme_profile=theme_profile,
                evidence_summary=evidence_summary,
                generation_notes="Creative-balanced mode permits contextual costume, lighting, and composition choices while keeping unsupported physical traits visibly interpretive.",
            ))
    for location in atlas["entities"]["locations"]:
        location_keywords = _joined(location.get("visual_keywords", []))
        assets.append(_asset(
            asset_id=f"asset_{location['entity_id']}_keyart", asset_type="location_keyart",
            entity_id=location["entity_id"], location_id=location["entity_id"], entity_name=location["canonical_name"],
            prompt=f"Immersive location key art of {location['canonical_name']}, a {location['location_type']}; atmosphere: {', '.join(location['mood'])}; visual motifs: {location_keywords}. Scene role: {location.get('scene_role', 'source-mentioned')}. Choose a cinematic viewpoint and enrich plausible environmental details without inventing exact geography.",
            negative_prompt="watermark, text labels, spoiler event, false map precision",
            aspect_ratio="16:9", priority="medium", language_profile=language_profile,
            provider_state=provider_state, theme_profile=theme_profile,
            evidence_summary=f"Location, type, mood, and motifs are sourced from {location['canonical_name']} directives or text evidence.",
            generation_notes="Environmental materials and lighting may be completed creatively when consistent with the stated mood.",
        ))
    for item in [*atlas["entities"].get("objects", []), *atlas["entities"].get("concepts", [])]:
        visual_keywords = _joined(item.get("visual_keywords", []))
        visual_clause = f" Preserve source visual attributes: {visual_keywords}." if visual_keywords else ""
        assets.append(_asset(
            asset_id=f"asset_{item['entity_id']}_codex", asset_type="object_lore_keyart",
            entity_id=item["entity_id"], location_id=None, entity_name=item["canonical_name"],
            prompt=f"Detailed game-codex visual study of {item['canonical_name']}: {item.get('description', '')}.{visual_clause} Show materials, energy, scale cues, and a compelling three-quarter or diagrammatic view as appropriate.",
            negative_prompt="watermark, text labels, unrelated object, invented plot revelation",
            aspect_ratio="1:1", priority="medium", language_profile=language_profile,
            provider_state=provider_state, theme_profile=theme_profile,
            evidence_summary=f"Name and function come from source evidence; mechanisms not stated by the text are stylized interpretation.",
            generation_notes="Creative-balanced mode allows a readable functional design while avoiding claims of canonical internal mechanics.",
        ))
    assets.extend([
        _asset(
            asset_id="asset_story_map", asset_type="interpretive_map", entity_id=None, location_id=None,
            entity_name="Story Geography Map", prompt="Interpretive story geography map using only stated location relationships. Create an elegant illustrated atlas composition with varied landmarks and routes; avoid false distances or invented canonical borders.",
            negative_prompt="false precision, invented borders, watermark, dense text labels", aspect_ratio="16:9", priority="high",
            language_profile=language_profile, provider_state=provider_state, theme_profile=theme_profile,
            evidence_summary="Map nodes come from extracted locations; relative placement is interpretive.",
            generation_notes="Use symbolic geography and visual hierarchy rather than claiming survey accuracy.",
        ),
        _asset(
            asset_id="asset_atlas_background", asset_type="spoiler_safe_background", entity_id=None, location_id=None,
            entity_name="Atlas Background", prompt=theme_profile["background_prompt"],
            negative_prompt="characters, plot events, spoilers, text, watermark", aspect_ratio="16:9", priority="medium",
            language_profile=language_profile, provider_state=provider_state, theme_profile=theme_profile,
            evidence_summary="Atmosphere derives from the theme profile, not later plot information.",
            generation_notes="Keep contrast low enough for readable interface overlays.",
        ),
    ])
    return {
        "schema_version": "0.4.0", "provider_status": provider_state["status"],
        "selected_provider": provider_state["recommended_provider"], "fallback_provider": provider_state["fallback_provider"],
        "prompt_only": provider_state["prompt_only"], "style_mode": "creative-balanced",
        "supported_style_modes": ["evidence-strict", "creative-balanced", "cinematic-free"],
        "assets": assets,
    }
