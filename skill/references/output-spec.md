# Output Spec

StoryVista outputs are portable artifacts that can be used by coding agents, chat agents, and agent frameworks.

## Required Structured Outputs

- `story-atlas.json`: canonical story data model.
- `visual-asset-plan.json`: required visual assets and prompts before generation.
- `image-manifest.json`: image status, provider, filenames, and binding targets.

## Optional User-Facing Outputs

- `index.html` or a named atlas HTML file.
- `assets/images/` for generated or supplied images.
- `assets/placeholders/` for semantic SVG placeholders.
- supporting README or notes.

## Atlas Binding Rule

The atlas should reference image assets by `image_asset_id`. Characters and locations should not store only initials or raw display names as default image substitutes.
