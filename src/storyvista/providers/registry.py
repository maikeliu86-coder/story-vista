from __future__ import annotations


CAPABILITIES = [
    "character_portrait", "character_half_body", "location_art", "map_art",
    "object_art", "background_art", "image_editing",
]


def provider(
    provider_id: str,
    display_name: str,
    region: str,
    provider_type: str,
    best_for: list[str],
    *,
    requires_api_key: bool = False,
    requires_browser: bool = False,
    supports_direct_generation: bool | str = False,
    env_vars: list[str] | None = None,
    notes: str = "",
) -> dict:
    return {
        "provider_id": provider_id,
        "display_name": display_name,
        "region": region,
        "provider_type": provider_type,
        "capabilities": CAPABILITIES,
        "best_for": best_for,
        "requires_api_key": requires_api_key,
        "requires_browser": requires_browser,
        "supports_direct_generation": supports_direct_generation,
        "supports_prompt_export": True,
        "supports_manual_binding": True,
        "status": "available-as-prompt-workflow" if not supports_direct_generation else "configurable",
        "env_vars": env_vars or [],
        "notes": notes,
    }


PROVIDER_REGISTRY = [
    provider("openai-image", "OpenAI Image", "global", "direct-api", ["natural-language art direction", "image editing"], requires_api_key=True, supports_direct_generation="configurable", env_vars=["OPENAI_API_KEY"]),
    provider("chatgpt-image", "ChatGPT Image", "global", "agent-native", ["conversational iteration", "image editing"], requires_browser=True),
    provider("dall-e", "DALL-E", "global", "direct-api", ["general illustration"], requires_api_key=True, supports_direct_generation="configurable", env_vars=["OPENAI_API_KEY"]),
    provider("google-imagen", "Google Imagen", "global", "direct-api", ["high-fidelity imagery"], requires_api_key=True, supports_direct_generation="configurable", env_vars=["GOOGLE_API_KEY", "VERTEX_API_KEY"]),
    provider("gemini-image", "Gemini Image", "global", "agent-native", ["multimodal iteration"], requires_api_key=True, supports_direct_generation="configurable", env_vars=["GEMINI_API_KEY", "GOOGLE_API_KEY"]),
    provider("stability-ai", "Stability AI", "global", "direct-api", ["configurable diffusion workflows"], requires_api_key=True, supports_direct_generation="configurable", env_vars=["STABILITY_API_KEY"]),
    provider("stable-diffusion", "Stable Diffusion", "global", "local-api", ["local control", "custom models"], supports_direct_generation="configurable"),
    provider("flux", "FLUX", "global", "direct-api", ["photorealism", "typographic composition"], requires_api_key=True, supports_direct_generation="configurable", env_vars=["BFL_API_KEY", "FAL_KEY", "REPLICATE_API_TOKEN"]),
    provider("black-forest-labs", "Black Forest Labs", "global", "direct-api", ["FLUX model access"], requires_api_key=True, supports_direct_generation="configurable", env_vars=["BFL_API_KEY"]),
    provider("replicate", "Replicate", "global", "direct-api", ["hosted open models"], requires_api_key=True, supports_direct_generation="configurable", env_vars=["REPLICATE_API_TOKEN"]),
    provider("fal-ai", "fal.ai", "global", "direct-api", ["fast hosted media models"], requires_api_key=True, supports_direct_generation="configurable", env_vars=["FAL_KEY"]),
    provider("together-ai", "Together AI", "global", "direct-api", ["hosted open models"], requires_api_key=True, supports_direct_generation="configurable", env_vars=["TOGETHER_API_KEY"]),
    provider("runpod", "RunPod", "global", "direct-api", ["custom GPU endpoints"], requires_api_key=True, supports_direct_generation="configurable", env_vars=["RUNPOD_API_KEY"]),
    provider("modal", "Modal", "global", "custom-api", ["custom serverless image pipelines"], requires_api_key=True, supports_direct_generation="configurable", env_vars=["MODAL_TOKEN_ID", "MODAL_TOKEN_SECRET"]),
    provider("custom-api", "Custom Image API", "global", "custom-api", ["bring-your-own endpoint"], requires_api_key=True, supports_direct_generation="configurable", env_vars=["STORYVISTA_IMAGE_API_URL", "STORYVISTA_IMAGE_API_KEY"]),
    provider("comfyui", "ComfyUI", "local", "local-api", ["node workflows", "local model control"], supports_direct_generation="configurable", env_vars=["COMFYUI_URL"]),
    provider("automatic1111", "AUTOMATIC1111", "local", "local-api", ["Stable Diffusion WebUI API"], supports_direct_generation="configurable", env_vars=["AUTOMATIC1111_URL"]),
    provider("sd-webui", "SD WebUI", "local", "local-api", ["local Stable Diffusion"], supports_direct_generation="configurable", env_vars=["SD_WEBUI_URL"]),
    provider("fooocus", "Fooocus", "local", "local-api", ["simple local generation"], supports_direct_generation="configurable", env_vars=["FOOOCUS_URL"]),
    provider("invokeai", "InvokeAI", "local", "local-api", ["local canvas and workflows"], supports_direct_generation="configurable", env_vars=["INVOKEAI_URL"]),
    provider("local-folder", "Local Generated Folder", "local", "manual-assets", ["existing local images"]),
    provider("manual-assets", "Manual Assets", "local", "manual-assets", ["licensed or user-created images"]),
    provider("qwen-image", "Qwen Image", "china-asia", "direct-api", ["Chinese semantics", "bilingual prompts"], requires_api_key=True, supports_direct_generation="configurable", env_vars=["DASHSCOPE_API_KEY"]),
    provider("tongyi-wanxiang", "Tongyi Wanxiang / 通义万相", "china", "direct-api", ["Chinese creative prompts"], requires_api_key=True, supports_direct_generation="configurable", env_vars=["DASHSCOPE_API_KEY"]),
    provider("minimax-image", "MiniMax Image", "china-asia", "direct-api", ["cinematic Chinese prompts"], requires_api_key=True, supports_direct_generation="configurable", env_vars=["MINIMAX_API_KEY"]),
    provider("tencent-hunyuan-image", "Tencent Hunyuan Image", "china", "direct-api", ["Chinese-language imagery"], requires_api_key=True, supports_direct_generation="configurable", env_vars=["TENCENT_SECRET_ID", "TENCENT_SECRET_KEY"]),
    provider("baidu-wenxin-image", "Baidu Wenxin Image", "china", "direct-api", ["Chinese-language imagery"], requires_api_key=True, supports_direct_generation="configurable", env_vars=["BAIDU_API_KEY", "BAIDU_SECRET_KEY"]),
    provider("volcengine-seedream", "Volcengine Seedream / 火山引擎 Seedream", "china-asia", "direct-api", ["high-fidelity cinematic imagery", "Chinese prompts"], requires_api_key=True, supports_direct_generation="configurable", env_vars=["VOLCENGINE_API_KEY", "VOLCENGINE_ACCESS_KEY", "VOLCENGINE_SECRET_KEY", "SEEDREAM_API_KEY", "BYTEDANCE_SEEDREAM_API_KEY"], notes="Configuration detection does not verify API availability."),
    provider("bytedance-seedream", "ByteDance Seedream / SeeDream", "china-asia", "custom-api", ["high-fidelity cinematic imagery", "character consistency"], requires_api_key=True, supports_direct_generation="configurable", env_vars=["SEEDREAM_API_KEY", "BYTEDANCE_SEEDREAM_API_KEY"], notes="Falls back to prompt export when no user API configuration is present."),
    provider("jimeng", "Jimeng / 即梦", "china", "manual-web", ["stylized cinematic images", "Chinese-language prompts", "short-video-friendly visuals"], requires_browser=True, notes="Copy exported prompts into the Jimeng web workflow, then bind downloaded images."),
    provider("jianying-jimeng", "Jianying Jimeng / 剪映即梦", "china", "manual-web", ["mainland creator workflows", "short-video-friendly visuals"], requires_browser=True),
    provider("liblibai", "LiblibAI", "china", "manual-web", ["community models", "Chinese creator workflows"], requires_browser=True),
    provider("runninghub", "RunningHub", "china-asia", "manual-web", ["hosted ComfyUI workflows"], requires_browser=True),
    provider("siliconflow", "SiliconFlow", "china-asia", "direct-api", ["hosted open image models"], requires_api_key=True, supports_direct_generation="configurable", env_vars=["SILICONFLOW_API_KEY"]),
    provider("modelscope", "ModelScope", "china-asia", "manual-web", ["open model discovery and demos"], requires_browser=True),
    provider("midjourney", "Midjourney", "global", "prompt-only", ["stylized cinematic imagery", "concept art"], requires_browser=True),
    provider("ideogram", "Ideogram", "global", "manual-web", ["graphic design", "text-aware images"], requires_browser=True),
    provider("leonardo", "Leonardo AI", "global", "manual-web", ["game assets", "concept art"], requires_browser=True),
    provider("canva", "Canva", "global", "manual-web", ["design layouts", "social assets"], requires_browser=True),
    provider("adobe-firefly", "Adobe Firefly", "global", "manual-web", ["commercial creative workflows"], requires_browser=True),
    provider("krea", "Krea", "global", "manual-web", ["rapid visual iteration"], requires_browser=True),
    provider("playground", "Playground", "global", "manual-web", ["web-based image iteration"], requires_browser=True),
    provider("prompt-pack", "Prompt Pack", "global", "fallback", ["external generation handoff"]),
    provider("placeholder-svg", "Semantic Placeholder SVG", "local", "fallback", ["offline visual fallback"]),
]


def get_provider(provider_id: str) -> dict | None:
    return next((item for item in PROVIDER_REGISTRY if item["provider_id"] == provider_id), None)
