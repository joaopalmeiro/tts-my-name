from transformers import pipeline

if __name__ == "__main__":
    model = pipeline(
        "automatic-speech-recognition",
        model="openai/whisper-large-v3",
        revision="1ecca609f9a5ae2cd97a576a9725bc714c022a93",
    )

    output = model("audio1984602622.m4a", generate_kwargs={"language": "english"})[
        "text"
    ]
    print(output)
