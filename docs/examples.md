# Example Workflows

## 1. Novel reader workflow

- User goal: remember a complex novel.
- Input type: novel chapters or reading notes.
- Suggested prompt: `Use $story-vista to map the characters, relationships, places, timeline, key objects, and recurring motifs in this novel.`
- Expected output: character graph, timeline, place index, object/motif list.
- Review checklist: check aliases, spoilers, and relationship direction.

## 2. Screenwriter workflow

- User goal: inspect story structure.
- Input type: screenplay draft.
- Suggested prompt: `Use $story-vista to break this screenplay into characters, scene objectives, locations, conflicts, reveals, and unresolved threads.`
- Expected output: scene atlas, relationship map, unresolved thread list.
- Review checklist: confirm scene order and character motivations.

## 3. Actor preparation workflow

- User goal: prepare a role.
- Input type: script or sides.
- Suggested prompt: `Use $story-vista to create a role-preparation atlas: relationships, objectives, obstacles, actions, emotional beats, and character arc.`
- Expected output: role map, scene tasks, opponent relationships, emotional timeline.
- Review checklist: verify that choices remain actor-interpretable, not prescriptive.

## 4. Director / producer workflow

- User goal: align a creative team.
- Input type: screenplay, treatment, or series bible.
- Suggested prompt: `Use $story-vista to produce a team-facing story map with character lines, location lines, plot beats, factions, and production-relevant world details.`
- Expected output: team story map and consistency checklist.
- Review checklist: ensure locations, props, and factions are actionable.

## 5. RPG worldbuilding workflow

- User goal: organize a campaign setting.
- Input type: lore notes, NPC list, maps, quest notes.
- Suggested prompt: `Use $story-vista to turn this RPG setting into factions, NPCs, locations, quests, artifacts, routes, and timeline views.`
- Expected output: lore atlas, faction graph, location network, quest timeline.
- Review checklist: confirm player-facing vs GM-only information.

## 6. Student literature analysis workflow

- User goal: analyze a literary work.
- Input type: assigned reading, notes, public-domain text, or excerpts.
- Suggested prompt: `Use $story-vista to analyze this text through character relationships, recurring symbols, themes, locations, and plot structure.`
- Expected output: analysis map and evidence-linked notes.
- Review checklist: avoid replacing close reading with generated conclusions.

## 7. Obsidian archive workflow

- User goal: build a personal knowledge archive.
- Input type: vault notes and source records.
- Suggested prompt: `Use $story-vista to create an Obsidian-ready story archive with source records, character maps, scene maps, timeline, and concept index.`
- Expected output: local HTML archive and linked source note.
- Review checklist: local paths should not appear in public links.

## 8. Static visual atlas workflow

- User goal: share a story atlas publicly.
- Input type: finalized archive and rights-cleared source summaries.
- Suggested prompt: `Use $story-vista to prepare this story atlas for public static hosting, with mobile checks and safe source attribution.`
- Expected output: static HTML, asset folder, public URL plan.
- Review checklist: copyright, privacy, mobile layout, and public URL.

## 9. Responsive interactive atlas workflow

- User goal: create one archive that works on desktop, tablet, and mobile.
- Input type: novel, screenplay, story bible, or long-form notes.
- Suggested prompt: `Use $story-vista to build a responsive interactive visual atlas. Separate characters, places, ships, technologies, powers, organizations, objects, and clues before designing the page. Include clickable character cards, a grouped relationship tree, timelines, and mobile-safe layouts.`
- Expected output: interactive HTML atlas with adaptive grids, clickable cards/nodes, readable labels, and device-specific interaction behavior.
- Review checklist: desktop/tablet/mobile screenshots, full names on mobile, no stretched images, graph clicks, timeline clicks, and non-blocking page scroll.

## 10. True 3D space-map workflow

- User goal: understand spatial relationships between worlds, ships, facilities, cities, rooms, routes, or battlefields.
- Input type: science-fiction, fantasy, adventure, war, or spatially complex story material.
- Suggested prompt: `Use $story-vista to create a true 3D spatial map. Build planets, ships, bases, stations, cities, and routes as miniature 3D models with animation. Do not use flat image cards. Make model bodies and labels clickable.`
- Expected output: WebGL/Three.js spatial view with rotating planets, orbiting satellites, animated ships or routes, clickable models, pointer-centered zoom, and a side detail panel.
- Review checklist: canvas is nonblank, models have volume, nodes are not billboards, body click works, labels are readable, and mobile gestures do not trap normal scrolling.
