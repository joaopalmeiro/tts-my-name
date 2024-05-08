from pathlib import Path

from omegaconf import OmegaConf
from transformers import pipeline


def write_txt(data: str, output_path: Path) -> None:
    with output_path.open(mode="w", encoding="utf-8") as f:
        f.write(data)


if __name__ == "__main__":
    conf = OmegaConf.load("config.yml")

    model = pipeline(
        "automatic-speech-recognition",
        model="openai/whisper-large-v3",
        revision="1ecca609f9a5ae2cd97a576a9725bc714c022a93",
    )

    output = model(conf.input_audio, generate_kwargs={"language": "english"})["text"]
    write_txt(output, Path("01.txt"))
