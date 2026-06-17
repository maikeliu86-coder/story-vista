# StoryVista Skill

This is the root entry point for the StoryVista skill documentation.

- Canonical skill file: [skill/SKILL.md](skill/SKILL.md)
- Core workflow references: [skill/references/](skill/references/)
- Provider registry: [docs/image-provider-registry.md](docs/image-provider-registry.md)
- External image workflow: [docs/external-image-generation.md](docs/external-image-generation.md)
- Provider workflow: [docs/provider-workflow.md](docs/provider-workflow.md)
- Image provider guide: [docs/image-provider-guide.md](docs/image-provider-guide.md)

Install or inspect the `skill/` directory when using StoryVista as an agent skill.

## Core Execution Rules

StoryVista must build a useful, spoiler-safe visual reading workflow from the user's source text. It should not invent story facts, future plot events, visual traits, or relationships that are not supported by the current reading scope.

## Product Experience Rules

StoryVista's final output should feel like an immersive visual reading atlas, not an engineering report. The page should lead with story-world browsing: character roster, relationship field, location/map surface, object and lore cards, event timeline, and reader evidence. Provider state, fallback status, validation details, and prompt workflow controls must remain available but secondary.

Use [docs/product-experience-contract.md](docs/product-experience-contract.md) and [docs/golden-reference.md](docs/golden-reference.md) as the product direction. Engineering features should protect the atlas experience, not dominate it.

## Spoiler Rules

- Default to spoiler-safe mode.
- Use only the source text inside the user's current reading progress.
- Do not reveal later events in summaries, portraits, image prompts, alt text, relationship labels, or location notes.
- Mark future-only or uncertain information as locked, unresolved, or omitted.
- Full-spoiler output requires explicit user approval.

## Source Basis Rules

Every important claim should be traceable to source text or clearly marked as inferred, ambiguous, contradictory, unresolved, or unknown. Visual prompts should include a `Source Basis` note so the user can see why a character, place, object, or worldbuilding detail was generated.

## Extraction Rules

StoryVista should extract and separate:

- characters, aliases, titles, roles, factions, and relationship changes
- locations, routes, rooms, cities, facilities, planets, and recurring places
- objects, weapons, technologies, powers, magic, medicine, clues, and artifacts
- organizations, families, armies, institutions, factions, and alliances
- events, timeline beats, scene transitions, and reader-progress boundaries
- worldbuilding concepts, rules, motifs, and unresolved mysteries

Ships, locations, and objects should not be placed in the character relationship tree unless the source treats them as characters.

## Image Model Detection Rules

Before generating visual content, StoryVista should confirm or detect:

- whether the current agent can call an image model
- whether an API key is present when required
- whether local services such as ComfyUI are running
- whether the output directory is writable
- whether rate limits or paid calls may be triggered
- whether the user wants a text-first atlas before batch image generation

## Image Generation Execution Rules

StoryVista is a visual reading workflow, not a placeholder-template generator. It must prioritize usable results:

- generate real images when a verified image model is callable
- output high-quality prompts when direct generation is unavailable
- explain why generation cannot run when no model is available
- never invent that images were generated
- never treat image-link placeholders as completion

When no usable image model is detected, the agent must tell the user clearly and provide an `Image Generation Task List` instead of blank or broken visuals.

Recommended fallback order:

1. Use the user's explicitly selected model.
2. Use Image2 if the current agent can call it directly.
3. Recommend SeeDream when the user is in a mainland-accessible cloud workflow and SeeDream is available.
4. Use local ComfyUI, Flux, or SDXL when the user has them running.
5. Use another cloud or local model that can produce real files for binding.
6. Output the structured task list when no model is callable.

Forbidden behavior:

- generating blank placeholder images as final output
- inserting image links that do not exist
- pretending images have already been generated
- using broken image URLs
- using "image generation in progress" as a substitute for a real result
- outputting decorative placeholders with no practical generation value

## Image Generation Task List

| ID | Type | Title | Source Basis | Prompt | Negative Prompt | Recommended Provider | Aspect Ratio | Priority |
|---|---|---|---|---|---|---|---|---|
| image_001 | character/location/object/event | Short asset title | Source paragraph, scene, or evidence note | Copy-ready visual prompt | Exclusions and spoiler limits | Image2 / SeeDream / ComfyUI / Flux / SDXL / other | 16:9 / 4:5 / 1:1 | high/medium/low |
