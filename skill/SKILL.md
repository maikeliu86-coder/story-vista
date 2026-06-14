---
name: story-vista
description: Build a multilingual, spoiler-safe Reader Visual Codex from complex novels and long-form story text.
---

# StoryVista | Reader Visual Codex

## Mission

Turn complex novels into multilingual visual reading companions: characters, aliases, relationships, locations, maps, objects, lore, highlighted source text, and spoiler-safe evidence.

## Required Inputs

- UTF-8 source text
- output directory
- optional `--ui-language auto|en|zh-CN|...`
- optional `--spoiler-mode safe|full`
- optional explicit visual provider or manual assets

## Run

```bash
python scripts/storyvista.py build input.txt --out output/story --ui-language auto
python scripts/storyvista.py validate output/story
```

## Required Outputs

Create source/chunk indexes, language profile, reader text, entity links, character atlas, relationship web, location atlas, map plan, object/lore codex, visual evidence, visual asset plan, image manifest, spoiler state, provider state, theme profile, placeholders, `atlas.html`, and `verification-report.md`.

## Language And Locale Rules

- Detect input language and script.
- Detect or accept UI language independently.
- Preserve canonical names and original spelling.
- Add localized labels only when useful; do not force-translate proper nouns.
- Apply language-specific alias rules conservatively.
- Mark uncertain alias merges ambiguous.
- Use English visual prompts by default unless explicitly changed.
- Load interface labels from locale files.
- Record language assumptions and locale status in verification.
- `en` and `zh-CN` are supported; other bundled locales are experimental.

## Core Pipeline

1. Run provider preflight; missing providers are not fatal.
2. Ingest and chunk source text with stable offsets.
3. Detect language, script, name system, and UI locale.
4. Set reader progress and spoiler-safe state.
5. Detect genre/atmosphere and create a spoiler-free theme profile.
6. Extract characters, places, organizations, objects, lore, relations, and events.
7. Resolve full names, titles, surnames, nicknames, and aliases conservatively.
8. Build character visual profiles and relationship/location/object codex data.
9. Build interpretive map data without inventing exact geography.
10. Build visual evidence with confirmed/contextual/inferred/unknown status.
11. Build reader paragraphs and entity links.
12. Create visual asset plan before image manifest or atlas rendering.
13. Bind provider, manual, prompt-only, or semantic placeholder assets.
14. Render localized `atlas.html` with Reader Sync and bidirectional jumps.
15. Validate every contract and write the verification report.

## Spoiler Rules

- Default to `safe` mode.
- Hide details marked `locked`.
- Do not place later revelations in portraits, backgrounds, summaries, or alt text.
- Full mode requires explicit user choice.

## Visual Provider Preflight

- Inspect configuration signals without printing secrets.
- A configured key is not a verified callable provider.
- Explicit user selection wins.
- Never auto-install providers, create accounts, or make paid calls.
- Fallback order: configured provider, manual assets, prompt-only, placeholder SVG.

## Theme Engine

- Derive theme from source motifs, not from unsupported plot assumptions.
- Keep backgrounds atmospheric, text-free, character-free, and spoiler-free.
- Record theme ID, palette, motifs, confidence, and background prompt.

## Reader Sync And Entity Jump

- Render source paragraphs with stable IDs.
- Highlight resolved characters, locations, organizations, objects, and lore.
- Clicking a highlight opens the matching codex entry.
- Clicking evidence opens the Reader panel and scrolls to the source paragraph.
- Persist reader open state, width, progress, font size, and line height locally.

## Fallback Rules

- Missing provider: continue with semantic SVG.
- Missing visual fact: use `unknown`, not invention.
- Ambiguous alias: keep candidates and report ambiguity.
- Missing geography: use interpretive map with a disclaimer.
- Missing locale key: fall back to English and keep experimental status.
- Never use initials-only avatars by default.

## Verification Checklist

- All required JSON/HTML files exist and parse.
- Major characters have portrait, half-body, and first-scene plans.
- Locations, map, objects/lore, and background have plans.
- Every asset has a unique manifest record and existing fallback file.
- Relation endpoints resolve and spoiler locks are preserved.
- Reader links resolve to both entities and paragraphs.
- Theme and locale are embedded in the atlas.
- Desktop and mobile Reader layouts are usable.
- No unsupported language or agent runtime is called fully supported.

## Final Response

Report output path, selected provider/fallback, input/UI language, theme, spoiler mode, test result, warnings, and known limitations.

Actor, writer, and director modes are future extensions, not core workflow steps.
