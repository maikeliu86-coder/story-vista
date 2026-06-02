---
name: story-vista
description: Build or update an interactive visual knowledge atlas for novels, scripts, screenplays, long-form prose, roleplaying worlds, or any text-heavy story material. Use when the user wants to make written content easier to understand through character relationship maps, scene/location networks, timelines, concept/technology cards, Image2/GPT-Image visual assets, mobile-friendly interaction, Obsidian integration, public static sharing, or real-time 3D world/space maps.
---

# StoryVista

## Operating Posture

Treat the archive as a reader-facing visual atlas for a text world, not as a private engineering artifact.

Use this skill for people who want to understand, teach, discuss, adapt, or remember complex written material: readers, writers, screenwriters, students, researchers, worldbuilders, and production teams. The goal is to turn abstract text into a clear interactive structure: who matters, how they relate, where events happen, what changes over time, and how scenes or places connect.

Use [references/implementation-notes.md](references/implementation-notes.md) when building or changing a full visual atlas, generating one-to-one images, syncing Obsidian and public hosting, or implementing 3D scene/space maps.

## Product Positioning

Name: **StoryVista**

Chinese name: **文景**

Taglines:

- English: **Make Text Worlds Visible**
- Chinese: **让文字世界看得见**

Explain it simply: StoryVista turns novels, scripts, notes, and long text into interactive visual archives for characters, scenes, timelines, concepts, and world maps.

## Workflow

1. Locate the source materials and target files.
   - Prefer the user's Obsidian vault path when provided.
   - Find existing HTML/Markdown/public copies with `rg`.
   - Identify the canonical local page, public deploy copy, source record, and asset folders before editing.

2. Read the text before classifying entities.
   - Extract characters, groups, settings, scenes, props, technologies, special abilities, locations, vehicles, timelines, routes, and spatial relationships.
   - Correct false entity types. For example, a ship, city, object, or organization is not a character even if it has a proper name.
   - Treat uncertain matches as provisional and mark them for review rather than inventing precision.

3. Build the atlas around reader questions.
   - Who are the people and how do they relate?
   - Where do scenes happen and how do places connect?
   - What events happen in what order?
   - What concepts, powers, technologies, symbols, or objects matter?
   - Which images help readers recognize each person, place, or concept?

4. Create useful sections.
   - Character overview grid with full names.
   - Interactive character relationship tree with click-to-detail side panel.
   - Character index with portraits and summaries.
   - Timeline for plot events, technologies, abilities, or scene progression.
   - Scene/location/ship/world relationship map with click-to-detail side panel.
   - Source record links for Obsidian and public sharing.

5. Bind generated or provided images one-to-one.
   - Match thumbnails to specific characters, concepts, scenes, locations, ships, and objects by reading the text and visible image content.
   - Avoid duplicate image assignments unless the story genuinely reuses a concept.
   - For Image2 work, generate per-object assets, then bind them into the exact slots in the HTML. Do not leave placeholder mood-board images.

6. Make interactions work on desktop and mobile.
   - Desktop: pointer drag rotates or pans as appropriate; trackpad pinch/wheel zoom is centered and natural.
   - Mobile: touch scrolling outside interactive canvases should not feel trapped; pinch zoom should work inside interaction surfaces.
   - Click or tap on names, thumbnails, relationship nodes, scene nodes, place nodes, and object nodes must update the side/detail panel.

7. For 3D maps, prefer real-time models over fake depth.
   - Do not use flat photo cards, image walls, rounded image boards, or 2D screenshots pasted into 3D space.
   - Model places as miniature landmarks, rooms, planets, cities, stations, ships, route lines, or holographic nodes.
   - Use compressed story/world scale when true distances are too large. Preserve relative order and spatial hierarchy rather than equal spacing.

8. Verify before finalizing.
   - Syntax-check embedded scripts by extracting `<script>` content into a JS parser.
   - Serve locally and verify the rendered page with Browser when available.
   - Check at least one desktop and one mobile viewport for nonblank render, no console-breaking errors, readable labels, and click-to-detail behavior.
   - Deploy only after local verification when public hosting is part of the task.

9. Sync all surfaces.
   - Update the Obsidian HTML file.
   - Update any public/static copy.
   - Update the Obsidian source record or index note with the current public URL and cache-busting parameter if needed.
   - Deploy to the selected static host and verify the hosted file.

## Implementation Rules

- Keep changes surgical. Do not refactor unrelated sections.
- Use `apply_patch` for manual edits; use small mechanical scripts only when editing a large generated HTML safely.
- Use existing page style, data structures, and helper functions before inventing new frameworks.
- When the page is a single static HTML, keep it self-contained unless the deployment target supports and needs external assets.
- Avoid copyright-heavy copying. Source records may link to sources and contain limited lawful excerpts, but should not mirror an entire copyrighted book, script, or article.
- If using public sharing, remind the user that friends need a public URL, not a `file://` Obsidian path.

## Acceptance Checklist

- Obsidian page opens locally.
- Public page opens with a shareable URL when requested.
- Character and scene/place nodes are clickable.
- Mobile layout does not hide full names or trap normal scrolling.
- Relationship labels do not sit under nodes or avatars.
- Images match the correct entities and duplicates have been checked.
- 3D maps show actual depth through coordinates, camera rotation, height/depth offsets, and scale guides.
- Obsidian source record points to the current public version when public sharing is involved.
