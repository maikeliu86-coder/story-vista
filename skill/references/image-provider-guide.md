# Image Provider Guide

StoryVista is image-provider neutral. It defines required visual assets and bindings, then lets the user or host agent choose how images are generated or supplied.

## Provider Modes

- `openai`
- `chatgpt-image`
- `google`
- `gemini-image`
- `imagen`
- `midjourney`
- `stable-diffusion`
- `stability`
- `flux`
- `comfyui`
- `automatic1111`
- `minimax-image`
- `qwen-image`
- `tencent-hunyuan-image`
- `baidu-wenxin-image`
- `zhipu-image`
- `volcengine-seedream`
- `ideogram`
- `leonardo`
- `replicate`
- `fal`
- `together`
- `local-folder`
- `manual-assets`
- `placeholder-svg`
- `custom-api`

## Core Rule

The core skill should create model-neutral asset requirements first. Provider-specific syntax belongs in adapters, configuration, or downstream scripts.

StoryVista defaults to Auto Mode. The system should detect configuration signals, score candidates, select a recommended provider when possible, and explain the selection in plain language. Beginners should not be forced to pick from a long provider list.

## Required Outputs

When visual output is requested, produce:

- `visual-asset-plan.json`
- provider-neutral image prompts
- optional provider-specific prompt variants
- `image-manifest.json`
- generated, user-provided, planned, placeholder, missing, or failed status for each asset

## BYO Image Model

When the user uses Midjourney, Flux, Stable Diffusion, ComfyUI, MiniMax, Jimeng, Qwen Image, Tencent Hunyuan Image, Baidu Wenxin Image, OpenAI image models, or another tool outside the agent, keep manifest entries at `status: "prompt_ready"` until files are returned.

## Manual Assets

When a user provides images, mark them as `status: "user_provided"` and preserve the supplied file path. Do not rename files unless the user asks or the output workflow requires stable local copies.

## Placeholder SVG

When no provider is available, generate semantic placeholders. Include the full entity name, entity type, and asset type. Do not use initials-only avatars by default.

## Failure Handling

If a provider fails:

1. Keep the failed entry in the manifest with `status: "failed"`.
2. Preserve the prompt and negative prompt.
3. Create or reference a semantic placeholder.
4. Report the failure in the final asset status summary.

## Preflight And Diagnosis

Before visual asset generation, run or offer Image Provider Diagnosis. Detection may inspect config files, environment variables, local endpoints, manual asset folders, and existing manifests. Do not print full API keys. Do not make paid API calls by default.

If no provider is detected, continue with full prompts, `image-manifest.json`, and semantic placeholders. This is a valid continuation mode, not a StoryVista failure.

Detection and verification are separate. A masked API key or configured endpoint can make a provider a good recommendation candidate, but mark it unverified until a safe verification step succeeds. Keep StoryVista generation status separate from image provider status in reports and generated atlas notes.
