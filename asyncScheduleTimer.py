import time
import os
# this one is different because it needs to figure out what the schedule is and write that to the text file

home = os.path.expanduser("~") #determines home path regardless of OS
file_path = home + '/SSS-Computer-Systems-/asyncTextFiles'
file_name = "scheduleTimer.txt"

completeName = os.path.join(file_path, file_name)

while True:
    time.sleep (60) #stops us from checking the time every millisecond

    #get time from RTC and convert to double so you can compare. Then store it in currentTime variable
    # when getting time from rtc, drop the seconds and simply convert the time to decimal format.
    #for example: 1:12:43 turns into 1.12

    if currentTime>0 && currentTime<2:
        schedule = "detumble"
    elif currentTime>4 && currentTime<6:
        schedule = "runhddtest"
    elif currentTime>8 && currentTime<10:
        schedule = "runmrwtest"
    elif currentTime>12 && currentTime<14:
        schedule = "hddimagingmode"
    elif currentTime>16 && currentTime<18:
        schedule = "mrwimagingmode"

    f = open(completeName, "w")
    f.write(schedule) #writing yes to txt file every minute
    f.close()
