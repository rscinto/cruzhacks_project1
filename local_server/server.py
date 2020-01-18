#%%
from time import sleep
import serial

ser = serial.Serial('COM3', 9600)


while True:
    print(".",end="")
    #  ser.write(str(chr(counter))) # Convert the decimal number to ASCII then send it to the Arduino
    print( ser.readline()) # Read the newest output from the Arduino
    sleep(.1) # Delay for one tenth of a second

# %%
