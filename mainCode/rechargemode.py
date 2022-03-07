from readFile import *
from writeFile import *
def rechargeMode(batteryPercentage):
    while batteryPercentage<90:
        #stay in this loop and check battery every 2 mins or however frequently asyncBattery.py is
        batteryText = readFile("batteryText.txt")

        if batteryText.strip()=='yes':

            #reset the battery timer
            writeFile("batteryText.txt","no")

            #check battery
            #dont actually call checkBattery.py or you'll start using recursion (since checkBattery.py also calls rechargeMode.py)
            #instead just copy the code for checking the battery into here
