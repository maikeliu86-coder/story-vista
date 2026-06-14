# LangChain Adapter

Invocation: model the phases as graph nodes or call the CLI from a tool node.

Capabilities: artifact storage is required; retrieval, image, and browser tools are optional.

Limit: validate state transitions against the canonical schemas.

Mode: Framework Adapter Mode.

Represent StoryVista phases as chain or graph nodes. Validate outputs against templates in `skill/templates/`. Keep provider calls optional and use `image-manifest.json` as the binding contract between generated assets and atlas UI.
