import serial
import time

ser = serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=1)

# Send the AT command to retrieve the cell tower information
ser.write(b'AT+CREG?\r')
#ser.write(b'AT+CREG=2\r')
response = ser.read(100).decode('utf-8').rstrip()
time.sleep(3)
print(response)

# Parse the response to extract the MCC, MNC, and CID
data = response.split(',')
mcc = data[2][:3]
mnc = data[2][3:]
cid = data[3]

print("MCC: {}".format(mcc))
print("MNC: {}".format(mnc))
print("CID: {}".format(cid))

ser.close()
