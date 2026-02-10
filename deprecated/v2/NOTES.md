# Notes

- https://github.com/joaopalmeiro/template-python-uv-script
- https://pypi.org/project/mlx-audio/
- https://huggingface.co/models?pipeline_tag=text-to-speech
- https://huggingface.co/models?inference_provider=all&pipeline_tag=text-to-speech&sort=trending
- Models:
  - https://github.com/hexgrad/kokoro
    - https://github.com/hexgrad/kokoro/blob/2668b2e279d0f94977995230e523b0183763f30e/kokoro.js/src/voices.js#L4
    - https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md
    - https://github.com/hexgrad/misaki
  - https://github.com/kyutai-labs/moshi
  - https://github.com/suno-ai/bark
    - https://suno-ai.notion.site/8b8e8749ed514b0cbf3f699013548683?v=bc67cff786b04b50b3ceb756fd05f68c
    - https://huggingface.co/docs/transformers/model_doc/bark
    - https://huggingface.co/spaces/suno/bark
    - https://huggingface.co/suno/bark-small
    - [how to set The attention mask and the pad token id ?](https://github.com/suno-ai/bark/issues/402) issue
  - https://huggingface.co/canopylabs/orpheus-3b-0.1-ft
  - https://play.ai/:
    - https://play.ai/play-dialog
    - https://play.ai/play-mini
    - https://docs.play.ai/documentation/text-to-speech/tts-models
  - https://huggingface.co/parler-tts/parler-tts-mini-multilingual-v1.1
  - https://huggingface.co/fishaudio/fish-speech-1.5
- https://docs.pytorch.org/docs/stable/generated/torch.Tensor.cpu.html
- https://console.groq.com/docs/vision#multiturn-conversations-with-images: "Multi-turn Conversations with Images"
- ElevenLabs:
  - https://elevenlabs.io/docs/quickstart
  - https://elevenlabs.io/docs/models
  - https://elevenlabs.io/docs/cookbooks/text-to-speech/quickstart
  - https://github.com/jiaaro/pydub
  - https://elevenlabs.io/docs/cookbooks/text-to-speech/pronunciation-dictionaries
  - https://elevenlabs.io/docs/api-reference/text-to-speech/convert
  - https://elevenlabs.io/app/voice-library
  - https://github.com/elevenlabs/elevenlabs-python
  - https://elevenlabs.io/docs/api-reference/text-to-speech/convert#request.body.language_code: "Currently only Turbo v2.5 and Flash v2.5 support language enforcement. For other models, an error will be returned if language code is provided."
  - https://elevenlabs.io/docs/best-practices/prompting/controls#pauses
  - `{"name": "Lucas — Male, Informative Voice", "id": "SVgp5d1fyFQRW1eQbwkq"}`
- https://arxiv.org/pdf/2304.10548:
  - "Zero-shot vs. One-shot vs. Few-shots: Since recent work showed conflicting results on the number of examples in a prompt, we explored different prompt settings."
  - https://arxiv.org/pdf/2107.13586

## Commands

```bash
deactivate && uv venv && source .venv/bin/activate && uv pip install -r requirements.txt
```

```bash
uv venv && source .venv/bin/activate && uv pip install -r requirements.txt
```

```bash
cp .env.example .env
```

### Clean slate

```bash
rm -rf .mypy_cache/ .ruff_cache/ .venv/
```
