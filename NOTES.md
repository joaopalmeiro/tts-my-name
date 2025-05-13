# Notes

- https://github.com/joaopalmeiro/template-python-uv-script
- https://pypi.org/project/mlx-audio/
- Models:
  - https://github.com/hexgrad/kokoro
    - https://github.com/hexgrad/kokoro/blob/2668b2e279d0f94977995230e523b0183763f30e/kokoro.js/src/voices.js#L4
    - https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md
  - https://github.com/kyutai-labs/moshi
  - https://github.com/suno-ai/bark
    - https://suno-ai.notion.site/8b8e8749ed514b0cbf3f699013548683?v=bc67cff786b04b50b3ceb756fd05f68c
    - https://huggingface.co/docs/transformers/model_doc/bark
    - https://huggingface.co/spaces/suno/bark
    - https://huggingface.co/suno/bark-small
    - [how to set The attention mask and the pad token id ?](https://github.com/suno-ai/bark/issues/402) issue

## Commands

```bash
deactivate && uv venv && source .venv/bin/activate && uv pip install -r requirements.txt
```

```bash
uv venv && source .venv/bin/activate && uv pip install -r requirements.txt
```

### Clean slate

```bash
rm -rf .mypy_cache/ .ruff_cache/ .venv/
```
