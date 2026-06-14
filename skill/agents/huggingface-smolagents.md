# Hugging Face smolagents Adapter

Invocation: expose each pipeline phase as a tool or call the CLI as one local tool.

Capabilities: a Python runtime and artifact storage are expected; image tools are optional.

Limit: tool boundaries must preserve stable IDs and evidence records.

Mode: Framework Adapter Mode.

Implement StoryVista as bounded tools:

- parse source text
- extract entities
- classify importance
- build story atlas JSON
- build visual asset plan
- build image manifest
- render atlas
- verify output

Use schemas in `skill/templates/` as tool contracts.
