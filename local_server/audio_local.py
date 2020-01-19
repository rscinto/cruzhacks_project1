import speech_recognition as sr
import pyaudio
from time import sleep
import serial

recycling = ["can","cup", "aluminum", "foil", "plastic", "carton", "metal", "bottle"]
trash = ["chip","bag","straw", "tissue", "single-use"]

with serial.Serial('COM3', 9600) as ser:

    # get audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source, phrase_time_limit=5.0)
    try:
        raw_text = r.recognize_google(audio)
        print("Result " + raw_text)
        for recycling_name in recycling:
            print(recycling_name)
            if recycling_name in raw_text:
                print("Open Recycle can!")
                ser.write("100".encode())
                break
        for trash_name in trash:
            if trash_name in raw_text:
                print("Open Trash can!")
                ser.write("2".encode())
                break
        
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

