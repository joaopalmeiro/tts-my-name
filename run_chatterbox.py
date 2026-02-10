from pathlib import Path

from gaveta.files import ensure_dir
from mlx_audio.tts.generate import generate_audio

if __name__ == "__main__":
    ensure_dir(Path("results"))

    generate_audio(
        text="João Palmeiro",
        model="mlx-community/chatterbox-fp16",
        lang_code="pt",
        audio_format="wav",
        output_path=Path("results"),
        file_prefix="chatterbox",
    )
