import sys
import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt
import librosa

# data sources: https://voiceage.com/Audio-Samples-AMR-WB.html
# kaggle
# korean: https://www.kaggle.com/datasets/bryanpark/korean-single-speaker-speech-dataset/data


def find_split_points(envelope, sr, percent=100, isPlot=False):

    median_value = np.median(envelope)
    meanv = np.mean(envelope)
    silent_parts_array = np.zeros_like(envelope)
    silent_parts_array[np.where(envelope > median_value*percent/100)] = meanv
    prev_val = silent_parts_array[0]
    part_len = 0
    for i in range(1, len(silent_parts_array)):
        if silent_parts_array[i] == 0 and prev_val == 0:
            part_len += 1
        elif silent_parts_array[i] != 0 and prev_val == 0 and part_len < sr/2:
            silent_parts_array[i - part_len - 1:i] = meanv
            part_len = 0
        elif silent_parts_array[i] != 0 and prev_val == 0 and part_len >= sr / 2:
            part_len = 0
        prev_val = silent_parts_array[i]

    part_len = 0
    split_points = []
    for i in range(1, len(silent_parts_array)):
        if silent_parts_array[i] == 0:
            part_len += 1
        if silent_parts_array[i] > 0 or i == len(silent_parts_array) - 1:
            if part_len >= sr / 2:
                middle_point = i - part_len // 2
                split_points.append(middle_point)
                part_len = 0
            else:
                part_len = 0
    if isPlot:
        plt.figure(figsize=(10, 6))
        plt.plot(envelope)
        plt.axhline(y=median_value * percent / 100, color='r', linestyle='-', label=f'{percent}% of Median')
        plt.plot(silent_parts_array)
        plt.title('Audio Envelope')
        plt.xlabel('Sample')
        plt.ylabel('Amplitude')
        plt.show()

    return split_points


audio_file = "Korean_1_0000.wav"
lang = "ko-KR"
# languages:
# en-US - English (United States)
# es-ES - Spanish (Spain)
# fr-FR - French (France)
# de-DE - German (Germany)
# zh-CN - Chinese (Mandarin/China)
# hi-IN - Hindi (India)
# ar-SA - Arabic (Saudi Arabia)
# ru-RU - Russian (Russia)
# ja-JP - Japanese (Japan)
# ko-KR - Korean (South Korea)
r = sr.Recognizer()

with sr.AudioFile(audio_file) as source:
    audio_data = r.record(source)
    print("Recognizing...")
    try:
        textFull = r.recognize_google(audio_data, language=lang)
        print(f"Full text in audio: \n{textFull}")
    except sr.UnknownValueError:
        print("Google Web Speech API could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")


sys.exit()
print("Recognising text by parts...")

audio, sr_rate = librosa.load(audio_file)
envelope = np.abs(audio)
split_points = find_split_points(envelope, sr_rate/2, 150, False)

recognized_texts = ""

for i, point in enumerate(split_points):
    start = split_points[i-1] if i > 0 else 0
    end = point
    start_time = start / sr_rate
    end_time = end / sr_rate
    fragment = audio[start:end]

    with sr.AudioFile(audio_file) as source:
        audio_data = r.record(source, duration=end_time-start_time, offset=start_time)
        try:
            text = r.recognize_google(audio_data)
            recognized_texts += "\n"+text
        except sr.UnknownValueError:
            print("Google Web Speech API could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")

print("Recognized Text:\n", recognized_texts)
