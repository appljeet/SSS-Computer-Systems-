import RPi.GPIO as GPIO
from rechargeMode import *

def checkBattery():
    batteryPercentage = None; #set this variable to whatever the percentage should be
    if batteryPercentage>60:
        #go into recharge loop otherwise this will go back to main
        rechargeMode(batteryPercentage)
