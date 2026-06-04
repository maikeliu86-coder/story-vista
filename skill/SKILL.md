---
name: story-vista
description: "Codex-first, cross-agent compatible story visualization skill for turning novels, scripts, lore documents, and long-form prose into interactive visual story atlases with visual asset plans and image manifests."
---

# StoryVista | 文景

StoryVista is a portable cross-agent skill for making story worlds visible. Use it when the user wants to transform novels, scripts, screenplays, lore documents, RPG settings, character notes, location notes, timelines, or long-form prose into an interactive visual story atlas.

## Model And Agent Neutrality

- Codex is the first supported platform, not the only supported platform.
- Keep the core workflow independent from any single agent, model, framework, or image API.
- Use platform adapters only for installation, prompting, file access, or framework glue.
- If an agent cannot install `SKILL.md`, run StoryVista in Project Instruction Mode, AGENTS.md Mode, Prompt-Only Mode, Framework Adapter Mode, BYO Image Model Mode, Manual Asset Binding Mode, or No-Image Mode.

## Required Workflow

Run these phases in order unless the user explicitly narrows the task:

1. Parse source text.
2. Extract entities.
3. Classify entities by importance.
4. Build story data model.
5. Create visual asset plan.
6. Generate image prompts and/or images.
7. Create image manifest.
8. Bind image assets to character cards, location cards, relationship graph, timeline, 3D map, concept cards, and detail panels.
9. Generate final interactive atlas.
10. Run verification checklist.

StoryVista must generate a visual asset plan before building the final atlas.

## Operating Posture

- Treat the default deliverable as a reader-facing interactive archive, not a Markdown-only report.
- Read the source text before designing visuals. Entity classification must come from the text, not guessed aesthetics.
- Preserve textual evidence and note ambiguous entities.
- Prefer a polished single-page HTML atlas when the user asks for something they can open, share, or explore.
- Preserve the user's requested output location and sync target when given.

## Text-First Entity Modeling

Build separate data models before visualizing:

- Characters: people, aliases, titles, roles, factions, relationship changes, and profile summaries.
- Places: rooms, cities, planets, kingdoms, facilities, routes, battlefields, stations, and recurring locations.
- Ships and vehicles: never place ships in the character relationship tree.
- Technologies and abilities: weapons, powers, devices, procedures, systems, and scientific concepts.
- Organizations and factions: institutions, crews, governments, families, clans, sects, cults, armies, companies, and alliances.
- Objects and clues: artifacts, documents, tools, motifs, secrets, evidence, and plot-critical items.
- Concepts: magic systems, symbolic motifs, ideologies, schools, clans, technologies, and abstract ideas with narrative function.

## Default Atlas Sections

A complete archive normally includes:

1. Hero and concise project framing.
2. Anchor navigation.
3. Character thumbnail overview.
4. Character relationship tree.
5. Character index with detailed profiles.
6. Location cards and maps.
7. Organization, object, and concept indexes.
8. Technology, power, weapon, device, object, and concept timeline.
9. Plot phase or event timeline.
10. Scene, location, planet, ship, route, or world-space 3D map.
11. Interactive detail panel for selected people, places, concepts, and nodes.

## Visual Asset Generation Phase

Before final atlas generation, create `visual-asset-plan.json`. It must include:

- Major character portraits.
- Supporting character portraits when narratively important.
- Key location images.
- Organization or faction emblems.
- Important object or prop images.
- Concept images for abstract concepts, magic systems, technologies, clans, schools, sects, or symbolic motifs.
- Timeline keyframe images for major events when useful.
- Relationship graph node image bindings.
- 3D map or spatial node image bindings.

Each planned asset must include an entity id, asset type, prompt, negative prompt, aspect ratio, filename, status, and binding targets.

## Image Provider Neutrality

StoryVista defines what images are needed, not where they are generated.

- Do not hard-bind the core skill to ChatGPT Image, GPT Image, Image-2, OpenAI, or any single provider.
- If an image provider is available, generate or prepare prompts for that provider.
- If no provider is available, generate complete prompts and an image manifest.
- If the user provides images, bind them through `image-manifest.json`.
- Put provider-specific syntax in provider adapters or configuration, not in the core workflow.

Supported provider modes: `openai`, `chatgpt-image`, `midjourney`, `stable-diffusion`, `flux`, `comfyui`, `minimax-image`, `qwen-image`, `tencent-hunyuan-image`, `baidu-wenxin-image`, `ideogram`, `leonardo`, `local-folder`, `manual-assets`, `placeholder-svg`, and `custom-api`.

## Character Image Requirements

Every major character must have a `character_portrait` asset. Important supporting characters should have one when they affect comprehension.

For every major character, record:

- `entity_id`
- `canonical_name`
- `aliases`
- `role_in_story`
- `age_range`
- `gender_presentation` if available
- `appearance_summary`
- `clothing_style`
- `era_or_genre_context`
- `personality_visual_cues`
- `expression_default`
- `pose_default`
- `color_palette`
- `image_prompt`
- `negative_prompt`
- `aspect_ratio`
- `filename`
- `binding_targets`

Initials-only avatars are not acceptable as primary character portraits.

## Location Image Requirements

