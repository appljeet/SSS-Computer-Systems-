import logging
import RPi.GPIO as GPIO

def deployAntenna():
    #Need to test setting gpio to high. IDK if it's set high for a millisecond or for the duration of the program
    #engage burnwire resistor
    GPIO.setmode(GPIO.BOARD)
    #need to change address of gpio pin because we don't know what it should be
    GPIO.setup(5, GPIO.OUT)
    #setting gpio pin to high
    GPIO.output(5, GPIO.HIGH)
    logging.debug('Deployed Antenna')
