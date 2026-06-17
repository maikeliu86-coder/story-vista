# Golden Reference: Early StoryVista Experience

This document records the early StoryVista page used as the product and visual reference for future atlas work.

Reference URL:

https://stars-foyle-d0g83bqc72a3597ad-1438491763.tcloudbaseapp.com/qunxing-script-atlas/index.html

Local snapshot captured during review:

`tmp/golden-reference/qunxing-script-atlas/index.html`

## Access Result

The reference page was accessible and the HTML was saved locally. The page title is:

`《群星，我的归宿》电影剧本｜StoryVista 星际档案`

The saved page is a large self-contained HTML atlas with embedded CSS, data, interaction logic, and a bundled Three.js module payload.

## Overall Visual Style

The early page feels like a cinematic sci-fi archive rather than an engineering report. Its dominant traits are:

- deep starfield background with subtle scanline texture
- cyan and gold signal colors on a dark blue-black base
- terminal-like panels with translucent glass, glow, and strong borders
- large title and badge that immediately frame the page as a StoryVista atlas
- dense but readable sections that feel like a game codex or film concept database
- visual-first content, with images, graph nodes, timeline cards, and spatial maps appearing before operational instructions

## Page Information Hierarchy

The early page uses a clear reader-facing sequence:

1. Hero title and short framing
2. Sticky anchor navigation
3. Character thumbnail overview
4. Interactive character relationship tree
5. Character index
6. Technology / special ability timeline
7. Plot phase timeline
8. 3D space relationship map
9. Side detail panels updated by clicks

The important point is that the page starts as an explorable world archive. It does not start with provider diagnostics, validation status, or implementation details.

## Card Structure

Cards are compact but atmospheric:

- image or thumbnail first
- title and bilingual name when available
- role, faction, scene, or story function chips
- concise story-facing description
- click behavior that updates the relationship tree or detail panel

The card is not merely a record in a database. It is a small visual dossier.

## Character, Location, Worldbuilding, And Relationship Presentation

Characters:

- top-level thumbnail roster
- relationship graph with selectable nodes
- right-side detail panel with role, arc, first appearance, and relationships

Locations and spatial entities:

- separated from characters
- presented as world-space nodes
- connected through routes or story relationships
- rendered with a 3D spatial map in the reference page

Technology, powers, weapons, and concepts:

- grouped as a timeline of comprehension
- each entry has a visual thumbnail and a story function

Relationships:

- interactive graph first, list second
- selected character highlights relevant edges
- labels can be filtered or hidden

## Color, Typography, Space, And Interaction

Color:

- black-blue sci-fi foundation
- cyan for structure and signals
- gold for selected, important, or story-critical states
- red/pink for threat or conflict accents

Typography:

- large cinematic title
- readable sans-serif UI text
- serif or display treatment only for high-level framing

Spacing:

- generous section padding
- strong panel boundaries
- dense grids without feeling like spreadsheets

Interaction:

- sticky navigation
- clickable roster cards
- zoomable / pannable relationship graph
- detail side panel
- 3D space map with click targets

## Why It Matches The Desired StoryVista Direction

The early page succeeds because it treats StoryVista as a reader-facing artifact. The user sees a world, not a build pipeline. It feels like:

- a game codex
- a worldbuilding atlas
- a film concept dossier
- a navigable story archive

It also keeps categories separated: characters, technologies, places, and routes are not collapsed into one generic table.

## Current Version Differences

The newer version kept useful engineering features, but its final atlas drifted in these ways:

- more tool-like left navigation and diagnostics
- less cinematic framing
- card layout became generic and less archival
- relationship view became a list instead of a graph-first experience
- map view became a simple node canvas instead of a spatial story surface
- provider/fallback state became too visible in the user-facing page
- validation can pass even when the atlas is visually thin
- examples became text tables rather than examples of a finished visual atlas

## Recovery Direction

Future changes should restore the reference page's product feeling while preserving the newer runtime contracts:

- keep provider workflow, fallback, tests, docs, and schema outputs
- keep Reader Sync and evidence linking
- make final `atlas.html` feel like a visual story archive first
- keep operational details available, but lower in the hierarchy
- prioritize character roster, relationship field, visual cards, timelines, and map-like browsing

