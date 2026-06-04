# Visual Asset Generation

This guide explains how StoryVista creates visual assets without falling back to initials-only avatars.

## Extract Characters And Locations

Read the source text first. Identify names, aliases, titles, pronouns, relationships, recurring locations, scene headings, routes, and descriptions. Keep evidence snippets or chapter references when possible.

## Classify Importance

Major characters usually meet one or more conditions:

- viewpoint character, protagonist, antagonist, narrator, or major support role
- appears across multiple scenes or chapters
- drives a major relationship, conflict, reveal, or decision
- anchors a faction, location, timeline, or event

Key locations usually meet one or more conditions:

- repeated setting
- scene of a major event
- route hub or spatial anchor
- symbolic, political, magical, technological, or emotional importance

## Character Visual Description

For each major character, produce a structured visual brief with canonical name, aliases, role, age range, gender presentation when available, appearance, clothing, era or genre context, personality cues, expression, pose, color palette, prompt, negative prompt, aspect ratio, filename, and binding targets.

Do not reduce a character to two letters. If the text lacks appearance details, infer only genre-safe, non-contradictory visual cues and mark uncertain fields in notes.

## Location Visual Description

For each key location, produce geography, architecture, time period, atmosphere, narrative function, lighting, color palette, prompt, negative prompt, aspect ratio, filename, and binding targets.

## Prompt Strategy

Start with a provider-neutral prompt:

```text
Portrait of [canonical_name], [role], [age_range], [appearance_summary], [clothing_style], [era_or_genre_context], [personality_visual_cues], [expression_default], [pose_default], palette [color_palette], story illustration style, clear face, no text.
```

Then create provider-specific variants only when the selected provider requires syntax changes.

## Image Manifest

Every planned, generated, user-provided, missing, placeholder, or failed asset must be represented in `image-manifest.json`. Use stable ids and filenames.

Before creating the visual asset plan, run or offer the Preflight Image Provider Check and apply Auto Mode provider selection. The selected provider affects prompt variants, output folders, generation mode, and attribution text, but it must not change the requirement that every major character and key location receives an asset entry.

## Binding Targets

Bind assets to:

- character cards
- relationship graph
- timeline
- 3D map
- location cards
- concept cards
- detail panels

Relationship graph nodes and 3D map nodes should point to asset ids, not embedded ad hoc image paths.

## Avoid Initials-Only Avatars

Default fallback is semantic SVG placeholder with full entity name, entity type, and asset category. Initials-only placeholder is last resort and requires explicit permission.

If no provider is available, mark assets as `prompt_ready` or `placeholder` rather than removing them from the plan.
