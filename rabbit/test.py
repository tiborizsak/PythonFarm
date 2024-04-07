import serial
import time

s = serial.Serial('COM3', 9600)
s.xonxoff = 1
counter = 0
# res = s.read()
# print(res)

while True:
    counter += 1
    time.sleep(0.001)
    s.readline()
    if counter % 100 == 0:
        #print(int(s.readline()[:-2]))
        print(int(s.readline()))