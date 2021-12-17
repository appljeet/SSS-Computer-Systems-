import time

while True:
    time.sleep (1) #checks battery every minute
    f = open("beacon.txt", "w")
    f.write("yes") #writing yes to txt file every minute
    f.close()
