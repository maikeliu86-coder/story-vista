# Provider Workflow

StoryVista uses a provider-neutral image workflow. The atlas build does not depend on one fixed image model, and the image step should never block text extraction, entity modeling, or atlas rendering.

## Core Rule

If a working image model is available, StoryVista can generate or bind real images.

If no working image model is available, StoryVista must:

- clearly tell the user that no usable image model was detected
- keep the atlas build moving
- export prompts and a structured task list
- preserve placeholder display only as a fallback surface
- avoid pretending that image generation already succeeded

StoryVista is a visual reading workflow, not a template that stops at placeholders.

## Forbidden Missing-Provider Behavior

When the current agent has no callable image model, it must not:

- generate blank placeholders as final image output
- insert image links that do not exist
- pretend images have already been generated
- use broken image URLs
- use "image generation in progress" as a substitute for real images
- output placeholders with no practical prompt or binding path

## Standard Pipeline

1. Build the atlas from source text.
2. Run provider preflight or inspect known environment signals.
3. Choose a provider or decide on prompt-only mode.
4. Export prompts.
5. Generate images externally or through a configured runtime.
6. Save images with expected filenames.
7. Bind the images back into the atlas.
8. Rebuild or validate the final output.

## Model Detection Prompt

Before generating visual content, the agent should confirm or detect:

- whether the current agent has a usable image model
- whether an API key is present when the selected provider requires one
- whether a local service such as ComfyUI is running
- whether the output directory is writable
- whether the request may hit provider rate limits
- whether the user wants a text atlas first and batch image generation later

## Base Commands

```bash
python scripts/storyvista.py build input.txt --out output/demo
python scripts/detect_image_provider.py --no-network
python scripts/storyvista.py export-prompts output/demo --provider jimeng
python scripts/storyvista.py bind-images output/demo --assets output/demo/assets/generated
python scripts/storyvista.py rebuild-atlas output/demo
python scripts/storyvista.py validate output/demo
```

## Provider Selection Logic

Use these rules in order:

1. If the user explicitly specifies a model, prioritize that model.
2. If the current agent can directly call Image2, use Image2.
3. If the user is on a mainland-accessible platform and SeeDream is available, recommend SeeDream.
4. If the user has local ComfyUI, Flux, or SDXL running, prioritize the local model.
5. If no model is available, output an image generation task list.
6. If detection is uncertain, mark it as detected but unverified.
7. Never treat `placeholder-svg` as a working image provider.
8. Never treat an API key alone as proof that generation is available.

## Recommended Provider Paths

### Image2

Use when the current agent can directly call a working image model. This is the simplest user experience because prompt export, generation, and follow-up edits can stay in one agent session.

### SeeDream

Use when the user prefers a cloud workflow and can manually copy prompts into a web or API interface. StoryVista should export provider-specific prompts and expected filenames.

### ComfyUI

Use when the user wants local control, reusable node graphs, or a self-hosted workflow. StoryVista should provide structured prompt outputs and asset naming guidance, then bind the generated files afterward.

### Flux And SDXL

Use when the user has access to local or hosted open-model infrastructure. These are strong choices for advanced users who want checkpoint choice, local privacy, or lower cloud dependency.

## Prompt-Only Mode

Prompt-only mode is the correct fallback when:

- no image model is callable
- keys are missing
- a provider is rate-limited
- the user wants to review prompts before generation
- the environment should avoid paid or external calls

In prompt-only mode, StoryVista should output:

- provider recommendation
- provider risk notes
- copy-ready prompts
- per-asset generation tasks
- expected filenames for later binding

## Image Generation Task List

When a provider is unavailable, each generation task should clearly state:

- `image_id`
- `title`
- `purpose`
- `source basis` / `依据文本`
- `visual prompt`
- `negative prompt`
- `recommended model`
- `aspect ratio`
- `priority`

This gives the user something operational instead of a dead-end placeholder state.

| ID | Type | Title | Source Basis | Prompt | Negative Prompt | Recommended Provider | Aspect Ratio | Priority |
|---|---|---|---|---|---|---|---|---|
| image_001 | character | Protagonist portrait | Chapter 1 description and current reading evidence only | Copy-ready portrait prompt with clothing, mood, lighting, and spoiler-safe traits | future plot reveals, extra characters, unread symbols, text, watermark | Image2 / SeeDream / ComfyUI / Flux / SDXL | 4:5 | high |

## Common Scenarios

### Scenario 1: Agent Has Image2

- Build atlas
- Generate images in-agent
- Save results to the expected asset paths
- Bind and rebuild

### Scenario 2: Agent Has No Image Model

- Build atlas
- Export prompts
- Tell the user no usable image model was detected
- Output structured generation tasks in the standard table format
- Let the user generate elsewhere
- Bind images later

### Scenario 3: Local ComfyUI Exists But Is Offline

- Report that ComfyUI was expected but not reachable
- Keep the atlas build successful
- Export tasks for later retry

## Related Docs

- [Image Provider Guide](image-provider-guide.md)
- [External Image Generation](external-image-generation.md)
- [Image Provider Registry](image-provider-registry.md)
- [Jimeng And Seedream Workflow](jimeng-seedream-workflow.md)
- [Manual Image Binding](manual-image-binding.md)
- [Troubleshooting](troubleshooting.md)
