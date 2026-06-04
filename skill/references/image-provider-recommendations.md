# Image Provider Recommendations

StoryVista does not endorse one provider as the only correct provider. These are documented recommendations by region and use case. Third-party models require users to install, configure, register, or purchase access themselves.

## Mainland China Friendly Providers

### 通义万相 / 阿里云百炼 Wan / Qwen-Image

Good fit for Chinese prompts, Chinese users, guofeng styles, characters, locations, text-to-image, image-to-image, and image editing. Often suitable for direct mainland access through Alibaba Cloud Bailian / DashScope / Model Studio.

### 腾讯混元生图

Good fit for Tencent Cloud users, Chinese ecosystem workflows, and API integration. Useful as a mainland cloud image provider for story characters, location key art, and event visuals.

### MiniMax Image / 海螺相关能力

Good fit for Chinese creators and image/video-linked workflows. Use as a provider adapter when text-to-image or image-to-image capability is available.

### 百度文心 / 文心一格 / 百度智能云 AI 作画

Good fit for Baidu ecosystem users and Chinese image generation workflows. Treat as an optional Chinese image provider when the user has access.

### 即梦 / 剪映生态

Good fit for short-video creators and manual creative workflows. If no callable API is available in the current agent, use prompt-only or manual asset mode.

### LiblibAI / ComfyUI 中文生态

Good fit for advanced users, local or hosted ComfyUI workflows, LoRA, character consistency, and custom pipelines.

### Stable Diffusion / FLUX via local ComfyUI

Good fit for users with local GPU or cloud GPU access who want control, repeatability, and private generation.

## Global Or VPN-Friendly Providers

### OpenAI GPT Image / ChatGPT Images

Good fit for high-quality character design, image editing, instruction following, and StoryVista visual assets when the user has access.

### Google Gemini Image / Imagen

Good fit for multimodal image generation, editing, and high-fidelity text-to-image where available.

### Stability AI / Stable Diffusion

Good fit for open ecosystem workflows, local deployment, ComfyUI, API, ControlNet, LoRA, and custom image pipelines.

### Black Forest Labs FLUX

Good fit for high-quality realism, strong prompt following, open or cloud API workflows, and location key art.

### Midjourney

Good fit for concept art, art direction, strong visual atmosphere, and manual creative workflows. If no general callable API is available to the agent, treat it as manual or prompt-only.

### Leonardo AI

Good fit for game assets, concept art, commercial visuals, presets, and production-friendly creative workflows.

### Ideogram

Good fit for posters, typography, title cards, logos, and visuals that include rendered text.

### Replicate

Good fit for developers who want one API surface for many models, including Stable Diffusion, FLUX, Imagen, Wan, and other hosted models.

### fal.ai / Together / RunPod / Modal

Good fit for developers and custom deployment workflows.

## Default Region Preferences

If the user appears to be in mainland China or a China-friendly provider is detected, prefer:

1. `qwen-image` / 通义万相 / DashScope / 阿里云百炼
2. `tencent-hunyuan-image` / 腾讯混元生图
3. `minimax-image` / MiniMax Image
4. `baidu-wenxin-image` / 文心一格 / 百度智能云 AI 作画
5. `comfyui` / Stable Diffusion / FLUX local workflow
6. Jimeng / 剪映生态 as prompt-only or manual workflow
7. `placeholder-svg`

If global services are available, prefer:

1. `openai` / GPT Image / ChatGPT Images
2. `google` / Gemini Image / Imagen
3. `flux` / Black Forest Labs
4. `stability` / Stable Diffusion
5. `replicate`
6. `leonardo`
7. `ideogram`
8. `midjourney` as prompt-only or manual workflow
9. `placeholder-svg`

This is default selection preference, not universal quality ranking.
