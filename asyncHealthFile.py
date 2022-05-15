import logging
import time
import os
from writeFile import *

while True:
    writeFile("healthFile.txt","yes")
    time.sleep(60) #checks battery every minute
