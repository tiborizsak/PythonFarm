import statistics
import serial
import picamera
from fractions import Fraction
from time import sleep

vidno = 0

for i in range(0,60):

    with picamera.PiCamera() as camera:
        #This section is used in case of low light capture
        camera.framerate = Fraction(1, 6)
        camera.sensor_mode = 3
        camera.shutter_speed = 6000000
        camera.iso = 300
        sleep(30)
        camera.exposure_mode = 'off'
        
        camera.rotation = 180
        camera.resolution = (1920, 1080)
        camera.start_recording('./output/my_video' + str(vidno) + '.h264')
        camera.wait_recording(10)
        camera.stop_recording()
        vidno += 1
        sleep(10)
