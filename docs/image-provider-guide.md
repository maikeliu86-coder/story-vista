# Image Provider Guide

StoryVista does not require one fixed image generator. It works as a provider-neutral reading and binding workflow.

## Non-Negotiable Rule

If the current agent has no usable image model, do not generate blank placeholder success states and do not pretend that images already exist. Export copy-ready prompts and a structured image generation task list instead.

When no model is callable, the correct user-facing message is explicit: no usable image model was detected in the current agent environment. The next step is to choose Image2, SeeDream, ComfyUI, Flux, SDXL, or another cloud/local model, then run generation or copy the prompts manually.

## Forbidden Missing-Provider Behavior

- Do not generate blank placeholders as final output.
- Do not insert nonexistent image links.
- Do not pretend images were generated.
- Do not use broken image URLs.
- Do not use "image generation in progress" instead of a real result.
- Do not output decorative placeholders that cannot help the user generate real images.

## Image2

### Best For

- agents with built-in image generation
- fast in-session iteration
- simple prompt-to-image workflows

### Notes

Use when the current agent can directly generate images and save them back into the project workflow.

## SeeDream

### Best For

- users comfortable with external cloud workflows
- Chinese prompt-oriented generation
- manual download and later binding

### Notes

StoryVista should export provider-specific prompts and expected filenames, then bind the downloaded files later.

## ComfyUI

### Best For

- local generation
- advanced node-based workflows
- users who want routing control across multiple open models

### Notes

ComfyUI is powerful but operationally heavier. StoryVista should treat it as a local provider only when the service is really running and reachable.

## Flux

### Best For

- local or hosted open-model image generation
- high prompt fidelity
- strong realism or stylized realism

### Notes

Flux is a good option when the user wants a modern open-model stack without being tied to one commercial cloud interface.

## SDXL

### Best For

- large community ecosystem
- many checkpoints and LoRA workflows
- users already familiar with local model tooling

### Notes

SDXL remains a practical choice when compatibility and checkpoint variety matter more than a single curated model family.

## Other Cloud Or Local Models

StoryVista can also work with:

- other hosted API-based image services
- web-based generation tools
- custom local inference pipelines
- studio-specific internal tools

The requirement is not the brand name. The requirement is that the workflow can produce real image files that StoryVista can bind back into the atlas.

## When To Use Which Path

1. Use the model explicitly chosen by the user.
2. Use `Image2` when the current agent can call it directly.
3. Recommend `SeeDream` when the user is on a mainland-accessible cloud workflow and SeeDream is available.
4. Use local `ComfyUI`, `Flux`, or `SDXL` when the user has them running.
5. Use another cloud or local model if it can produce real files for binding.
6. Output a structured task list when no model is callable.

## Minimum Safe Fallback

When no provider is available, StoryVista should still produce:

- per-asset prompt text
- negative prompt text
- expected filenames
- provider recommendation notes
- a structured generation task list

This is the correct fallback. A blank image slot is not a successful generation result.

## Image Generation Task List

| ID | Type | Title | Source Basis | Prompt | Negative Prompt | Recommended Provider | Aspect Ratio | Priority |
|---|---|---|---|---|---|---|---|---|
| image_001 | location | First major location key art | Current reading section and extracted location evidence | Copy-ready environment prompt with architecture, light, camera, mood, and spoiler-safe visual details | later-story symbols, unread characters, text, watermark, distorted geometry | SeeDream / Flux / SDXL | 16:9 | high |
