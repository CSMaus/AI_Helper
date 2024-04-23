import speech_recognition as sr
import time


# for punctuator make sure to have installed c++ build tools
# https://visualstudio.microsoft.com/visual-cpp-build-tools/

# punct_model = pipeline("text-generation", model="lvwerra/bert-imdb")
audio_file = "Trailer.wav"
lang = "en-US"
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
useMicro = False

if useMicro:
    # listening the speech and store in audio_text variable
    # need to run this parts in parallel, to keep all text.
    # i e if one part is recorded, then we sdtart recognize it and in parallel to write another part
    with sr.Microphone() as source:
        # can setup hot word with using snowboy_configuration
        print("Please speak:")
        audio_data = r.listen(source)  # phrase_time_limit, timeout
        # listen_in_background
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

            # punctuated_text = punct_model(text)[0]['generated_text']
            # print(f"Punctuated text: \n{punctuated_text}")
            print(f"Time taken: {time.time() - tstart} sec")
        except sr.UnknownValueError:
            print("Google Web Speech API could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")

