# StoryVista v0.2.0 - Runnable Story Atlas

StoryVista v0.2.0 upgrades the project from a documentation-first Skill prototype to a runnable, evidence-aware Story Atlas pipeline.

## Highlights

- One-command, standard-library Python build
- Source index and stable text chunks
- Characters, locations, organizations, objects, concepts, relations, events, and timeline
- Evidence records with explicit, inferred, ambiguous, contradictory, and unresolved states
- Cinematic Bible interactive HTML atlas
- Reader Mode and Actor Mode prototype
- Semantic SVG portraits and location/event placeholders
- Provider-neutral visual asset plan and image manifest
- Fictional Chinese historical-drama demo: Wu Yue Night Rain
- Desktop and mobile browser-verified layouts

## Quick Start

```bash
python scripts/storyvista.py build skill/examples/minimal-novel-demo/input.txt --out output/minimal-novel-demo
python scripts/storyvista.py validate output/minimal-novel-demo
```

Open `output/minimal-novel-demo/atlas.html` after the build completes.

## Verification

- Demo build: 43 checks passed, 0 warnings
- pytest: 7 tests passed
- Desktop: 1440 x 900 verified
- Mobile: 390 x 844 verified
- Search, filters, evidence drawer, Actor Mode, image loading, overflow, and browser console checked

## Image Providers

Image generation is optional. Without a configured provider, StoryVista still produces prompts, `image-manifest.json`, and semantic SVG placeholders. Provider adapters remain an extension point rather than a runtime dependency.

## Known Limits

- The v0.2 extractor is intentionally conservative and directive-based.
- Actor Mode is a preparation prototype and may contain interpretation requiring human review.
- Paid image generation, advanced relationship graphs, 3D maps, and complete external agent runtimes are not included in this release.

## Rights and Privacy

Use only source text and images you are authorized to process. Unreleased manuscripts should remain local unless external processing is explicitly approved. Review AI-assisted output before public or commercial use.