Every key location must have a `location_keyart` asset.

For every key location, record:

- `entity_id`
- `canonical_name`
- `location_type`
- `geography`
- `architecture`
- `time_period`
- `atmosphere`
- `narrative_function`
- `lighting`
- `color_palette`
- `image_prompt`
- `negative_prompt`
- `aspect_ratio`
- `filename`
- `binding_targets`

Locations must not default to blank or text-only cards. If no image is generated, bind a semantic placeholder through the manifest.

## Asset Manifest Requirements

Create `image-manifest.json` before final atlas binding. It must track assets with statuses such as `planned`, `prompt_ready`, `generated`, `user_provided`, `placeholder`, `missing`, and `failed`.

Supported asset types include:

- `character_portrait`
- `character_full_body`
- `location_keyart`
- `organization_emblem`
- `object_icon`
- `concept_art`
- `event_keyframe`
- `timeline_thumbnail`
- `relationship_node`
- `map_node`
- `placeholder`

Images must be bound through `image-manifest.json`. The final atlas must never silently replace missing images with initials without logging the fallback in the manifest.

## No Initials-Only Avatar Policy

StoryVista must not use initials-only avatars as the default visual output.

Initials-only avatars are allowed only as fallback placeholders when all of these are true:

- Image generation is unavailable, user assets are unavailable, or the selected image provider fails.
- Semantic SVG placeholder generation is unavailable or unsuitable.
- The user explicitly requests lightweight placeholder mode or sets `allow_initials_avatar: true`.
- The fallback is recorded in `image-manifest.json`.

Default configuration: `allow_initials_avatar: false`.

## Fallback Placeholder Rules

Fallback priority:

1. User-provided image.
2. Generated image from configured provider.
3. Provider-specific prompt ready.
4. Generic prompt ready.
5. Semantic SVG placeholder with full entity name and type.
6. Initials-only placeholder only as last resort and only when explicitly allowed.

Semantic placeholders should include full name, entity type, visual category, and stable filename. They should avoid pretending to be final art.

## Cross-Agent Execution Modes

- **Core Skill Mode**: agents that read this `SKILL.md` directly.
- **Project Instruction Mode**: copy or reference this file as project instructions.
- **AGENTS.md Mode**: use repository root `AGENTS.md` for coding agents.
- **Prompt-Only Mode**: paste the workflow into a chat agent.
- **Framework Adapter Mode**: implement phases as tools or steps in Hugging Face smolagents, LlamaIndex, LangChain, CrewAI, AutoGen, Qwen-Agent, or custom pipelines.
- **BYO Image Model Mode**: produce prompts and manifest entries for external image generation.
- **Manual Asset Binding Mode**: bind user-provided images through `image-manifest.json`.
- **No-Image Mode**: create prompts, manifest entries, and semantic SVG placeholders.

## Responsive-First Requirement

Verify desktop, tablet, and mobile layouts:

- Desktop: about 1365 x 900 or wider.
- Tablet: about 768 x 1024.
- Mobile: about 390 x 844.

Names must remain readable. Cards, controls, labels, and graph nodes need touch-sized click targets. Page scrolling must not be trapped by graph or 3D interaction areas.

## Character Relationship Rules

- Character overview should use independent character cards.
- Names must remain complete on mobile and should not cover faces.
- Character nodes should use manifest-bound portraits or semantic placeholders.
- Clicking a character should update a detail panel and highlight related characters and edges.
- Relationship trees should prefer faction, function, or story-role grouping over chaotic all-to-all webs.

## 3D Space Map Rules

Use Three.js or an equivalent real-time 3D engine when spatial relationships, planets, ships, facilities, routes, battlefields, or world maps matter.

Forbidden patterns:

- 2D image stickers in 3D space.
- Rounded photo cards, album-wall layouts, or floating screenshot panels.
- Fake 3D canvas that only moves flat icons.
- Text-only clickable nodes.

Build every spatial entity as an independent 3D miniature model or holographic landmark where feasible. Model bodies and labels must both support hover/click/tap and update the detail panel.

## Verification Checklist

Before calling StoryVista output complete, verify:

- Source entities are separated into characters, places, ships, technologies, organizations, objects, and concepts.
- Every major character has a planned or bound `character_portrait` asset.
- Every key location has a planned or bound `location_keyart` asset.
- `visual-asset-plan.json` exists before final atlas generation.
- `image-manifest.json` exists and covers generated, planned, missing, placeholder, and user-provided assets.
- Initials-only avatars are not used as primary portraits.
- Missing images use semantic placeholders or manifest-tracked fallback.
- Image paths resolve and thumbnails are not stretched.
- Character cards, relationship graph nodes, timeline items, location cards, concept cards, detail panels, and 3D map nodes bind to manifest assets.
- Desktop, tablet, and mobile screenshots show readable text and no major overlap.
- 3D canvas/WebGL is nonblank when a 3D map is included.
- Script syntax checks pass for generated HTML/JS.

## Output Habit

When producing files, report:

- What story model was extracted.
- Which assets are generated, planned, missing, placeholder, or user-provided.
- Where `visual-asset-plan.json`, `image-manifest.json`, and final atlas files are located.
- What verification was performed and what remains unverified.
