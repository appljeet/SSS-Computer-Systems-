import time
import os

home = os.path.expanduser("~") #determines home path regardless of OS
file_path = home + '/SSS/mainCode'
file_name = "batteryText.txt"

completeName = os.path.join(file_path, file_name)

while True:
    time.sleep (60) #checks battery every minute
    f = open(completeName, "w")
    f.write("yes") #writing yes to txt file every minute
    f.close()
