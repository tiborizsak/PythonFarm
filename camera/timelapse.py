import time
import picamera
from datetime import datetime, timedelta
from fractions import Fraction
from time import sleep

#def wait():
    # Calculate the delay to the start of the next hour
    #next_hour = (datetime.now() + timedelta(hour=1)).replace(
        #minute=0, second=0, microsecond=0)
    #delay = (next_hour - datetime.now()).seconds
    #time.sleep(delay)

with picamera.PiCamera() as camera:
    
    camera.resolution = (2592, 1944)
    #camera.resolution = (1280, 720)
    camera.rotation = 180
    # Set a framerate of 1/6fps, then set shutter
    # speed to 6s and ISO to 800
    camera.framerate = Fraction(1, 6)
    camera.shutter_speed = 10000000
    camera.exposure_mode = 'off'
    camera.iso = 800
    # Give the camera a good long time to measure AWB
    # (you may wish to use fixed AWB instead)
    sleep(10)
    
    camera.start_preview()
    sleep(50)
    for filename in camera.capture_continuous('img{timestamp:%Y-%m-%d-%H-%M-%S}.jpg'):
        sleep(10)
        print('Captured %s' % filename)