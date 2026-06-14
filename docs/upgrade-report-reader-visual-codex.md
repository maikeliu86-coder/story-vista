# StoryVista v0.3 Reader Visual Codex Upgrade Report

## Result

StoryVista has been redirected from an actor-oriented Story Atlas into a multilingual, spoiler-safe visual reading companion for complex novels.

## Main Changes

- Rebuilt the CLI pipeline around language detection, alias resolution, reader text, entity linking, character visual profiles, relationship web, location atlas, interpretive maps, object/lore codex, visual evidence, spoiler state, provider preflight, theme profile, visual planning, manifest binding, rendering, and verification.
- Replaced the Actor Mode HTML surface with a Game Codex interface and Reader Sync Panel.
- Added forward entity jumps, reverse evidence jumps, hover labels, reader search, draggable width, collapse/full-screen behavior, and localStorage persistence.
- Rewrote README and SKILL around the reader mission. Actor, writer, and director modes are future extensions.
- Added English and Simplified Chinese supported locales plus experimental `zh-TW`, `ja`, `ko`, `fr`, `es`, `de`, and `ru` structures.
- Added schemas, tests, six reader demos, generated expected output, and current product documentation.

## Added Modules

`language_detection.py`, `i18n.py`, `alias_resolver.py`, `entity_extraction.py`, `visual_profile.py`, `visual_evidence.py`, `relationship_web.py`, `location_atlas.py`, `map_planner.py`, `object_lore_codex.py`, `reader_text.py`, `entity_linking.py`, `spoiler.py`, `provider_preflight.py`, and `theme_engine.py`.

## Reader Visual Codex Status

- Character Atlas: implemented with aliases, memory labels, localized-name fields, and explicit visual-profile status.
- Relationship Web: implemented with visible/locked spoiler states.
- Location Atlas and map plan: implemented; map defaults to interpretive and includes a no-false-precision disclaimer.
- Object & Lore Codex: implemented for objects, weapons, potions, technology, magic, and concepts.
- Reader Sync Panel: implemented for desktop and mobile.
- Entity Highlight & Jump: implemented in both directions.
- Provider Preflight: implemented as non-secret configuration detection with local fallback.
- Theme Engine: implemented with literary archive, ancient Chinese, and futuristic sci-fi presets.
- Semantic placeholders: implemented for every planned asset; initials-only avatars remain disabled.

## Language And Agent Status

English and Simplified Chinese input/UI paths are tested. Other locale files are experimental. Script detection exists for additional writing systems, but advanced multilingual extraction is not claimed.

The CLI is verified without an agent. Codex, Claude Code, Cursor, Qwen Code, Trae, IDE agents, and orchestration frameworks can invoke the same command, but not every product runtime has been tested end to end.

## Demos

- English full demo: `skill/examples/reader-visual-codex-demo`
- English compact demo: `skill/examples/english-reader-demo`
- Chinese demo: `skill/examples/chinese-reader-demo`
- Bilingual demo: `skill/examples/bilingual-demo`
- Ancient Chinese demo: `skill/examples/ancient-chinese-demo`
- Futuristic sci-fi demo: `skill/examples/futuristic-sci-fi-demo`
- Generated main output: `skill/examples/reader-visual-codex-demo/expected`

## Verified Quick Start

```bash
python scripts/storyvista.py build skill/examples/reader-visual-codex-demo/input.txt --out output/reader-visual-codex-demo --ui-language auto
```

The command generates the required JSON, SVG, HTML, and verification artifacts with no provider and no runtime dependency beyond Python.

## Tests

The automated suite covers the Quick Start, language overrides, locale status, aliases, visual-profile statuses, reader linking, spoiler locks, provider fallback, themes, HTML controls, legacy placeholder compatibility, relation integrity, and schemas.

## Current Limits

- Extraction is deterministic and directive-assisted; it is not a general literary NLP model.
- Localization fields are present but automatic proper-name translation is intentionally absent.
- Relationship and map views are dependency-free visualizations, not advanced graph/GIS engines.
- Provider preflight detects configuration signals; actual provider calls remain optional future integrations.
- Experimental locales need native-speaker review and broader extraction rules.

## Next Recommendation

Use v0.4 for real provider adapters and asset-quality/version workflows. Preserve the v0.3 local fallback and spoiler/evidence contracts as non-optional foundations.
