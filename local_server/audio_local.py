import speech_recognition as sr
import pyaudio

# get audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak:")
    audio = r.listen(source, phrase_time_limit=5.0)
    print(type(audio))
# "16d5e7247d859dbb052b431e562a3fa09a56f6e9"
try:
    print("You said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))

