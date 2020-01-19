# %%
from time import sleep
import speech_recognition as sr
import serial
import requests


response  = requests.get('https://storeie5k4smygdd3w.blob.core.windows.net/cruzhacks/json_test.json')
data = json.loads(response.text)




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
   for recycling_item in data['recycling']:
         if recycling_name in raw_text:
            print("Open Recycle can!")
            ser.write("100".encode())
            response = requests.post('https://events-api.notivize.com/applications/91f0d979-965d-4218-8bab-369ce0c1a762/event_flows/b5016281-b0e7-46ba-9af4-05009a5d00d6/events', json={"garbage": garbage, "recycle": 1})
            print(response)
            return
   
   for trash_name in data['trash']:
         if trash_name in raw_text:
            print("Open Trash can!")
            ser.write("100".encode())
            response = requests.post('https://events-api.notivize.com/applications/91f0d979-965d-4218-8bab-369ce0c1a762/event_flows/b5016281-b0e7-46ba-9af4-05009a5d00d6/events', json={"garbage": garbage, "recycle": 1})
            print(response)
            return
        
        
         
if __name__ == "__main__":
   with serial.Serial("COM3",9600) as ser:
      while True:
         arduino_button_state = ser.readline().decode("utf-8").strip() #decode byte string from arduino and strip return characters
         audio_command = record_audio()
         open_trash_door(audio_command)