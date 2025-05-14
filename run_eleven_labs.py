import os
from pathlib import Path
from typing import Literal, TypedDict

from dotenv import load_dotenv
from elevenlabs import save
from elevenlabs.client import ElevenLabs
from gaveta.files import ensure_dir


class Model(TypedDict):
    name: str
    language_code: Literal["pt"] | None


class Voice(TypedDict):
    name: str
    id: str


class Prompt(TypedDict):
    text: str
    id: str


MODELS: list[Model] = [
    {"name": "eleven_multilingual_v2", "language_code": None},
    {"name": "eleven_flash_v2_5", "language_code": "pt"},
    {"name": "eleven_turbo_v2_5", "language_code": "pt"},
]

VOICES: list[Voice] = [
    {"name": "Paulo PT", "id": "aLFUti4k8YKvtQGXv0UO"},
    {"name": "Francisco", "id": "WsQeRzWJvoDvhPPJj5r7"},
    {"name": "Victor Power - Ebooks", "id": "YNOujSUmHtgN6anjqXPf"},
]

PROMPTS: list[Prompt] = [
    {"text": "João Palmeiro", "id": "baseline"},
    {"text": '"João" <break time="1.0s" /> "Palmeiro"', "id": "break_time"},
]

RESULTS = Path("results") / "eleven_labs"

if __name__ == "__main__":
    load_dotenv()
    ensure_dir(RESULTS)

    client = ElevenLabs(
        api_key=os.getenv("ELEVENLABS_API_KEY"),
    )

    for model in MODELS:
        for voice in VOICES:
            for prompt in PROMPTS:
                audio_data = client.text_to_speech.convert(
                    text=prompt["text"],
                    voice_id=voice["id"],
                    model_id=model["name"],
                    language_code=model["language_code"],
                    output_format="mp3_44100_128",
                    voice_settings={"speed": 1.0},
                )

                # Source: https://github.com/elevenlabs/elevenlabs-python/blob/v1.58.1/src/elevenlabs/play.py#L62-L66
                save(
                    audio_data,
                    RESULTS
                    / f"my_name_{model['name']}_{voice['name'].replace(' ', '_')}_{prompt['id']}.mp3",
                )
