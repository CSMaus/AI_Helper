import sounddevice as sd
import numpy as np
import soundfile as sf
import whisper
import tempfile
import os


def record_audio(duration, samplerate=16000):
    """Record audio from the microphone."""
    print("Recording...")
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()
    print("Recording finished.")
    return recording


def transcribe_audio_to_text(audio_data, samplerate=16000, model_size="tiny"):
    """Transcribes audio to text using a temporary file to bypass Whisper's current API limitations."""
    # Create a temporary file to hold the recording
    with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmpfile:
        sf.write(tmpfile.name, audio_data, samplerate)
        model = whisper.load_model(model_size)
        result = model.transcribe(tmpfile.name)
        print("Transcription:", result['text'])
    os.remove(tmpfile.name)


def main_loop():
    model = whisper.load_model("tiny")
    samplerate = 16000

    while True:
        duration = 5
        recording = record_audio(duration, samplerate)

        transcribe_audio_to_text(recording, samplerate)

        if input("Continue recording? (y/n): ").strip().lower() != 'y':
            break

if __name__ == "__main__":
    main_loop()
