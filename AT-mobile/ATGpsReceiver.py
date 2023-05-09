import serial

def parse_gps_data(data):
    data = data.split(',')
    latitude = float(data[2]) / 100
    latitude_direction = data[3]
    longitude = float(data[4]) / 100
    longitude_direction = data[5]
    if latitude_direction == 'S':
        latitude = -latitude
    if longitude_direction == 'W':
        longitude = -longitude
    return latitude, longitude

ser = serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=1)

# Turn on the GPS receiver
ser.write(b'AT+CGNSPWR=1\r')
response = ser.read(10).decode('utf-8').rstrip()
print(response)

# Start the GPS search
ser.write(b'AT+CGNSSEQ=GPGGA\r')
response = ser.read(10).decode('utf-8').rstrip()
print(response)

# Get the GPS data
ser.write(b'AT+CGNSINF\r')
response = ser.read(10).decode('utf-8').rstrip()
print(response)

# Parse the GPS data and convert it to latitude and longitude
latitude, longitude = parse_gps_data(response)

print("Latitude: {}".format(latitude))
print("Longitude: {}".format(longitude))

ser.close()
