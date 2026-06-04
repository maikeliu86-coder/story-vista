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
2. Extract story entities.
3. Classify entities by narrative importance.
4. Build story data model.
5. Show Preflight Image Provider Check.
6. Run or offer Image Provider Diagnosis.
7. Detect available image providers, config files, environment variables, local endpoints, manual asset folders, and existing manifests.
8. Apply Default Image Provider Selection Policy.
9. Select image mode: `api`, `manual-assets`, `prompt-only`, or `placeholder-svg`.
10. If provider state is high risk, ask for secondary confirmation when the agent environment supports it.
11. Create visual asset plan.
12. Generate image prompts and/or images.
13. Create or update image manifest.
14. Bind generated images, manual assets, prompts, or semantic placeholders to atlas UI.
15. Generate final interactive atlas.
16. Add image provider attribution note to generated page.
17. Run verification checklist.
18. Report StoryVista generation status, image provider status, selected provider, selection reason, visual asset status, placeholder status, and recommended next steps.

StoryVista must generate a visual asset plan before building the final atlas.
Preflight check does not block story parsing. Image provider diagnosis does not block final atlas generation.

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

## Preflight Image Provider Check

StoryVista must run or offer a Preflight Image Provider Check before visual asset generation.

- Preflight is a helpful status check, not an error and not blame.
- It should say "current environment has no directly callable image provider" when applicable.
- If the agent environment supports interactive confirmation, ask only when useful.
- If the environment does not support interactive confirmation, use auto diagnosis and auto selection when possible.
- If the user is unsure, keep Auto Mode enabled.
- Missing image provider is not a fatal error; continue with `prompt-only` or `placeholder-svg`.

Chinese message:

> 在开始生成故事视觉页面前，建议先检查当前配置的生图引擎。StoryVista 会根据你的当前 image provider 生成人物、地点和关键事件的视觉资产。如果当前没有可调用的生图引擎，StoryVista 仍会生成完整提示词、图片清单和语义占位图，方便你后续补图或切换模型后重新生成。
>
> 如果你不确定该选哪个生图引擎，可以直接使用 Auto Mode。StoryVista 会根据当前环境自动选择一个推荐 image provider。

English message:

> Before generating the visual story atlas, StoryVista recommends checking your current image provider. Character portraits, location key art, and event visuals will be generated or planned based on the selected provider. If no callable image provider is available, StoryVista will still create full image prompts, an image manifest, and semantic placeholders for later replacement or regeneration.
>
> If you are not sure which image provider to use, keep Auto Mode enabled. StoryVista will select a recommended provider based on the current environment.

## Image Provider Diagnosis

Diagnosis checks config files, environment variables, local endpoints, manual asset folders, and existing manifests. It must not print complete API keys.

Allowed provider status values:

- `detected`
- `not_found`
- `configured_but_unverified`
- `reachable`
- `unreachable`
- `requires_manual_setup`
- `prompt_only`
- `placeholder_only`

Default diagnosis behavior:

- Do not make real paid API calls by default.
- `--verify` may check local endpoints or safe availability where supported.
- `--no-network` must prevent network checks.
- Mask secrets, for example `OPENAI_API_KEY: detected, masked as sk-***abcd`.

## Default Image Provider Selection Policy

StoryVista defaults to Auto Mode for image provider selection.

- Beginners should not be forced to choose from a long provider list.
- Explicit user configuration always wins.
- If the user previously selected a provider, prefer it when still available.
- If exactly one verified provider is detected, select it automatically.
- If multiple providers are detected, select the best recommended provider and explain why.
- If no provider is detected, continue with `prompt-only` or `placeholder-svg`.
- Provider recommendations are shown only when useful, not spammed.
- User can always override the selected provider.
- Never silently fall back to initials-only avatars.

Selection priority:

1. Explicit user config in `image-provider.config.yaml`.
2. User selection from current session.
3. Previously saved user preference if available.
4. Verified provider with highest StoryVista fit score.
5. Detected but unverified provider with highest score.
6. Prompt-only provider.
7. Manual assets mode.
8. Semantic `placeholder-svg` mode.
9. Initials-only avatar only if explicitly allowed.

Each detected provider should get `score`, `selection_reason`, and `risk_reasons`. Scoring should consider callable API, verified status, StoryVista fit, character consistency, location key art quality, Chinese prompt support, global accessibility, mainland China accessibility, cost predictability, speed, image-to-image support, batch generation, manual workflow support, user region fit, and config clarity.

## Secondary Confirmation Rules

Secondary confirmation is only required for high-risk image provider states:

- `no_provider_detected`
- `provider_configured_but_unverified`
- `provider_unreachable`
- `placeholder_only`
- `prompt_only`
- `allow_initials_avatar` is true
- user selected a provider with unknown capability
- image generation is disabled
- current provider does not support image generation
- selected provider requires manual generation outside the agent

Chinese:

> 当前配置可能无法直接生成完整图片资产，StoryVista 将使用 prompt-only 或 semantic placeholder 模式继续。是否继续使用当前设置？

English:

> The current configuration may not be able to generate complete image assets directly. StoryVista will continue in prompt-only or semantic placeholder mode. Continue with the current settings?

If the user continues, record `user_confirmed_current_provider: true`.

## Provider Attribution Note

The final atlas must include a subtle image provider attribution note. The note must be neutral and must not blame the user.

Use short attribution when images were generated:

- 中文：图片资产由当前配置的 image provider 生成或规划。你可以随时切换生图引擎并重新生成视觉资产。
- English: Image assets are generated or planned with the currently configured image provider. You can switch providers and regenerate visual assets at any time.

Use long attribution for `prompt-only` or `placeholder-svg`:

- 中文：本页面的图片资产由当前配置的生图引擎生成、规划或占位呈现。若希望获得不同风格、更高细节或更稳定的人物一致性，可切换 image provider 后重新生成视觉资产。
- English: The image assets in this atlas were generated, planned, or represented with placeholders based on the currently configured image provider. To get a different style, higher detail, or stronger character consistency, switch image providers and regenerate visual assets.

For `manual-assets`:

- 中文：图片资产来自用户提供素材，并通过 image-manifest.json 绑定到 StoryVista 页面。

Use subtle footer, info note, or settings panel placement. Do not use red warning styling unless a real error occurred.

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
- Preflight Image Provider Check was run or offered.
- Auto Mode selection policy was applied unless the user explicitly configured a provider.
- Every major character has a planned or bound `character_portrait` asset.
- Every key location has a planned or bound `location_keyart` asset.
- `visual-asset-plan.json` exists before final atlas generation.
- `image-manifest.json` exists and covers generated, planned, missing, placeholder, and user-provided assets.
- Image provider status, selected provider, selected mode, score, selection reason, and risk reasons are reported.
- The final atlas includes a subtle image provider attribution note.
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
- StoryVista generation status.
- Image provider status.
- Selected provider and selection reason.
- Which assets are generated, planned, missing, placeholder, or user-provided.
- Placeholder status and recommended next steps.
- Where `visual-asset-plan.json`, `image-manifest.json`, and final atlas files are located.
- What verification was performed and what remains unverified.
