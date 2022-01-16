import os
from picamera import PiCamera
from datetime import datetime

home = os.path.expanduser("~") #determines home path regardless of OS
file_path = home + '/SSS/images'

camera = PiCamera()

def capture():
    timestamp = datetime.now().isoformat()
    camera.capture(os.path.join(file_path, ('/%s.jpg' % timestamp)))

capture()