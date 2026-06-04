# StoryVista Agent Instructions

StoryVista is a Codex-first, cross-agent compatible story visualization skill. Use it to turn novels, scripts, screenplays, lore documents, long-form prose, character notes, location notes, and timelines into interactive visual story atlases.

## Required Workflow

1. Parse source text.
2. Extract entities.
3. Classify entities by importance.
4. Build the story data model.
5. Create `visual-asset-plan.json`.
6. Generate image prompts and/or images.
7. Create `image-manifest.json`.
8. Bind assets to character cards, location cards, relationship graphs, timelines, concept cards, detail panels, and 3D map nodes.
9. Generate the final interactive atlas.
10. Run the verification checklist.

## Visual Asset Requirement

Do not build the final atlas before creating a visual asset plan. Every major character needs a planned or bound `character_portrait` asset. Every key location needs a planned or bound `location_keyart` asset.

## Image Provider Neutrality

StoryVista defines what images are needed, not where they are generated. Do not require a specific image model. Support configured providers, bring-your-own image models, manual assets, local folders, custom APIs, and semantic placeholder SVGs.

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
- The atlas never silently substitutes missing images with initials.
- Generated HTML/JS passes syntax checks when applicable.
- Desktop, tablet, and mobile layouts are readable when an HTML atlas is produced.

## Read More

- Core workflow: `skill/SKILL.md`
- Cross-agent modes: `skill/references/cross-agent-compatibility.md`
- Image providers: `skill/references/image-provider-guide.md`
- Asset generation: `skill/references/visual-asset-generation.md`
- Schemas and examples: `skill/templates/` and `skill/examples/`
