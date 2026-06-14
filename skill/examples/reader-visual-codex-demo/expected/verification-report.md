# StoryVista Verification Report

## Result
- Passed checks: 67
- Warnings: 0
- Input language: en
- UI language: en
- UI locale status: supported
- Provider status: prompt-workflow-ready
- Recommended provider: openai-image
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
- Exists: prompt-pack.md
- Exists: manual-generation-instructions.md
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
- Display and fallback assets exist: asset_char_001_portrait
- Display and fallback assets exist: asset_char_001_half_body
- Display and fallback assets exist: asset_char_001_first_scene
- Display and fallback assets exist: asset_char_002_portrait
- Display and fallback assets exist: asset_char_002_half_body
- Display and fallback assets exist: asset_char_002_first_scene
- Display and fallback assets exist: asset_char_003_portrait
- Display and fallback assets exist: asset_char_003_half_body
- Display and fallback assets exist: asset_char_003_first_scene
- Display and fallback assets exist: asset_loc_001_keyart
- Display and fallback assets exist: asset_loc_002_keyart
- Display and fallback assets exist: asset_loc_003_keyart
- Display and fallback assets exist: asset_obj_001_codex
- Display and fallback assets exist: asset_obj_002_codex
- Display and fallback assets exist: asset_lore_001_codex
- Display and fallback assets exist: asset_story_map
- Display and fallback assets exist: asset_atlas_background
- Every major character has a portrait asset
- Initials-only avatars disabled

## Warnings
- None

## Unresolved Evidence
- None

## Ambiguous Entity Links
- None

## Missing Optional Assets
- Manifest status counts: {'pending_external_generation': 17}
- Real images may remain pending external generation; semantic placeholders are display fallbacks.

## Manual Image Binding
- Successfully bound: 0
- Unmatched files: []

## Next Steps
- Review inferred visual details and ambiguous aliases before publishing.
- Use prompt-pack.md or provider-specific prompt files, then bind generated files with the CLI.
- Review evidence tags before publishing the atlas.
