import logging
import time
import os
from writeFile import *

while True:
    writeFile("batteryText.txt", "yes")
    time.sleep (60) #checks battery every minute
