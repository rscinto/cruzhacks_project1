# %%
from time import sleep
import speech_recognition as sr
import serial
import requests
import platform
import json
import os
import warnings
import serial
import serial.tools.list_ports
import pathlib
import os,webbrowser

# add "export PHONE_NUMBER='<phone_number>'" to bashrc
PHONE_NUMBER = os.environ.get('PHONE_NUMBER')

response  = requests.get('https://storeie5k4smygdd3w.blob.core.windows.net/cruzhacks/json_test.json')
data = json.loads(response.text)


PLATFORM = platform.system()
if PLATFORM == "Windows":
	COM_PORT = "COM4"
else:
   COM_PORT = ""
   for p in serial.tools.list_ports.comports():
      if "usbmodem" in p.device:
         print(p.device)
         COM_PORT = p.device


def record_audio():
   r = sr.Recognizer()
   with sr.Microphone() as source:
      print("Speak:")
      audio = r.listen(source, phrase_time_limit=3.0)
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

   decided = 0

   for recycling_item in data['recycling']:
         if recycling_item in raw_text:
            decided = 1
            show_photo(recycling_item)
            print("Open Recycle can!")
            ser.write("0".encode())
            response = requests.post('https://events-api.notivize.com/applications/91f0d979-965d-4218-8bab-369ce0c1a762/event_flows/b5016281-b0e7-46ba-9af4-05009a5d00d6/events', json={"garbage": PHONE_NUMBER, "recycle": 1})
            print(response)
            return
   
   for trash_item in data['trash']:
         if trash_item in raw_text:
            decided = 1
            show_photo(trash_item)
            print("Open Trash can!")
            ser.write("180".encode())
            response = requests.post('https://events-api.notivize.com/applications/91f0d979-965d-4218-8bab-369ce0c1a762/event_flows/b5016281-b0e7-46ba-9af4-05009a5d00d6/events', json={"garbage": PHONE_NUMBER, "recycle": 1})
            print(response)
            return

   # if it was neither in trash or recycle dict, trash it
   if decided == False:
      print("Open Trash can!")
      ser.write("180".encode())
      response = requests.post('https://events-api.notivize.com/applications/91f0d979-965d-4218-8bab-369ce0c1a762/event_flows/b5016281-b0e7-46ba-9af4-05009a5d00d6/events', json={"garbage": PHONE_NUMBER, "recycle": 1})
      print(response)

def show_photo(name):
    name_ = name + ".jpg"
    img_path = pathlib.Path.cwd() / "img" / name_
    print(img_path)
    if img_path.is_file():
        if PLATFORM == "Windows":
            iexplore = os.path.join(os.environ.get("PROGRAMFILES", "C:\\Program Files"),
                                    "Internet Explorer\\IEXPLORE.EXE")
            browser = webbrowser.get(iexplore)
            browser.get(str(img_path))

        else:
            browser = webbrowser.get("chrome")
            browser.open('file://'+str(img_path), new=0)


    else:
        print("Item not in database found")
           
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
