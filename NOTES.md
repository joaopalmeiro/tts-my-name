# Notes

- https://www.stefanjudis.com/today-i-learned/readonly-files-in-vscode/:
  - `"src/app/core/generated-models/**": true`
  - `"deprecated/**/{*.md,*.py,*.txt,*.yml}": true`
- https://github.com/OHF-Voice/piper1-gpl
  - Old repo: https://github.com/rhasspy/piper
  - https://rhasspy.github.io/piper-samples/#pt_PT-tug%C3%A3o-medium
  - https://github.com/OHF-Voice/piper1-gpl/blob/v1.4.1/docs/API_PYTHON.md
  - https://github.com/OHF-Voice/voice-datasets
  - https://huggingface.co/rhasspy/piper-voices/tree/main/pt/pt_PT/tug%C3%A3o/medium
- https://www.monologue.to/
- https://github.com/Blaizzy/mlx-audio
- https://huggingface.co/mlx-community/chatterbox-fp16
  - https://huggingface.co/ResembleAI/chatterbox
- https://kumo-ui.com/components/combobox/
- https://kumo-ui.com/components/clipboard-text/
  - https://github.com/cloudflare/kumo/blob/%40cloudflare/kumo%401.4.1/packages/kumo/src/components/clipboard-text/clipboard-text.tsx
- https://github.com/QwenLM/Qwen3-TTS
  - https://huggingface.co/spaces/Qwen/Qwen3-TTS
    - "TTS (CustomVoice): Generate speech with predefined speakers and optional style instructions"
- https://github.com/Blaizzy/mlx-audio/blob/v0.3.1/mlx_audio/tts/models/qwen3_tts/README.md
  - [Got error "fix_mistral_regex=True " on Qwen3-TTS-12Hz-1.7B-VoiceDesign-bf16](https://github.com/Blaizzy/mlx-audio/issues/413) issue
    - "I deleted the cache, closed terminal, relaunched terminal and ran the command again. same errors. (Even with the errors it still generates the expected audio)"
- https://github.com/InternLM/Intern-S1
  - https://huggingface.co/internlm/Intern-S1-mini-GGUF
- https://github.com/OpenBMB/MiniCPM-o
  - https://huggingface.co/openbmb/MiniCPM-o-4_5
  - https://huggingface.co/openbmb/MiniCPM-o-4_5-gguf

## Commands

```bash
deactivate && uv venv && source .venv/bin/activate && uv pip install -r requirements.txt --prerelease=allow
```
