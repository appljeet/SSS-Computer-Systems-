#import RPi.GPIO as GPIO
from rechargemode import *

def checkBattery():
    batteryPercentage = 70; #set this variable to whatever the percentage should be
    if batteryPercentage<60:
        #go into recharge loop otherwise this will go back to main
        rechargeMode(batteryPercentage)
