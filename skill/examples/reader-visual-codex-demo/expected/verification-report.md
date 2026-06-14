# StoryVista Verification Report

## Result
- Passed checks: 65
- Warnings: 0
- Input language: en
- UI language: en
- UI locale status: supported
- Provider status: fallback-selected
- Selected provider: placeholder-svg
- Theme: futuristic-sci-fi
- Atlas generation status: complete

## Passed Checks
- Exists: source-index.json
- Valid JSON: source-index.json
- Exists: chunks.json
- Valid JSON: chunks.json
- Exists: language-profile.json
- Valid JSON: language-profile.json
- Exists: reader-text.json
- Valid JSON: reader-text.json
- Exists: entity-linking.json
- Valid JSON: entity-linking.json
- Exists: character-atlas.json
- Valid JSON: character-atlas.json
- Exists: relationship-web.json
- Valid JSON: relationship-web.json
- Exists: location-atlas.json
- Valid JSON: location-atlas.json
- Exists: map-plan.json
- Valid JSON: map-plan.json
- Exists: object-lore-codex.json
- Valid JSON: object-lore-codex.json
- Exists: visual-evidence.json
- Valid JSON: visual-evidence.json
- Exists: story-atlas.json
- Valid JSON: story-atlas.json
- Exists: visual-asset-plan.json
- Valid JSON: visual-asset-plan.json
- Exists: image-manifest.json
- Valid JSON: image-manifest.json
- Exists: spoiler-state.json
- Valid JSON: spoiler-state.json
- Exists: provider-choice-state.json
- Valid JSON: provider-choice-state.json
- Exists: theme-profile.json
- Valid JSON: theme-profile.json
- Exists: atlas.html
- Major character has entity_id: Lord Elias Alexander Varron
- Major character has entity_id: Doctor Mirabelle Saye Ashcroft
- Major character has entity_id: Captain Aleksandr Ilyich Petrov
- Relation integrity: rel_001
- Relation evidence state recorded: rel_001
- Relation integrity: rel_002
- Relation evidence state recorded: rel_002
- Relation integrity: rel_003
- Relation evidence state recorded: rel_003
- Visual asset ids are unique
- Manifest asset ids are unique
- Placeholder exists: asset_char_001_portrait
- Placeholder exists: asset_char_001_half_body
- Placeholder exists: asset_char_001_first_scene
- Placeholder exists: asset_char_002_portrait
- Placeholder exists: asset_char_002_half_body
- Placeholder exists: asset_char_002_first_scene
- Placeholder exists: asset_char_003_portrait
- Placeholder exists: asset_char_003_half_body
- Placeholder exists: asset_char_003_first_scene
- Placeholder exists: asset_loc_001_keyart
- Placeholder exists: asset_loc_002_keyart
- Placeholder exists: asset_loc_003_keyart
- Placeholder exists: asset_obj_001_codex
- Placeholder exists: asset_obj_002_codex
- Placeholder exists: asset_lore_001_codex
- Placeholder exists: asset_story_map
- Placeholder exists: asset_atlas_background
- Every major character has a portrait asset
- Initials-only avatars disabled

## Warnings
- None

## Unresolved Evidence
- None

## Ambiguous Entity Links
- None

## Missing Optional Assets
- API-generated images are optional in v0.3; semantic placeholders are present.

## Next Steps
- Review inferred visual details and ambiguous aliases before publishing.
- Replace placeholder assets through image-manifest.json when licensed images are available.
- Review evidence tags before publishing the atlas.
