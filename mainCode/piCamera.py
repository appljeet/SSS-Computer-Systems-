import os
from picamera import PiCamera
from datetime import datetime
from time import sleep

camera = PiCamera()

def capture():
    camera.resolution(1920, 1080)
    timestamp = datetime.now().isoformat()
    sleep(3)
    camera.capture('../images/%s.jpg' % timestamp)

capture()