import whisper
import argparse
import os

def transcribe(audio_path, model_size="small"):
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"File not found: {audio_path}")

    print(f" Loading model '{model_size}'...")
    model = whisper.load_model(model_size)

    print("️ Converting audio to text...")
    result = model.transcribe(audio_path, language="fa")

    print("\nRecognized text:")
    print(result["text"])

    output_path = os.path.splitext(audio_path)[0] + ".txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result["text"])

    print(f"\nText saved to file.: {output_path}")
