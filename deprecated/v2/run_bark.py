from pathlib import Path
from typing import TypedDict

from gaveta.files import ensure_dir
from scipy.io.wavfile import write as write_wav
from transformers import AutoProcessor, BarkModel


class Prompt(TypedDict):
    text: str
    id: str


MODEL_ID = "suno/bark"
VOICES = [f"v2/pt_speaker_{index}" for index in range(10)]

PROMPTS: list[Prompt] = [
    {"text": "João Palmeiro", "id": "baseline"},
    # Source: https://github.com/suno-ai/bark/blob/f4f32d4cd480dfec1c245d258174bc9bde3c2148/README.md#%EF%B8%8F-details
    {"text": "João... Palmeiro", "id": "break_time"},
]

RESULTS = Path("results") / "bark"

if __name__ == "__main__":
    ensure_dir(RESULTS)

    for voice in VOICES:
        for prompt in PROMPTS:
            processor = AutoProcessor.from_pretrained(MODEL_ID)
            model = BarkModel.from_pretrained(MODEL_ID)

            inputs = processor(prompt["text"], voice_preset=voice)

            audio_data = model.generate(**inputs)

            write_wav(
                RESULTS / f"my_name_{voice.replace('/', '_')}_{prompt['id']}.wav",
                rate=model.generation_config.sample_rate,
                data=audio_data.cpu().numpy().squeeze(),
            )
