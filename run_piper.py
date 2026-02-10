import wave
from pathlib import Path

from gaveta.files import ensure_dir
from piper import PiperVoice

if __name__ == "__main__":
    ensure_dir(Path("results"))

    voice = PiperVoice.load("pt_PT-tug%C3%A3o-medium.onnx")

    with wave.open(str(Path("results") / "piper.wav"), "wb") as wav_file:
        voice.synthesize_wav("João Palmeiro", wav_file)
