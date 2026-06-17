# Troubleshooting

## Images Were Not Generated

### Possible Causes

- no working image provider is available
- provider detection found signals but not a verified runtime
- the current agent cannot call image generation

### How To Check

- run `python scripts/detect_image_provider.py --no-network`
- inspect `image-provider-report.json` or related preflight output if present
- confirm whether the current agent can actually generate images

### How To Fix

- use a verified provider
- export prompts instead of forcing generation
- switch to a manual binding workflow if generation must happen elsewhere
- output an `Image Generation Task List` with prompt, negative prompt, recommended provider, aspect ratio, and priority

Do not treat blank placeholders, broken links, or "generation in progress" labels as successful image output.

## I Only See Placeholders

### Possible Causes

- no real images were bound
- the atlas was built before image generation finished
- files were saved under the wrong names

### How To Check

- inspect `image-manifest.json`
- check whether generated files exist under `output/demo/assets/generated/`
- compare filenames against the expected manifest names

### How To Fix

- generate the missing images
- save them with the expected filenames
- run `python scripts/storyvista.py bind-images output/demo --assets output/demo/assets/generated`
- if no generator is available, use the task list to generate images in Image2, SeeDream, ComfyUI, Flux, SDXL, or another model first

## The Agent Cannot Find Any Image Model

### Possible Causes

- no provider is configured
- keys are missing
- local services are not running
- the agent runtime has no image capability

### How To Check

- run provider detection
- inspect environment variables
- confirm local endpoints and ports
- verify output directory permissions
- check whether the provider is rate-limited
- ask whether the user wants text-first atlas generation before batch images

### How To Fix

- configure a provider properly
- start the local service if using ComfyUI or similar
- fall back to prompt export plus a structured generation task list
- clearly tell the user no usable image model is currently detected

## API Key Is Missing

### Possible Causes

- the required environment variable was never set
- the shell session does not expose it
- the wrong provider key is present

### How To Check

- inspect your environment configuration
- confirm the key name expected by the chosen provider
- rerun provider detection

### How To Fix

- set the correct key in the environment used by the agent
- restart the agent session if needed
- avoid paid generation calls until the configuration is verified

## The Model Is Rate-Limited

### Possible Causes

- provider-side quota limits
- concurrency limits
- exhausted paid credits

### How To Check

- inspect provider error messages
- retry with a small batch
- compare behavior across different providers

### How To Fix

- wait and retry later
- reduce batch size
- switch providers
- export prompts and continue in manual mode

## The Local Model Is Not Running

### Possible Causes

- ComfyUI or another local service was never started
- the service crashed
- the port changed

### How To Check

- open the local service UI if it has one
- verify the expected port is listening
- inspect local service logs

### How To Fix

- restart the local service
- correct the configured endpoint
- keep StoryVista in prompt-only mode until the service is healthy

## README Images Do Not Display

### Possible Causes

- wrong relative path
- image file missing
- the branch has not been pushed
- GitHub has not refreshed the rendered page yet

### How To Check

- confirm the file exists in the repository
- check the README path
- inspect the raw GitHub README and image path directly

### How To Fix

- correct the relative path
- commit and push the missing asset
- refresh GitHub after the push completes

## GitHub Badges Do Not Display

### Possible Causes

- shields.io temporary issue
- repository path typo
- release badge added without a matching release

### How To Check

- open the badge URL directly
- confirm the repository owner and name
- check whether the referenced release really exists

### How To Fix

- correct the badge URL
- remove badges that do not have real backing data
- wait if the badge service is temporarily unavailable

## Documentation Links Are Broken

### Possible Causes

- README links point to files that do not exist
- files were renamed without updating links
- case-sensitive path mismatch

### How To Check

- run a local link existence check
- inspect the exact file paths in the repository

### How To Fix

- create the missing file
- update README or docs links to match the real path
- keep names stable once they are public

## Broken Image URLs Were Inserted

### Possible Causes

- image files were referenced before they existed
- a generated image path was copied from a temporary location
- the atlas or README was edited manually without committing assets

### How To Check

- open each image path from the repository root
- inspect `image-manifest.json`
- verify the file is committed or present in the output directory

### How To Fix

- remove broken URLs
- bind real generated files before referencing them
- use task-list prompts instead of fake image links when no provider is callable

## The Agent Says Images Are Still Generating

### Possible Causes

- the agent used a progress label as a final result
- provider generation failed or timed out
- no output file was produced

### How To Check

- inspect the output directory for real image files
- check provider logs or API responses
- confirm whether generation actually completed

### How To Fix

- report the failed or pending state clearly
- retry with a smaller batch if the provider is available
- output an `Image Generation Task List` if generation cannot be completed now

## The Output Contains Spoilers

### Possible Causes

- the input included later chapters
- the prompt did not specify spoiler-safe boundaries
- manual edits introduced out-of-scope knowledge

### How To Check

- inspect the input text used for the build
- compare the atlas content against the allowed reading boundary
- review prompts and intermediate notes

### How To Fix

- rerun using only the allowed reading scope
- explicitly request spoiler-safe extraction
- remove future-only entities and rebuild the atlas
