# Changelog

All notable changes to StoryVista will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [0.1.2] - 2026-06-03

### Changed

- Added 3D map rotation guidance: trackpad or touch rotation should use the map/grid center instead of an arbitrary node origin.
- Expanded mobile and tablet gesture rules for StoryVista 3D maps.
- Clarified that vertical one-finger swipes through a 3D map should preserve normal page scrolling.

### Added

- Gesture intent rules for mobile 3D maps: intercept only clear horizontal one-finger drags or two-finger map gestures.
- Verification guidance for map-centered rotation, pointer-centered zoom, horizontal map pan, two-finger pinch/rotate, and non-blocking mobile page scroll.

## [0.1.1] - 2026-06-03

### Changed

- Revised the StoryVista skill into a responsive-first interactive visual archive workflow.
- Clarified that default outputs should be explorable atlas pages, not Markdown-only summaries.
- Added stronger text-first entity modeling rules for characters, places, ships, technologies, powers, organizations, objects, and clues.
- Added template inheritance guidance for reusing successful previous atlas layouts and interaction patterns.
- Updated English and Chinese README pages with the revised skill direction.

### Added

- Responsive requirements for desktop, tablet, and mobile outputs.
- Character overview and relationship-tree rules for independent portrait cards, readable names, faction/function grouping, clickable avatars, and relationship highlighting.
- True 3D space-map rules for miniature models, animated planets, orbiting satellites, moving ships, clickable model bodies, and pointer-centered zoom.
- Expanded quality checklist for future StoryVista HTML outputs.

### Removed

- Rejected visual patterns from the recommended workflow: 2D image stickers, rounded photo-card space maps, album-wall layouts, fake 3D canvases, static nodes pretending to be models, and text-only clickable nodes.

## [0.1.0] - 2026-06-02

### Added

- Public beta README in English and Chinese.
- StoryVista skill package.
- Visual README assets.
- Quick start, examples, prompts, FAQ, roadmap, and keyword docs.
- Community files and issue templates.

### Known limitations

- Demo atlas examples are planned but not included.

### License

- MIT License.
