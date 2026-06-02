# Implementation Notes

## Lessons From The Accepted Archive

The accepted pattern came from an Obsidian plus CloudBase static HTML archive for a science-fiction novel. These are reusable decisions for future scripts.

## File Surfaces To Maintain

- Canonical Obsidian HTML page: the page the user opens inside the vault.
- Public copy: the static HTML deployed to a public host.
- Source record note: a Markdown note that links source material, local HTML, and public sharing URL.
- Asset inputs: user-provided grids or Image2 outputs for characters, technologies, locations, ships, and concepts.

Always search for all relevant copies before editing:

```bash
rg -n "public-url-fragment|story-title|spacePos3D|source record" <vault-or-project>
```

## Character And Entity Extraction

Create data records with stable ids. Use separate collections for:

- `characters`
- `technologies`
- `places`
- `ships`
- `relationships`
- `spaceLinks`

Do not mix category types. Proper names can be misleading: a named ship belongs in ships/places/space maps, not in the character tree.

For each character, include:

- Chinese display name
- English or transliterated name when known
- role/faction
- first appearance or timeline position
- concise introduction
- relationships with specific labels
- image assignment

For technologies and special abilities, preserve story order. Include the chapter/scene, what it does, who uses it, and why it matters.

For places and ships, include:

- type
- chapter/scene span
- description
- events
- routes or links
- image or 3D model mapping

## Image2 And Thumbnail Binding

When the user provides composite image grids:

1. Inspect the grid dimensions and cell order.
2. Slice or CSS-crop cells consistently.
3. Match each cell by story evidence and visual clues.
4. Bind every thumbnail and detail image to the corresponding data record.
5. Search for duplicates and category mistakes.

The user expects "generate and place", not a mood board. A generated picture is incomplete until it is bound into the HTML slot that uses it.

## Interaction Patterns That Worked

Character overview:

- Use a grid of portraits.
- Put the English and Chinese names near the lower-left or bottom area.
- On mobile, show full names without covering faces. Use a gradient label strip under or near the lower edge, not over eyes or central face details.

Character relationship tree:

- Clicking a person updates a right-side detail panel.
- Layout can be scattered rather than a dense net. Main character may sit above center or upper region, with others spread around.
- Relationship labels need collision handling or offset logic so avatars/nodes do not cover them.

Technology timeline:

- Use chronological cards or bands.
- Each technology/ability should have a thumbnail, story context, and significance.

Space map:

- Use a real-time 3D canvas when the user asks for spatial depth.
- Click or tap a planet/place/ship node to update details.
- Include a short HUD explaining gestures.

## 3D Space Map Rules

Avoid fake 3D:

- no rectangular image cards
- no rounded photo frames
- no 2D image wall
- no screenshot pasted into the scene

Model each node as geometry:

- planets: spheres, orbit rings, moons, atmosphere glow
- cities: base plate, tower clusters, domes, light columns
- stations: torus rings, hubs, spokes, docking pads, antennas
- asteroid fields: irregular rocks, facilities, debris, orbit lines
- ships: bodies, noses, fins, engine glow, route trails
- hospitals/factories: shafts, pods, robotic arms, underground rings

For "true proportion" requests, use compressed scale:

- Keep relative story order and distance hierarchy.
- Cluster near-ground or near-planet scenes around their parent planet.
- Put moon/near orbit beyond the planet cluster.
- Place Mars/intermediate regions farther away.
- Place asteroid belt/ship wrecks between Mars and Jupiter.
- Place Jupiter and its moons at the farthest layer.
- Add different `x`, `y`, and `z` values so rotation reveals depth.
- Add faint scale rings, coordinate grids, vertical depth guides, and curved route lines.

Example coordinate strategy:

```js
const spacePos3D = {
  earth: [0, 35, 0],
  outerOrbit: [8, 210, -126],
  moon: [-178, 82, 48],
  earthCityA: [82, -54, 112],
  earthCityB: [-96, -42, -98],
  mars: [430, 142, -362],
  asteroidBelt: [740, 12, -204],
  shipWreck: [825, -44, -72],
  jupiter: [1195, 118, 252],
  outerMoonRoute: [1370, 16, 392]
};
```

Tune camera target to the center of the compressed system, not to Earth only.

## Verification Pattern

For single-file HTML:

```bash
node <<'NODE'
const fs = require('fs'), vm = require('vm');
const html = fs.readFileSync('index.html', 'utf8');
for (const [i, m] of [...html.matchAll(/<script[^>]*>([\s\S]*?)<\/script>/g)].entries()) {
  new vm.Script(m[1], { filename: `index.html:script${i}` });
}
console.log('script ok');
NODE
```

Then serve locally:

```bash
python3 -m http.server 8765
```

Validate:

- page identity and title
- canvas exists for 3D maps
- no stale static image layer if real-time 3D is expected
- labels render
- click a character and a place/ship node
- inspect desktop and mobile screenshots

Stop the local server after testing:

```bash
lsof -ti tcp:8765 | xargs -r kill
```

## Deployment And Sync Pattern

For CloudBase-style static hosting:

```bash
npx tcb hosting deploy '<public-copy>/index.html' index.html -e <environment-id>
npx tcb hosting list index.html -e <environment-id>
```

Use cache-busting URLs after deploy:

```text
https://example.tcloudbaseapp.com/index.html?v=<short-version>#space
```

Update the Obsidian source record with the current public URL. This matters because friends opening old links may see CDN cache.

## Final Response Shape

When done, report:

- what was changed
- which local files were updated
- which public URL was deployed
- what was verified
- any cache note or remaining limitation
