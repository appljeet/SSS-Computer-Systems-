from readFile import *
from writeFile import *
import time
def rechargeMode(batteryPercentage):
    while batteryPercentage<90:
        time.sleep(300) #check battery every 5 mins
        # here is where you should be getting battery info
        if batteryText.strip()=='yes':

            #reset the battery timer
            writeFile("batteryText.txt","no")

            #check battery
            #dont actually call checkBattery.py or you'll start using recursion (since checkBattery.py also calls rechargeMode.py)
            #instead just copy the code for checking the battery into here
