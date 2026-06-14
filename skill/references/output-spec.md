# Output Spec

Required v0.3 outputs:

- `source-index.json`, `chunks.json`, `language-profile.json`
- `reader-text.json`, `entity-linking.json`
- `character-atlas.json`, `relationship-web.json`
- `location-atlas.json`, `map-plan.json`
- `object-lore-codex.json`, `visual-evidence.json`
- compatibility aggregate `story-atlas.json`
- `visual-asset-plan.json`, `image-manifest.json`
- `spoiler-state.json`, `provider-choice-state.json`, `theme-profile.json`
- `assets/placeholders/*.svg`, `atlas.html`, `verification-report.md`

All image bindings come from `image-manifest.json`. Every asset records provider/fallback and provenance. Visual prompts record prompt, source, and UI language. Missing providers or visual facts must not make the output incomplete.
