# FAQ

## StoryVista 是什么？

StoryVista is a visual reading companion that turns novels, scripts, and lore-heavy texts into a spoiler-safe atlas of characters, locations, relationships, objects, factions, and events.

## 为什么没有生成图片？

Usually because the current agent does not have a callable image model, the provider is unverified, the key is missing, the model is rate-limited, or local generation is offline. StoryVista should still export prompts and a structured generation task list.

## 为什么只有 placeholder？

Placeholders are display fallbacks. They mean the atlas structure exists, but real images have not been generated and bound yet.

## 如何切换图像模型？

Choose a different provider during prompt export or provider setup. For example, export prompts for `jimeng` or `seedream`, or use a local ComfyUI, Flux, or SDXL workflow. The atlas data can stay the same while the image provider changes.

## 如何避免剧透？

Limit the source text to the current reading boundary, tell StoryVista the current progress, and explicitly ask for spoiler-safe extraction. Do not feed later chapters if the reader should not see them yet.

## 如何处理长篇小说？

It works best when long texts are chunked and processed incrementally. For very long books, use chapter-based or progress-based passes, then rebuild the atlas over time instead of forcing one huge all-at-once extraction.

## 支持中文小说吗？

Yes. Chinese input and Chinese UI are supported. StoryVista can work with Chinese names, locations, objects, and relationship structures.

## 支持英文小说吗？

Yes. English is a first-class workflow and several demos are already English-based.

## 支持本地模型吗？

Yes, when a local workflow exists. ComfyUI, Flux, SDXL, and similar local or self-hosted setups can be used as external generation backends.

## 支持 Codex / Claude Code / Trae / Marvis 吗？

Yes, as orchestration layers. StoryVista's stable contract is the local CLI plus generated files. Compatibility depends on whether the tool can read files and run commands.

## Image2、SeeDream、ComfyUI、Flux、SDXL 有什么区别？

- `Image2`: best when the current agent already has integrated image generation.
- `SeeDream`: cloud-oriented workflow with exported prompts and later binding.
- `ComfyUI`: local graph-based workflow with high control.
- `Flux`: modern open-model family with strong prompt following and realism.
- `SDXL`: broad ecosystem with many checkpoints and community workflows.

## 如果当前 Agent 没有可用生图模型，会发生什么？

StoryVista should not output blank success states. It should generate copy-ready prompts, expected filenames, and a structured image generation task list that can be used in another model.

## Can I Keep The Atlas Textual And Skip Images?

Yes. StoryVista still provides value as a structured reading atlas even without image generation.
