#%%
# from time import sleep
# import serial

# ser = serial.Serial('COM3', 9600)


# while True:
#     print( ser.readline().decode("utf-8") ) # Read the newest output from the Arduino
#     sleep(.1) # Delay for one tenth of a second

# %%
from time import sleep
import serial
import requests
from flask import Flask, jsonify
from multiprocessing import Process, Value

ser = serial.Serial('COM3', 9600)

app = Flask(__name__)
print("Starting Local Server")
@app.route('/')
def hello_world():
    return 'Hello, World!'
# while True:
#     print( ser.readline().decode("utf-8") ) # Read the newest output from the Arduino
#     sleep(.1) # Delay for one tenth of a second




tasks = [
   {
      'id': 1,
      'title': u'Buy groceries',
      'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
      'done': False
   },
   {
      'id': 2,
      'title': u'Learn Python',
      'description': u'Need to find a good Python tutorial on the web', 
      'done': False
   }
]


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
   return jsonify({'tasks': tasks})


def record_loop(loop_on):
   while True:
      if loop_on.value == True:
         print("loop running")
         print( ser.readline().decode("utf-8") ) # Read the newest output from the Arduino
         
         requests.get("https://enaaxnabzfjwp.x.pipedream.net/")
         sleep(0.1)

if __name__ == "__main__":
   recording_on = Value('b', True)
   p = Process(target=record_loop, args=(recording_on,))
   p.start()  
   app.run(debug=True, use_reloader=False)
   p.join()
# %%
