# StoryVista v0.1.1 — Responsive Interactive Atlas Update

## What changed

StoryVista is now documented as a responsive-first workflow for building interactive visual story archives across desktop, tablet, and mobile.

The skill now emphasizes:

- Interactive atlas pages instead of Markdown-only summaries.
- Text-first entity modeling before visual design.
- Clear separation between characters, places, ships, technologies, powers, organizations, objects, and clues.
- Template inheritance when users provide a successful previous atlas.
- Character views with independent portrait cards, clickable avatars, and relationship highlighting.
- True 3D space maps built from miniature models rather than flat image cards.

## New responsive rules

Future StoryVista HTML outputs should be checked at desktop, tablet, and mobile sizes.

- Desktop: readable dual-column panels and zoomable/clickable graphs.
- Tablet: touch-sized controls and stable layout.
- Mobile: full names, no face-covering labels, normal page scroll, and adaptive thumbnail grids.

## New 3D map rules

StoryVista spatial maps should use real model volume when spatial relationships matter.

- Planets rotate.
- Moons orbit.
- Ships drift or move along routes.
- Stations, bases, cities, factories, prisons, and ruins use miniature 3D structures.
- Model bodies and labels are both clickable.
- Zoom should center on the pointer when supported.

Rejected patterns include 2D image stickers, rounded photo cards, album walls, fake 3D canvases, static nodes pretending to be models, and text-only clickable nodes.

## Upgrade note

Replace your installed `story-vista` skill folder with the repository `skill/` folder to use this revised workflow:

```bash
rm -rf "$HOME/.codex/skills/story-vista"
cp -R skill "$HOME/.codex/skills/story-vista"
```
