import whisper
import sounddevice as sd
import numpy as np
import tempfile
import wave
import os


def transcribe_audio_file(audio_file_path, model_size="tiny"):
    """
    :param audio_file_path: str to audio file in wav format
    :param model_size: "tiny": 39M, "base": 74M, "small": 244M, "medium" 769M, "large" 1550M
    :return: print parsed text, no return
    """
    model = whisper.load_model(model_size)
    result = model.transcribe(audio_file_path)
    print(result["text"])


def process_audio_chunk(indata, frames, time, status):
    tmpfile_path = tempfile.mktemp()
    try:
        with wave.open(tmpfile_path, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(16000)  # Whisper works with 16kHz audio
            wf.writeframes(indata.tobytes())

        result = model.transcribe(tmpfile_path)
        print(result["text"])
    finally:
        os.remove(tmpfile_path)


if __name__ == "__main__":
    audio_file_path = "test.wav"
    # transcribe_audio_file(audio_file_path)
    model = whisper.load_model("tiny")
    with sd.InputStream(callback=process_audio_chunk, dtype='int16', channels=1, samplerate=16000):
        print("Recording... Press Ctrl+C to stop.")
        sd.sleep(10000)

