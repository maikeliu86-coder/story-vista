# StoryVista Agent Instructions

StoryVista is a runnable multilingual Reader Visual Codex. Keep the dependency-free CLI, spoiler-safe reader workflow, and semantic fallback working before adding optional adapters or providers.

## Primary Command

```bash
python scripts/storyvista.py build skill/examples/minimal-novel-demo/input.txt --out output/minimal-novel-demo
```

## Required Pipeline

1. Ingest source and create `source-index.json` plus `chunks.json`.
2. Detect language and model characters, aliases, relations, locations, objects/lore, events, reader text, entity links, spoilers, and evidence.
3. Mark claims as `explicit`, `inferred`, `ambiguous`, `contradictory`, or `unresolved`.
4. Create `visual-asset-plan.json` before rendering.
5. Create `image-manifest.json`, semantic placeholders, and `atlas.html`.
6. Validate and write `verification-report.md`.

## Engineering Rules

- Prefer the Python standard library and existing repository patterns.
- Keep changes small, reproducible, and covered by targeted tests.
- Do not invent missing story facts; preserve unresolved states.
- Do not make image providers a prerequisite for atlas generation.
- Bind all visuals through `image-manifest.json`.
- Keep `allow_initials_avatar: false` unless the user explicitly opts in.
- Mask secrets and avoid paid provider calls during diagnosis.
- Treat files in `skill/agents/` as adapter documentation unless executable runtime code exists.

## Verification

Run:

```bash
python -m unittest discover -s tests -v
python scripts/storyvista.py validate output/minimal-novel-demo
```

For HTML changes, also check embedded JavaScript syntax and verify desktop/mobile layouts, navigation, search, Reader Sync, bidirectional jumps, spoiler locks, settings persistence, image loading, and console errors.

## Canonical References

- Workflow: `skill/SKILL.md`
- Pipeline: `skill/references/core-pipeline.md`
- Data: `skill/references/data-contracts.md`
- Fallbacks: `skill/references/fallback-rules.md`
- Verification: `skill/references/verification.md`
- Image providers: `skill/references/image-provider.md`
