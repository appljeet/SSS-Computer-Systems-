import sched
import time
import os
from writeFile import *
import random
# this one is different because it needs to figure out what the schedule is and write that to the text file
currentTime = 17

while True:
    #get time from RTC and convert to double so you can compare. Then store it in currentTime variable
    # when getting time from rtc, drop the seconds and simply convert the time to decimal format.
    #for example: 1:12:43 turns into 1.12

    if currentTime>0 and currentTime<=2:
        schedule = "detumble"
    elif currentTime>4 and currentTime<=6:
        schedule = "mrwPointing"
    elif currentTime>8 and currentTime<=10:
        schedule = "mrwImaging"
    elif currentTime>12 and currentTime<=14:
        schedule = "hddPointing"
    elif currentTime>16 and currentTime<=18:
        schedule = "hddImaging"
    #elif currentTime>20 and currentTime<22:
    #    schedule = "rotisserie" 

    print("current time = " + str(currentTime))
    writeFile("scheduleTimer.txt",schedule)

    currentTime = random.randrange(0,18,1) #only for testing
    time.sleep(1) #stops us from checking the time every millisecond