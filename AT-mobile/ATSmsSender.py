import serial

ser = serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=1)

# Send the AT command to initialize the modem
ser.write(b'AT\r')
response = ser.read(10).decode('utf-8').rstrip()
print(response)

# Check if the modem is ready to receive AT commands
ser.write(b'AT+CPMS?\r')
response = ser.read(10).decode('utf-8').rstrip()
print(response)

# Set the modem to use text message format
ser.write(b'AT+CMGF=1\r')
response = ser.read(10).decode('utf-8').rstrip()
print(response)

# Get the phone number from the user
phone_number = input("Enter the recipient's phone number: ")

# Set the recipient phone number
ser.write(f'AT+CMGS="{phone_number}"\r'.encode())
response = ser.read(10).decode('utf-8').rstrip()
print(response)

# Get the message text from the user
message = input("Enter the text of the message: ")

# Send the message
ser.write(f'{message}\r\x1a'.encode())
response = ser.read(10).decode('utf-8').rstrip()
print(response)

ser.close()
