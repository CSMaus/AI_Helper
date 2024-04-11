import speech_recognition as sr
import time

r = sr.Recognizer()
useMicro = False

if useMicro:
    # listening the speech and store in audio_text variable
    with sr.Microphone() as source:
        print("Please speak:")
        audio_data = r.listen(source)
        print("Recognizing...")

        try:
            text = r.recognize_google(audio_data)
            print("You said: {}".format(text))
        except sr.UnknownValueError:
            print("Google Web Speech API could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")

else:
    # use from file
    tstart = time.time()
    audio_file = "harvard.wav"
    with sr.AudioFile(audio_file) as source:
        audio_data = r.record(source)
        print("Recognizing...")
        try:
            text = r.recognize_google(audio_data)
            print(f"The text in audio: \n{text}")
            print(f"Time taken: {time.time() - tstart} sec")
        except sr.UnknownValueError:
            print("Google Web Speech API could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")

