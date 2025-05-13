from pathlib import Path

from gaveta.files import ensure_dir
from scipy.io.wavfile import write as write_wav
from transformers import AutoProcessor, BarkModel

MODEL_ID = "suno/bark"
VOICE_PRESETS = [f"v2/pt_speaker_{index}" for index in range(10)]

RESULTS = Path("results") / "bark"

if __name__ == "__main__":
    ensure_dir(RESULTS)

    for voice_preset in VOICE_PRESETS:
        processor = AutoProcessor.from_pretrained(MODEL_ID)
        model = BarkModel.from_pretrained(MODEL_ID)

        inputs = processor("João Palmeiro", voice_preset=voice_preset)

        audio_array = model.generate(**inputs)

        write_wav(
            RESULTS / f"my_name_{voice_preset.replace('/', '_')}.wav",
            rate=model.generation_config.sample_rate,
            data=audio_array.cpu().numpy().squeeze(),
        )
