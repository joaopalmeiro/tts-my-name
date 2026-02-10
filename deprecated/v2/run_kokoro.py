from pathlib import Path

from gaveta.files import ensure_dir
from kokoro import KPipeline
from scipy.io.wavfile import write as write_wav

MODEL_ID = "hexgrad/Kokoro-82M"
VOICES = ["pf_dora", "pm_alex", "pm_santa"]

RESULTS = Path("results") / "kokoro"

if __name__ == "__main__":
    ensure_dir(RESULTS)

    pipeline = KPipeline(lang_code="p", repo_id=MODEL_ID)

    for voice in VOICES:
        generator = pipeline("João Palmeiro", voice=voice)

        audio_data = next(generator)[-1]

        write_wav(
            RESULTS / f"my_name_{voice}.wav",
            # Source: https://github.com/hexgrad/kokoro/blob/2668b2e279d0f94977995230e523b0183763f30e/examples/phoneme_example.py#L14
            rate=24_000,
            data=audio_data.cpu().numpy(),
        )
