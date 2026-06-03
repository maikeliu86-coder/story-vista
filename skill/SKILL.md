---
name: story-vista
description: Use when turning novels, scripts, screenplays, lore bibles, long-form fiction, or other narrative text into reader-facing interactive visual atlases: character graphs, character indexes, scene/location maps, timelines, concept cards, and 3D world or space maps.
---

# StoryVista | 文景

StoryVista turns text worlds into visible, explorable archives. Use it when the user wants to understand a novel, screenplay, script, lore document, or story world through interactive visual structure rather than plain summary.

## Operating Posture

- Treat the default deliverable as a reader-facing interactive archive, not a Markdown-only report.
- Read the source text before designing visuals. Entity classification must come from the text, not from guessed aesthetics.
- Keep the skill general. Do not bind the workflow to any single source work; project examples are patterns, not templates with fixed content.
- Prefer a polished single-page HTML atlas when the user asks for something they can open, share, or explore.
- Preserve the user's requested output location and sync target when given.

## Default Atlas Sections

A complete StoryVista archive should normally include these sections unless the source or user request makes one irrelevant:

1. Hero and concise project framing.
2. Anchor navigation for major views.
3. Character thumbnail overview.
4. Character relationship tree.
5. Character index with detailed profiles.
6. Technology, power, weapon, device, object, and concept timeline.
7. Plot phase or event timeline.
8. Scene, location, planet, ship, route, or world-space map.
9. Interactive detail panel for selected people, places, concepts, and nodes.

## Text-First Entity Modeling

Build separate data models before visualizing:

- Characters: people, aliases, titles, roles, factions, relationship changes, and profile summaries.
- Places: rooms, cities, planets, kingdoms, facilities, routes, battlefields, stations, and recurring locations.
- Ships and vehicles: never place ships in the character relationship tree.
- Technologies and abilities: weapons, powers, devices, procedures, systems, and scientific concepts.
- Organizations and factions: institutions, crews, governments, families, cults, armies, companies, and alliances.
- Objects and clues: artifacts, documents, tools, motifs, secrets, evidence, and plot-critical items.

If a source item could fit multiple categories, record the ambiguity in data, then choose the visual surface that best matches its story function.

## Template Inheritance

When the user provides an existing page that they say is good, inherit its successful layout temperament and interaction logic before inventing a new design.

- Reuse the proven page rhythm, section order, visual density, controls, and interaction expectations.
- Replace all project-specific data with newly extracted source data.
- Do not copy obsolete mistakes from the old page. Apply the corrected rules in this skill first.

## Responsive-First Requirement

All HTML or web outputs must be designed for desktop, tablet, and mobile from the start.

Verify and adapt at these viewport classes:

- Desktop: about 1365 x 900 or wider.
- Tablet: about 768 x 1024.
- Mobile: about 390 x 844.

Mobile and tablet requirements:

- Full English and Chinese names must be readable without covering faces.
- Cards, controls, labels, and graph nodes need touch-sized click targets.
- Page scrolling must not be trapped by graph or 3D interaction areas.
- Thumbnail grids must reflow naturally and preserve image aspect ratio.
- Use `object-fit: cover` or equivalent cropping; never stretch or squash images.

Desktop requirements:

- Dual-column or side-detail panels must remain readable.
- Graphs and maps must support zoom, pan, click, and reset controls.
- Relationship labels must not be hidden underneath avatars, icons, or nodes.

## Character Visual Rules

- Character overview should use independent character cards, not a left-side composite image plus repeated cards.
- Each card should show a character portrait, English name, Chinese name, and a role/faction cue when useful.
- Names must remain complete on mobile. Prefer placing name bands below or in a lower-safe area instead of over faces.
- Clicking a character card should scroll or update to that character's profile.
- Relationship trees should prefer faction, function, or story-role grouping over chaotic all-to-all webs.
- Character nodes should be avatars when assets exist; both avatar and label must be clickable.
- Clicking a character should update a detail panel and highlight related characters and relationship edges.

## Technology And Timeline Rules

- Technologies, powers, weapons, devices, procedures, and special abilities should be ordered by story timeline or first reader-comprehension order.
- Each item should have a thumbnail or concept image when available, a concise definition, story function, first appearance, and related characters/places.
- Do not merge technologies with characters or locations just because one image resembles a person or place.

## 3D Space Map Rules

Use Three.js or an equivalent real-time 3D engine when the user asks for spatial relationships, planets, ships, facilities, routes, battlefields, or world maps.

Forbidden patterns:

- 2D image stickers in 3D space.
- Rounded photo cards, album-wall layouts, or floating screenshot panels.
- Fake 3D canvas that only moves flat icons.
- Nodes that always face the camera like billboards.
- Static nodes pretending to be 3D models.
- Only making text labels clickable while the model body cannot be clicked.

Default implementation:

- Build every location, planet, ship, city, base, prison, factory, ruin, station, and route as an independent 3D miniature model or holographic landmark.
- Models need volume, top/side surfaces, depth, shadow, rim light, and spatial occlusion.
- Planets rotate; moons orbit; ships drift, fly, or pulse along route lines; stations, cities, factories, and bases use animated lights or scanning effects.
- Use compressed universe scale: preserve relative distance, hierarchy, and spatial direction without copying real astronomical values literally.
- Node model bodies and labels must both support hover/click/tap and update the detail panel.
- Labels should be floating HUD text below or near the model, never pasted across the model body.

Gesture defaults:

- Desktop mouse press-drag: pan in the 2D screen plane.
- Trackpad two-finger scroll: change the 3D view direction.
- Pinch or `Ctrl`/`Meta` + wheel: zoom centered on the pointer location.
- Mobile/tablet: one-finger page scroll should work outside intentional interaction gestures; inside the 3D area, support two-finger pinch/rotate and tap-to-detail.

## Visual Design Direction

- Match the story domain rather than using a generic landing page.
- Keep operational atlas pages dense but readable: restrained color, clear hierarchy, and direct access to information.
- Use visual assets for characters, concepts, places, and spatial nodes when the user asks for an immersive archive.
- Avoid decorative clutter that competes with the story structure.

## Verification Checklist

Before calling a StoryVista output complete, verify:

- Source entities are separated into characters, places, ships, technologies, organizations, and objects.
- Ships or places are not accidentally included in the character relationship tree.
- Character cards click through or update details correctly.
- Relationship-tree clicks highlight the selected character's relevant people and edges.
- Technology and ability timelines use the intended order and have explanations.
- 3D canvas/WebGL is nonblank, models have visible volume, and node bodies are clickable.
- Zoom centers on the pointer where required.
- Desktop, tablet, and mobile screenshots show readable text and no major overlap.
- Image paths resolve and thumbnails are not stretched.
- Script syntax checks pass for generated HTML/JS.

## Output Habit

When producing files, provide the final file path, what was generated or changed, and what was verified. If verification was not possible, state the exact gap.
