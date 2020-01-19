# %%
from time import sleep
import speech_recognition as sr
import serial
import requests
import platform

recycling = ["can","cup"]
trash = ["chip","bag"]
garbage = "17074946135"

PLATFORM = platform.system()
if PLATFORM == "Windows":
	COM_PORT = "COM3"
else:
	COM_PORT = '/dev/cu.usbmodem1411'



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
            response = requests.post('https://events-api.notivize.com/applications/91f0d979-965d-4218-8bab-369ce0c1a762/event_flows/b5016281-b0e7-46ba-9af4-05009a5d00d6/events', json={"garbage": garbage, "recycle": 1})
            print(response)
            return
   for trash_name in trash:
         if trash_name in raw_text:
            print("Open Trash can!")
            ser.write("100".encode())
            response = requests.post('https://events-api.notivize.com/applications/91f0d979-965d-4218-8bab-369ce0c1a762/event_flows/b5016281-b0e7-46ba-9af4-05009a5d00d6/events', json={"garbage": garbage, "recycle": 1})
            print(response)
            return
        
        
         
if __name__ == "__main__":

# with serial.Serial("COM3",9600) as ser: PC
	with serial.Serial(COM_PORT,9600) as ser:
		while True:
			arduino_button_state = '0' # init
			while arduino_button_state != '1':
				arduino_button_state = ser.readline().decode("utf-8").strip() #decode byte string from arduino and strip return characters

			print(arduino_button_state)
			audio_command = record_audio()
			open_trash_door(audio_command)
			arduino_button_state = "0"






