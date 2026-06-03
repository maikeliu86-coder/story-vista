# StoryVista v0.1.2 — 3D Gesture Stability Update

## What changed

StoryVista now includes stronger guidance for cross-device 3D space-map interaction.

This update documents a tested interaction pattern:

- Trackpad rotation should pivot around the map or grid center, not a selected node or arbitrary scene origin.
- Pointer-centered zoom remains required where zoom is supported.
- Mobile and tablet vertical one-finger swipes through the 3D map should keep normal page scrolling.
- Clear horizontal one-finger drags may pan the map.
- Two-finger gestures should handle pinch zoom, center movement, and view rotation.

## Implementation guidance

For Three.js-style maps, keep a stable `mapCenter` in local scene coordinates. When rotating the map group, compare the world position of `mapCenter` before and after rotation and offset the group position by the difference. This keeps the grid center visually stable while the scene rotates.

For touch handling, do not call `preventDefault()` immediately on single-touch start. Wait until movement crosses a small threshold and the gesture is mostly horizontal. Let mostly vertical movement scroll the page. Intercept two-finger gestures immediately because they are intentional map gestures.

## Verification checklist

- Rotate the 3D map with a trackpad and confirm it pivots around the grid center.
- Confirm mobile vertical page scrolling is not trapped by the 3D map.
- Confirm mobile horizontal drag pans the map.
- Confirm mobile two-finger pinch/rotate changes the map.
- Confirm model bodies and labels remain clickable after gesture changes.
