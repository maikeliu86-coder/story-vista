# StoryVista Implementation Notes

These notes capture durable implementation rules for StoryVista HTML atlases. They are project-agnostic and should be applied to novels, scripts, screenplays, lore bibles, and other narrative text.

## Purpose

StoryVista outputs should help readers, writers, students, screenwriters, researchers, and worldbuilders see the hidden structure of a text: people, aliases, relationships, places, movement, concepts, technologies, plot phases, and world geometry.

The target is an interactive visual archive, not a decorative summary page.

## Confirmed Page Structure

A full archive should normally use this structure:

1. Hero with title, subtitle, and short framing.
2. Anchor navigation.
3. Character thumbnail overview.
4. Character relationship tree.
5. Character index and profiles.
6. Technology and ability timeline.
7. Plot phase or event timeline.
8. 3D space relationship map for places, ships, planets, routes, or worlds.
9. Detail panel updated by clicks from cards, graph nodes, timeline items, and 3D nodes.

Keep the first screen useful. Do not turn the page into a marketing landing page unless explicitly requested.

## File Surfaces

Typical outputs:

- `index.html` or a named single-file HTML atlas.
- `data/*.json` only when the page architecture benefits from structured separation.
- `assets/` for generated or cropped images.
- `README` or notes only as supporting material, not the main deliverable when the user requested an interactive page.

## Character And Entity Extraction

Read the source before visual design. Extract and classify separately:

- Characters: names, aliases, translations, roles, relationships, factions, arc notes.
- Locations: rooms, cities, planets, bases, stations, routes, geographic areas, recurring places.
- Ships and vehicles: model separately from people; ships must not appear in character trees.
- Technologies and abilities: powers, weapons, procedures, devices, systems, scientific ideas.
- Organizations: factions, crews, governments, companies, families, armies, institutions.
- Objects and clues: artifacts, tools, secrets, documents, symbols, motifs.

Use text evidence to decide ambiguous entities. If an item is a ship, facility, organization, or AI system, do not force it into the people model just because it has a name.

## Character Thumbnail Overview

Confirmed rule: use only independent character cards in the overview grid.

Do:

- Show one portrait per person.
- Preserve aspect ratio with `object-fit: cover` or equivalent.
- Place English and Chinese full names in a lower-safe area, below the face, or in a responsive caption block.
- Make each card clickable/tappable.
- Let the grid reflow for desktop, tablet, and mobile.

Do not:

- Keep a large left-side composite collage plus repeated right-side cards.
- Stretch, squash, or distort portraits to fill a fixed box.
- Truncate names on mobile when full names are required.
- Place name blocks over faces.

## Character Relationship Tree

Prefer structured clarity over dense web complexity.

Recommended layout logic:

- Group by faction, institution, family, function, or story arc when possible.
- Put the protagonist or central viewpoint near the top or a clear anchor position when the story calls for it, but do not automatically force the protagonist to the exact center.
- Spread related clusters with enough spacing for relationship labels.
- Keep avatars away from edge labels; relationship text must remain readable.
- Make avatars and labels clickable, not just labels.
- On click/tap, update the detail panel and highlight related people, edges, and relationship descriptions.

Relationship descriptions should be specific enough to be useful, such as `mentor / betrays in act two / shares secret route`, rather than generic `related` labels.

## Technology, Ability, And Concept Timeline

Technology-like entities include powers, weapons, procedures, devices, systems, artifacts, drugs, special skills, scientific concepts, and recurring mechanisms.

Recommended order:

1. Story chronology when clear.
2. First appearance order when chronology is not the main reader problem.
3. Reader-comprehension order when the concept is introduced before it is explained.

Each timeline item should include:

- Name.
- Category.
- First appearance or relevant phase.
- Plain explanation.
- Story function.
- Related characters, places, or conflicts.
- Thumbnail or concept image when available.

## 3D Space Map Rules

The 3D map exists to show spatial relationships that text alone makes hard to imagine.

### Forbidden

- 2D image paste-ins.
- Rounded photo cards.
- Album walls.
- Flat screenshot panels in 3D space.
- Nodes that always face the camera as billboards.
- Static tokens with no model behavior.
- Text-only clickable nodes.

### Required Direction

