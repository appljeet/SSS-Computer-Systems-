import time
import os
# this one is different because it needs to figure out what the schedule is and write that to the text file

home = os.path.expanduser("~") #determines home path regardless of OS
file_path = home + '/SSS/mainCode'
file_name = "scheduleTimer.txt"

completeName = os.path.join(file_path, file_name)

while True:
    time.sleep (60) #checks battery every minute
    f = open(completeName, "w")
    f.write("yes") #writing yes to txt file every minute

    ## TODO: write code to calculate current scheduled state of sat

    f.close()
