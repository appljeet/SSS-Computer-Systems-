import time

# this one is different because it needs to figure out what the schedule is and write that to the text file



while True:
    time.sleep (1) #checks battery every minute
    f = open("scheduleTimer.txt", "w")
    f.write("yes") #writing yes to txt file every minute

    ## TODO: write code to calculate current scheduled state of sat

    f.close()