Use Three.js or an equivalent real-time 3D engine. Build each spatial entity as a miniature scene or holographic landmark:

- Planets: spheres with rotation, atmosphere or rim light, and optional orbit rings.
- Moons/satellites: smaller orbiting bodies with visible paths.
- Ships: simplified 3D hulls with engines, drift, route movement, or light trails.
- Stations/bases: ring systems, platforms, antennae, docks, light arrays.
- Cities/facilities: layered blocks, towers, domes, roads, shafts, or platforms.
- Asteroids/ruins: irregular rock bodies with embedded structures and depth.
- Routes: curved HUD lines or orbital paths that avoid cutting through major models where possible.

Compress scale for readability. Preserve relative near/far relationships, hierarchy, and spatial direction, but do not require literal astronomical distance values.

### Interaction Defaults

- Desktop mouse press-drag: 2D plane pan.
- Trackpad two-finger scroll: rotate/change 3D view direction around the map/grid center, not around whichever node happens to be near the origin.
- Pinch or `Ctrl`/`Meta` + wheel: zoom centered on the current pointer position.
- Mobile/tablet: allow normal page scroll outside intentional gestures. In the 3D region, vertical one-finger swipes should continue scrolling the page; clear horizontal one-finger drags should pan the map; two-finger gestures should support pinch zoom, center movement, and view rotation.
- Touch handlers should not call `preventDefault()` on first contact. Intercept only after a small threshold confirms horizontal map drag, or immediately for two-finger gestures.
- Both the 3D model body and its label must show pointer affordance and open/update detail content.

### Visual Target

A good 3D map feels like a sci-fi strategy map, holographic world atlas, or miniature star-system navigation table. It should show real depth, not a 2D collage.

## Responsive Behavior

Verify three viewport families:

- Desktop: about 1365 x 900 or wider.
- Tablet: about 768 x 1024.
- Mobile: about 390 x 844.

Responsive rules:

- Use adaptive grids with `minmax`, `clamp`, or measured breakpoints.
- Do not scale font purely by viewport width.
- Keep text readable and complete where the user requested full names.
- Keep click targets large enough for touch.
- Do not let graph or 3D interactions prevent basic page scrolling on mobile. Use `touch-action: pan-y` or equivalent mobile CSS where appropriate, then let JavaScript intercept only intentional map gestures.
- Use detail panels that collapse into drawers or stacked sections on small screens.

## Image2 And Thumbnail Binding

When the user requests generated images:

- Treat it as one-to-one object binding when they ask for every person, concept, place, or node to have an image.
- Match images to the extracted data slots, not to vague visual resemblance.
- If using a contact sheet, crop individual tiles into separate assets before binding.
- Verify that no two unrelated entities accidentally share the same thumbnail unless the story explicitly requires it.
- Keep image paths local and stable for the HTML page.

## Template Inheritance

If a user provides a previous successful page, use it as a design and interaction reference:

- Preserve the successful section rhythm, information density, interaction patterns, and visual temperament.
- Replace the content with newly extracted data.
- Apply current StoryVista corrections even if the old page had now-rejected behavior.

## Verification Pattern

For generated HTML, run or perform:

- Script syntax check.
- Missing asset/path check.
- Browser click checks for character cards, character graph nodes, timeline items, and space-map nodes.
- Desktop, tablet, and mobile screenshots.
- Canvas/WebGL nonblank check for 3D maps.
- Check that 3D nodes have volume and do not behave like flat image cards.
- Check that node model bodies, not only labels, are clickable.
- Check map/grid-centered 3D rotation where required.
- Check pointer-centered zoom where required.
- Check that vertical mobile scroll through a 3D section is not trapped, while horizontal drag and two-finger gestures still control the map.
- Check that relationship labels are not hidden by avatars or model icons.

## Deployment And Sync Pattern

When a StoryVista page is meant to be shared:

- Keep a local source copy.
- Sync to the user's requested target such as Obsidian, a static host, or a public repository.
- Prefer static, dependency-light output when the audience will open on mobile browsers.
- If using public hosting, verify the deployed URL on mobile dimensions after upload.

## Final Response Shape

When completing work, report:

- Main file path or URL.
- Sections or rules updated.
- Verification performed.
- Any known limitations or next required user action.
