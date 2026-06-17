# StoryVista Product Experience Contract

StoryVista is not primarily a test harness, README package, provider workflow, or engineering template. Those systems are useful only if they support the final reader-facing atlas.

## Product Goal

StoryVista turns complex novels, scripts, and worldbuilding texts into immersive visual reading atlases.

The first opened page should feel like:

- a game codex
- a world setting archive
- a film or animation concept dossier
- an interactive reader companion

It should not feel like:

- an engineering report
- a provider diagnostic page
- a spreadsheet export
- a generic documentation template

## Core Experience Principles

1. Visual archive first.
   The user should immediately see a story world: characters, places, factions, objects, lore, relationships, events, maps, and timelines.

2. Reader orientation before developer orientation.
   Build status, provider fallback, validation, prompts, and schema information must be secondary.

3. Card-based browsing.
   Characters, locations, objects, factions, lore, events, and technologies should be shown as visual dossiers, not plain rows.

4. Category separation.
   Characters, places, vehicles, factions, objects, technologies, and concepts must not collapse into one generic entity surface.

5. Immersive but evidence-aware.
   The atlas may use atmosphere, composition, and visual hierarchy, but must not invent unsupported story facts or spoil later content.

6. Fallbacks should not dominate the page.
   Missing image providers should result in useful prompt tasks and tasteful semantic fallbacks. The final page should still feel browseable.

7. Engineering serves experience.
   Tests, schemas, docs, provider registries, and workflow files exist to protect the product experience, not to replace it.

## Required Final Atlas Qualities

A good StoryVista atlas should include:

- a strong story title and world-framing hero
- visual roster for major characters
- character cards with role, faction, arc, evidence, and image slot
- relationship field or graph before raw relationship lists
- location or world map surface
- object / lore / technology card grid
- timeline or phase view
- reader panel and source evidence access
- spoiler-safe states that hide unrevealed information
- prompt access for pending images without turning the whole page into a prompt report

## Engineering Capabilities To Preserve

The following newer capabilities remain valuable:

- provider preflight and provider selection
- prompt pack export
- external generation and image binding
- semantic display fallbacks
- source evidence and Reader Sync
- language detection and localized interface labels
- validation reports and tests
- docs and agent compatibility notes

These capabilities must stay below the user-facing story experience in the page hierarchy.

## Drift Warning Signs

StoryVista is drifting away from its product goal if:

- the first screen is mostly diagnostics
- the page has many empty tables but little visual browsing
- provider state dominates over story content
- tests pass while characters, locations, relationships, or lore are empty
- examples are only Markdown tables
- the atlas feels like an admin tool instead of a story archive

## Design Reference

Use `docs/golden-reference.md` as the experience baseline. Do not copy its exact story data, but inherit its successful rhythm:

- cinematic dark archive
- cyan/gold signal language
- terminal panels
- visual character roster
- relationship-first interaction
- timeline and map surfaces
- dense but readable cards

