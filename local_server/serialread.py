from time import sleep
import serial
import requests

with serial.Serial('COM3', 9600) as ser:

    while True:
        print("loop running")
        arduino_button_state = ser.readline().decode("utf-8").strip() #decode byte string from arduino and strip return characters
        print(repr(arduino_button_state)) # Read the newest output from the Arduino
        re = requests.get("https://en459uflysvc8.x.pipedream.net/"+arduino_button_state)
        print(re)   
        # sleep(0.1)