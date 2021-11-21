import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(27, GPIO.OUT)

GPIO.output(27, True)





