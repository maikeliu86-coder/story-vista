# LlamaIndex Adapter

Invocation: use readers/indexes for evidence retrieval, then emit the portable StoryVista artifacts or call the CLI directly.

Capabilities: source retrieval and artifact storage are expected; image tools are optional.

Limit: cited chunks must map back to StoryVista `source_id` and `chunk_id` values.

Mode: Framework Adapter Mode.

Use LlamaIndex readers and indexes for source ingestion, retrieval, and evidence lookup. Emit StoryVista structured artifacts using `story-atlas.schema.json` and `image-manifest.schema.json`.

Keep image generation in a separate provider step.
