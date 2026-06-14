# Core Pipeline

`scripts/storyvista.py build <input> --out <directory> --ui-language auto` runs the v0.3 standard-library pipeline:

1. detect provider configuration and safe fallback
2. ingest and chunk source text
3. detect input language, script, name system, and UI locale
4. extract entities and resolve aliases conservatively
5. build spoiler state and atmosphere theme
6. build character, relationship, location, map, object/lore, and visual-evidence data
7. create reader paragraphs and entity links
8. plan and bind visual assets
9. generate semantic SVG fallback assets
10. render the localized Reader Visual Codex
11. validate contracts and write the verification report

Advanced NLP, real provider calls, graph engines, and geographic simulation remain optional adapters. The core must stay runnable offline.
