---
name: story-vista
description: Build an evidence-aware interactive Story Atlas from novels, scripts, lore, and long-form prose.
---

# StoryVista | 文景

StoryVista turns a UTF-8 story source into structured JSON, semantic visual assets, and a static interactive atlas. The runnable path uses only the Python standard library. Image providers are optional.

## Run First

```bash
python scripts/storyvista.py build input.txt --out output/story
python scripts/storyvista.py validate output/story
```

Expected output:

- `source-index.json`
- `chunks.json`
- `story-atlas.json`
- `visual-asset-plan.json`
- `image-manifest.json`
- `assets/placeholders/*.svg`
- `atlas.html`
- `verification-report.md`

## Six-Step Workflow

1. **Ingest**: read UTF-8 text, identify title/language, and create `source-index.json`.
2. **Chunk**: split source into stable, offset-addressed chunks in `chunks.json`.
3. **Model**: extract entities, relations, events, Actor Mode notes, and evidence into `story-atlas.json`.
4. **Plan visuals**: create `visual-asset-plan.json` before rendering the atlas.
5. **Bind assets**: create `image-manifest.json`; use user assets, a configured provider, or semantic SVG placeholders.
6. **Render and verify**: build `atlas.html`, then validate IDs, evidence state, asset bindings, placeholders, and the no-initials policy.

## Evidence Contract

- Every explicit relation and event needs source evidence.
- Evidence records include `source_id`, `chunk_id`, quote, confidence, and status.
- Allowed status: `explicit`, `inferred`, `ambiguous`, `contradictory`, `unresolved`.
- Never present an inference as source fact. Actor Mode is preparation material, not a definitive interpretation.

## Source Directives

The minimal extractor recognizes optional Chinese directives. Put one record per line before or beside prose:

```text
人物：姓名｜角色｜阵营｜叙事功能
地点：名称｜类型｜氛围关键词｜视觉关键词
组织：名称｜说明
道具：名称｜说明
概念：名称｜说明
关系：人物A -> 人物B｜关系类型｜polarity｜0.8｜阶段
事件：事件名｜人物A、人物B｜地点｜摘要
表演：姓名｜场景目标｜秘密｜剧透信息｜潜台词｜情绪弧｜动作｜服装道具｜声音形体
```

If directives are absent, keep uncertain fields unresolved. Do not invent missing plot facts.

## Image Provider Rules

- Auto Mode may inspect configured providers, but provider absence is never fatal.
- Explicit user configuration wins.
- Do not print full API keys or make paid calls during diagnosis.
- Default fallback is `placeholder-svg`, with full entity name and semantic type.
- `allow_initials_avatar` must remain `false` unless the user explicitly overrides it.
- All atlas image bindings come from `image-manifest.json`.

Run provider diagnosis separately:

```bash
python scripts/detect_image_provider.py --no-network
```

See [image-provider.md](references/image-provider.md) for levels, switching, ComfyUI checks, and recommendations.

## Atlas Experience

The default `Cinematic Bible` atlas includes:

- overview metrics and themes
- searchable character cards
- relationship and event views
- locations and visual bible
- evidence drawer
- Actor Mode with objectives, subtext, emotional arc, playable actions, costume/props, and voice/physicality notes

Use `atlas.html` as a dependency-free baseline. Extend it only when the source and user request justify more complex maps, graph engines, or 3D scenes.

## Verification

Before completion, confirm:

- required JSON and HTML files exist and parse
- relation endpoints resolve
- explicit claims have evidence or remain unresolved
- every major character has a portrait plan
- every planned asset has a unique manifest binding
- semantic placeholders exist when no image provider is used
- initials-only avatars are disabled
- desktop and mobile layouts remain readable

Detailed contracts: [core-pipeline.md](references/core-pipeline.md), [data-contracts.md](references/data-contracts.md), [verification.md](references/verification.md), and [fallback-rules.md](references/fallback-rules.md).
