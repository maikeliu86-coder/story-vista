# StoryVista v0.2 Upgrade Report

## Goal

Move StoryVista from a documentation-heavy concept to a runnable minimal Story Atlas pipeline.

## Delivered

- Standard-library Python CLI for build and validation
- Source index and stable chunk model
- Conservative directive-based extraction for entities, relations, events, and Actor Mode
- Evidence records with explicit/inferred/ambiguous/contradictory/unresolved states
- Visual asset plan, image manifest, and semantic SVG placeholders
- Dependency-free interactive Cinematic Bible atlas
- Fictional Chinese demo, JSON Schemas, and seven regression tests
- Consolidated provider documentation and shorter executable Skill instructions
- README-first run path, design docs, rights guidance, media plan, and release roadmap

## Verification Snapshot

- Demo build: 43 checks passed, 0 warnings
- Unit tests: 7 passed
- External image generation: not required for the baseline
- Browser verification: desktop 1440 x 900 and mobile 390 x 844 passed; navigation, search, evidence drawer, Actor Mode, image loading, overflow, and console state checked

## Known Limits

- Minimal extraction depends on explicit directives for deterministic rich output.
- Actor Mode is a preparation prototype and may include interpretation.
- Provider integrations, advanced graph layout, and 3D maps remain optional future work.
