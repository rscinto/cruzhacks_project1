#%%
# from time import sleep
# import serial

# ser = serial.Serial('COM3', 9600)


# while True:
#     print( ser.readline().decode("utf-8") ) # Read the newest output from the Arduino
#     sleep(.1) # Delay for one tenth of a second

# %%
from time import sleep
import atexit

import serial
import requests
from flask import Flask, jsonify
from multiprocessing import Process, Value

app = Flask(__name__)
SERVER_URL = "https://en459uflysvc8.x.pipedream.net/"

print("Starting Local Server")
@app.route('/')
def hello_world():
   return 'Local Server Started'

def record_loop(loop_on):
   with serial.Serial('COM3', 9600) as ser:
      while True:
         if loop_on.value == True:
            print("loop running")
            arduino_button_state = ser.readline().decode("utf-8").strip() #decode byte string from arduino and strip return characters
            print(repr(arduino_button_state)) # Read the newest output from the Arduino
            
            re = requests.get("https://en459uflysvc8.x.pipedream.net/"+arduino_button_state)
            print(re)  
            
def exit_cleanup():
   print("shutting down")
   exit()
if __name__ == "__main__":
   recording_on = Value('b', True)
   p = Process(target=record_loop, args=(recording_on,))
   p.start()  
   app.run(debug=True, use_reloader=False)
   p.join()
   atexit.register(exit_cleanup)
