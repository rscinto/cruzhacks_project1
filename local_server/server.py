# %%
from time import sleep
import speech_recognition as sr
import serial

recycling = ["can","cup"]
trash = ["chip","bag"]



def record_audio():
   r = sr.Recognizer()
   with sr.Microphone() as source:
      print("Speak:")
      audio = r.listen(source, phrase_time_limit=5.0)
   try:
      text = r.recognize_google(audio)
      print("Result " + text)
      return text

   except sr.UnknownValueError:
      print("Could not understand audio")
   except sr.RequestError as e:
      print("Could not request results; {0}".format(e))
   return "ERROR"
def open_trash_door(raw_text):
   for recycling_name in recycling:
         if recycling_name in raw_text:
            print("Open Recycle can!")
            ser.write("100".encode())
            break
   for trash_name in trash:
         if trash_name in raw_text:
            print("Open Trash can!")
            ser.write("100".encode())
            break
         
if __name__ == "__main__":
   with serial.Serial("COM3",9600) as ser:
      while True:
         arduino_button_state = ser.readline().decode("utf-8").strip() #decode byte string from arduino and strip return characters
         audio_command = record_audio()
         open_trash_door(audio_command)