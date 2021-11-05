#-----------------------------------------------------------------------------------------
#Developer: Jackie Arroyo 
#Purpose of code: To run a 30 second timer after deployment of satelite before initializing
#------------------------------------------------------------------------------------------

import time 
#there are 1800 seconds in 30 minutes
t = 1800

while t: 
    minutes = t//60
    seconds = t%60
    timer = '{:02d}:{:02d}'.format(minutes,seconds)
    print(timer, end='\r')                                     # '\r' overwrites previous time with new time
    time.sleep(1)                                              #sleeps every 1 second
    t-= 1                                                      #counts down incriments of 100    
      
