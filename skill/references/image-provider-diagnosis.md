# Image Provider Diagnosis

Image Provider Diagnosis is a best-effort check of the current project and environment. It should never print complete secrets, never make paid API calls by default, and never block StoryVista from continuing.

## Detection Signals

International or global providers:

- `OPENAI_API_KEY`
- `GOOGLE_API_KEY`
- `GEMINI_API_KEY`
- `STABILITY_API_KEY`
- `BFL_API_KEY`
- `REPLICATE_API_TOKEN`
- `LEONARDO_API_KEY`
- `IDEOGRAM_API_KEY`
- `FAL_KEY`
- `TOGETHER_API_KEY`

Mainland China friendly providers:

- `DASHSCOPE_API_KEY`
- `QWEN_API_KEY`
- `ALIBABA_CLOUD_API_KEY_ID`
- `ALIBABA_CLOUD_API_KEY_SECRET`
- `MINIMAX_API_KEY`
- `TENCENTCLOUD_SECRET_ID`
- `TENCENTCLOUD_SECRET_KEY`
- `BAIDU_API_KEY`
- `BAIDU_SECRET_KEY`
- `ZHIPUAI_API_KEY`
- `VOLCENGINE_ACCESS_KEY`
- `VOLCENGINE_SECRET_KEY`

Local services:

- `COMFYUI_API_URL`
- `AUTOMATIC1111_API_URL`
- `SD_WEBUI_API_URL`
- `LOCAL_IMAGE_PROVIDER_URL`

Local image resources:

- `STORYVISTA_IMAGE_ASSETS_DIR`
- `STORYVISTA_MANUAL_ASSETS_DIR`
- `STORYVISTA_IMAGE_MANIFEST_PATH`

## Safe Status Values

Reports should use only:

- `detected`
- `not_found`
- `configured_but_unverified`
- `reachable`
- `unreachable`
- `requires_manual_setup`
- `prompt_only`
- `placeholder_only`

## Secret Handling

Never print full API keys. Mask values, for example `sk-***abcd`.

## Diagnosis Result

Diagnosis should output an `image-provider-report` JSON object with detected providers, scores, risk reasons, selected provider, selected mode, and recommended next steps.
