# StoryVista Agent Instructions

StoryVista is a Codex-first, cross-agent compatible story visualization skill. Use it to turn novels, scripts, screenplays, lore documents, long-form prose, character notes, location notes, and timelines into interactive visual story atlases.

## Required Workflow

1. Parse source text.
2. Extract entities.
3. Classify entities by importance.
4. Build the story data model.
5. Run or offer Preflight Image Provider Check.
6. Run or offer Image Provider Diagnosis.
7. Apply Auto Mode provider selection.
8. Select `api`, `manual-assets`, `prompt-only`, or `placeholder-svg` mode.
9. Create `visual-asset-plan.json`.
10. Generate image prompts and/or images.
11. Create `image-manifest.json`.
12. Bind assets to character cards, location cards, relationship graphs, timelines, concept cards, detail panels, and 3D map nodes.
13. Generate the final interactive atlas.
14. Add a subtle image provider attribution note.
15. Run the verification checklist.

## Preflight And Auto Mode

StoryVista defaults to Auto Mode for image provider selection. Beginners should not be forced to choose from a long provider list. If exactly one verified provider is detected, use it. If multiple providers are detected, recommend the highest-scoring provider and explain why. If no provider is detected, continue with prompt-only or semantic placeholder mode.

Explicit user configuration always wins, and manual override must remain available. Missing provider is not a fatal error.

## Visual Asset Requirement

Do not build the final atlas before creating a visual asset plan. Every major character needs a planned or bound `character_portrait` asset. Every key location needs a planned or bound `location_keyart` asset.

## Image Provider Neutrality

StoryVista defines what images are needed, not where they are generated. Do not require a specific image model. Support configured providers, bring-your-own image models, manual assets, local folders, custom APIs, and semantic placeholder SVGs.

Do not print full API keys during diagnosis. Mask secrets and separate StoryVista generation status from image provider status.

## No Initials-Only Avatar By Default

Do not use initials-only avatars as default character portraits. Initials-only placeholders are allowed only as a last resort when explicitly enabled by the user or configuration. Default: `allow_initials_avatar: false`.

## Output Requirements

Expected outputs usually include:

- `story-atlas.json`
- `visual-asset-plan.json`
- `image-manifest.json`
- interactive `index.html` or equivalent atlas page when requested
- semantic placeholder assets when no image provider or user asset is available

## Verification Checklist

Before completion, verify:

- Major characters have `character_portrait` assets.
- Key locations have `location_keyart` assets.
- All images or placeholders are registered in `image-manifest.json`.
- Provider status, selected provider, selected mode, score, and selection reason are reported.
- The atlas contains a subtle provider attribution note.
- The atlas never silently substitutes missing images with initials.
- Generated HTML/JS passes syntax checks when applicable.
- Desktop, tablet, and mobile layouts are readable when an HTML atlas is produced.

## Read More

- Core workflow: `skill/SKILL.md`
- Cross-agent modes: `skill/references/cross-agent-compatibility.md`
- Image providers: `skill/references/image-provider-guide.md`
- Provider diagnosis: `skill/references/image-provider-diagnosis.md`
- Provider selection: `skill/references/provider-selection-policy.md`
- Provider switching: `skill/references/image-provider-switching.md`
- Asset generation: `skill/references/visual-asset-generation.md`
- Schemas and examples: `skill/templates/` and `skill/examples/`
