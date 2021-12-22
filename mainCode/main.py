import logging

#Format follows convention of: Level of Warning, Time (down to the ms), Message
LOG_FORMAT = "%(levelname)s %(asctime)s -> %(message)s"
logging.basicConfig(filename = "logger.txt", level = logging.DEBUG, format = LOG_FORMAT)
logger = logging.getLogger()

def main():

    logger.info("Starting main loop")
    # check if battery timer is done
    logger.debug("Checking battery")
    bt = open("batteryText.txt", "r")
    batteryText = bt.readline()
    bt.close();
    logger.debug("Successful battery check")

# change name of file so it isnt confused with where health data is actually being stored
    logging.debug("Opening healthFile.txt")
    h = open("healthFile.txt", "r")
    healthText = h.readline()
    h.close();
    logging.debug("Successful healthFile.txt access")

    logging.debug("Opening beacon.txt")
    b = open("beacon.txt", "r")
    beaconText = b.readline()
    b.close();
    logging.debug("Successful beacon.txt access")

    logging.debug("Opening scheduleTimer.txt")
    s = open("scheduleTimer.txt", "r")
    schedulerText = s.readline()
    s.close();
    logging.debug("Successful scheduleTimer.txt access")


    if batteryText.strip()=='yes':
        logging.info("Battery check said yes")
        print('checking battery')
        # write no to file and restart timer
        f = open("batteryText.txt","w")
        f.write("no")
        f.close()
        logging.info("Wrote no to batteryText.txt file")
    elif healthText.strip()=='yes':
        logging.info("Health check said yes")
        print('logging health')
        f = open("healthFile.txt","w")
        f.write("no")
        f.close()
        logging.info("Wrote no to healthText.txt file")
    elif beaconText.strip()=='yes':
        logging.info("Beacon check said yes")
        print('sending to ground')
        f = open("beacon.txt","w")
        f.write("no")
        f.close()
        logging.info("Wrote no to beacon.txt file")
    elif schedulerText.strip()=='yes':

        # TODO: get the async function responsible for this txt file to also write what the current mode is
        # TODO: did not implement logging for scheduler
        # figure out which mode to go into from second line of text file


        f = open("scheduleTimer.txt","w")
        mode = f.readline()
        # calling readline twice gets you the second line
        mode = f.readline()
        f.write("no")
        f.close()

        if mode == 'detumble':
            logging.debug("Calling detumble function")
            print('calling detumble function')
        elif mode == 'runhddtest':
            logging.debug("Calling ADCS HDD function")
            print('calling ADCS HDD function')
        elif mode == 'runmrwtest':
            logging.debug("Calling ADCS MRW Test function")
            print('calling ADCS MRW Test function')
        elif mode == 'hddimagingmode':
            logging.debug("Calling ADCS HDD Imaging function")
            print('calling ADCS HDD Imaging function')
        elif mode == 'mrwimagingmode':
            logging.debug("Calling ADCS MRW Imaging function")
            print('calling ADCS MRW Imaging function')

main()
