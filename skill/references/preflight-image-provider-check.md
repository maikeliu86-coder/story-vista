# Preflight Image Provider Check

The Preflight Image Provider Check is a short, non-blocking check before StoryVista creates visual assets. It helps the user understand which image provider will generate, plan, or placeholder character portraits, location key art, concept images, and event visuals.

This check is not an error and not a blame message. It separates StoryVista generation status from image provider status: StoryVista can still parse the story, create a visual asset plan, generate prompts, create `image-manifest.json`, bind placeholders, and build the atlas even when no callable image provider is available.

Do not hardcode this as a popup. Different agents support different interaction surfaces: console output, chat confirmation, project notes, report JSON, settings panels, or silent auto mode.

## Chinese Preflight Message

在开始生成故事视觉页面前，建议先检查当前配置的生图引擎。StoryVista 会根据你的当前 image provider 生成人物、地点和关键事件的视觉资产。如果当前没有可调用的生图引擎，StoryVista 仍会生成完整提示词、图片清单和语义占位图，方便你后续补图或切换模型后重新生成。

如果你不确定该选哪个生图引擎，可以直接使用 Auto Mode。StoryVista 会根据当前环境自动选择一个推荐 image provider。

选择项：

- 使用 Auto Mode，继续生成
- 检查当前生图配置
- 手动选择生图引擎

## English Preflight Message

Before generating the visual story atlas, StoryVista recommends checking your current image provider. Character portraits, location key art, and event visuals will be generated or planned based on the selected provider. If no callable image provider is available, StoryVista will still create full image prompts, an image manifest, and semantic placeholders for later replacement or regeneration.

If you are not sure which image provider to use, keep Auto Mode enabled. StoryVista will select a recommended provider based on the current environment.

Options:

- Use Auto Mode and continue
- Run image provider diagnosis
- Manually select image provider

## Behavior

- Preflight does not block story parsing.
- Diagnosis does not block final atlas generation.
- Missing provider is not fatal.
- Continue with `prompt-only` or `placeholder-svg` when needed.
- Never silently fall back to initials-only avatars.
- Record selected mode and provider state in the final report.
