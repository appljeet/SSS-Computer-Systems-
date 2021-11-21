def main():

    # check if battery timer is done
    bt = open("batteryText.txt", "r")
    batteryText = bt.readline()
    bt.close();

# change name of file so it isnt confused with where health data is actually being stored
    h = open("healthFile.txt", "r")
    healthText = h.readline()
    h.close();

    b = open("beacon.txt", "r")
    beaconText = b.readline()
    b.close();

    s = open("scheduleTimer.txt", "r")
    schedulerText = s.readline()
    s.close();



    if batteryText.strip()=='yes':
        print('checking battery')
        # write no to file and restart timer
        f = open("batteryText.txt","w")
        f.write("no")
        f.close()
    elif healthText.strip()=='yes':
        print('logging health')

        f = open("healthFile.txt","w")
        f.write("no")
        f.close()
    elif beaconText.strip()=='yes':
        print('sending to ground')

        f = open("beacon.txt","w")
        f.write("no")
        f.close()
    elif schedulerText.strip()=='yes':

        # TODO: get the async function responsible for this txt file to also write what the current mode is
        # figure out which mode to go into from second line of text file


        f = open("scheduleTimer.txt","w")
        mode = f.readline()
        # calling readline twice gets you the second line
        mode = f.readline()
        f.write("no")
        f.close()

        if(mode = 'detumble'):
            print('calling detumble function')
        elif(mode = 'runhddtest'):
            print('calling ADCS HDD function')
        elif(mode='runmrwtest'):
            print('calling ADCS MRW Test function')
        elif(mode = 'hddimagingmode'):
            print('calling ADCS HDD Imaging function')
        elif(mode = 'mrwimagingmode'):
            print('calling ADCS MRW Imaging function')

main()
