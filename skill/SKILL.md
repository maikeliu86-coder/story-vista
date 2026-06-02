---
name: story-interactive-archive
description: Build or update an Obsidian-ready interactive archive page for a novel, script, screenplay, or worldbuilding project. Use when the user wants character relationship trees, character indexes, technology/timeline panels, place/ship/space maps, GPT-Image/Image2 asset matching, mobile-friendly interaction, public static deployment, or synchronization between Obsidian local files and a shareable website.
---

# Story Interactive Archive

## Operating Posture

Treat the archive as a durable knowledge artifact, not a throwaway web page.

Start from the source text and the user's prior accepted decisions. Preserve the story's names, relationships, chronology, and spatial logic. When the page already exists, keep its working layout and interaction patterns unless the user explicitly asks to redesign them.

Use [references/implementation-notes.md](references/implementation-notes.md) when building or changing a full archive page, generating one-to-one images, syncing Obsidian and public hosting, or implementing 3D space maps.

## Workflow

1. Locate the source materials and target files.
   - Prefer the user's Obsidian vault path when provided.
   - Find existing HTML/Markdown/public copies with `rg`.
   - Identify the canonical local page, public deploy copy, source record, and asset folders before editing.

2. Read the story before classifying entities.
   - Extract characters, factions, technology, special abilities, locations, vehicles, timelines, routes, and spatial relationships from the text.
   - Correct false entity types. For example, a ship is not a character even if it has a proper name.
   - Treat uncertain matches as provisional and mark them for review rather than inventing precision.

3. Build the archive around usable sections.
   - Character overview grid with full Chinese and English names.
   - Interactive character relationship tree with click-to-detail side panel.
   - Character index with portraits and summaries.
   - Technology/special ability timeline in story order.
   - Location/ship/space relationship map with click-to-detail side panel.
   - Source record links for Obsidian and public sharing.

4. Bind generated or provided images one-to-one.
   - Match thumbnails to specific characters, technologies, places, ships, and scenes by reading the text and visible image content.
   - Avoid duplicate image assignments unless the story genuinely reuses a concept.
   - For Image2 work, generate per-object assets, then bind them into the exact slots in the HTML. Do not leave placeholder mood-board images.

5. Make interactions work on desktop and mobile.
   - Desktop: pointer drag rotates or pans as appropriate; trackpad pinch/wheel zoom is centered and natural.
   - Mobile: touch scrolling outside interactive canvases should not feel trapped; pinch zoom should work inside interaction surfaces.
   - Click or tap on names, thumbnails, relationship nodes, place nodes, and ship nodes must update the side/detail panel.

6. For space maps, prefer real-time 3D over fake depth.
   - Do not use flat photo cards, image walls, rounded image boards, or 2D screenshots pasted into 3D space.
   - Model places as miniature 3D landmarks, planet systems, cities, stations, ships, asteroid fields, route lines, or holographic nodes.
   - Use compressed story/world scale when true distances are too large. Preserve relative order and spatial hierarchy rather than equal spacing.

7. Verify before finalizing.
   - Syntax-check embedded scripts by extracting `<script>` content into a JS parser.
   - Serve locally and verify the rendered page with Browser when available.
   - Check at least one desktop and one mobile viewport for nonblank render, no console-breaking errors, readable labels, and click-to-detail behavior.
   - Deploy only after local verification when public hosting is part of the task.

8. Sync all surfaces.
   - Update the Obsidian HTML file.
   - Update any public/static copy.
   - Update the Obsidian source record or index note with the current public URL and cache-busting parameter if needed.
   - Deploy to the selected static host and verify the hosted file.

## Implementation Rules

- Keep changes surgical. Do not refactor unrelated sections.
- Use `apply_patch` for manual edits; use small mechanical scripts only when editing a large generated HTML safely.
- Use existing page style, data structures, and helper functions before inventing new frameworks.
- When the page is a single static HTML, keep it self-contained unless the deployment target supports and needs external assets.
- Avoid copyright-heavy copying. Source records may link to sources and contain limited lawful excerpts, but should not mirror an entire copyrighted book or script.
- If using public sharing, remind the user that friends need a public URL, not a `file://` Obsidian path.

## Acceptance Checklist

- Obsidian page opens locally.
- Public page opens with a shareable URL.
- Character and place nodes are clickable.
- Mobile layout does not hide full names or trap normal scrolling.
- Relationship labels do not sit under nodes or avatars.
- Images match the correct entities and duplicates have been checked.
- 3D maps show actual depth through coordinates, camera rotation, height/depth offsets, and scale guides.
- Obsidian source record points to the current public version.
