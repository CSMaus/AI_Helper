import speech_recognition as sr
import time

audio_file = "Trailer.wav"
lang = "ru-RU"
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
useMicro = True

if useMicro:
    # listening the speech and store in audio_text variable
    with sr.Microphone() as source:
        print("Please speak:")
        audio_data = r.listen(source) # phrase_time_limit, timeout
        print("Recognizing...")

        try:
            text = r.recognize_google(audio_data, language=lang)
            print("You said: {}".format(text))
        except sr.UnknownValueError:
            print("Google Web Speech API could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")

else:
    # use from file
    tstart = time.time()
    with sr.AudioFile(audio_file) as source:
        audio_data = r.record(source)
        print("Recognizing...")
        try:
            text = r.recognize_google(audio_data, language=lang)
            print(f"The text in audio: \n{text}")
            print(f"Time taken: {time.time() - tstart} sec")
        except sr.UnknownValueError:
            print("Google Web Speech API could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")

