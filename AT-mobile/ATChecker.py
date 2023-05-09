import time
import serial
import os

cmd = ''
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
ser.reset_input_buffer()

while True:
    smd=input("gimme command: ")
    smd=smd+'\n'
    smds=smd.encode('utf-8')
    ser.write(smds)
    print("smd value is: ",smd)
    line = ser.read(10).decode('utf-8').rstrip()
    print(line)
