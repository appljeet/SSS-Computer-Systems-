import logging
#import RPi.GPIO as GPIO
#local imports
import time
from checkBattery import *
#from deployantenna import *
from detumble import *
from HDDimagingmode import *
from HDDtest import *
from MRWimagingmode import *
from readFile import *
from writeFile import *

#Format follows convention of: Level of Warning, Time (down to the ms), Message
LOG_FORMAT = "%(levelname)s %(asctime)s -> %(message)s"
logging.basicConfig(filename = "logger.txt", level = logging.DEBUG, format = LOG_FORMAT)
logger = logging.getLogger()

def main():

    #time.sleep(1800) wait 30 mins

    logger.info("Starting main loop")

    # Check if we need to wait 30 minutes (first time booting up)
    initialTimer = readFile("initialTimer.txt")
    logging.debug('Succesfully read initialTimer.txt')

    if initialTimer.strip()!='no':
        # Here it will wait for 30 minutes
        logging.debug('Succesfully waited 30 minutes')
        # Write no to file so it doesn't wait the 30 minutes next time it boots up
        writeFile("initialTimer.txt","no")


    #check if antenna has been deployed
    ifAntennaDeploy=readFile("antennaDeploy.txt")
    if ifAntennaDeploy.strip()=='no':
        #actually deploy the antenna
        #deployAntenna()
        #write to text file so antenna doesn't deploy again
        writeFile("antennaDeploy.txt", "no")

    while True:
        
        #Get first line of respective file
        batteryText = readFile("batteryText.txt")
        
        #Get temps and battery percentage of CubeSat
        healthText = readFile("healthFile.txt")
        
        #Transmit data
        beaconText = readFile("beacon.txt")

        if batteryText.strip()=='yes':
            writeFile("batteryText.txt","no")
            logging.info("Battery check said yes, just finished writing no")
            print('checking battery')
            #actually check the battery
            checkBattery()
            # write no to file and restart timer
        if healthText.strip()=='yes':
            writeFile("healthFile.txt","no")
            logging.info("Health check said yes, just finished writing no")
        if beaconText.strip()=='yes':
            writeFile("beacon.txt","no")
            logging.info("Beacon check said yes, just finished writing no")

        #check the battery before hitting the schedule so you dont die mid hdd or mrwtest
        checkBattery()

        #this is checking what mode it should be in
        mode = readFile("scheduleTimer.txt")

        if mode == 'detumble':
            logging.debug("Calling detumble function")
            print('calling detumble function')
            writeFile("schedulerText.txt", "no")
            #Insert ADCS function call here
            #Main_ADCS(sunsensor_input, mag_inputs, angvel_inputs, epoch_time, mode, TLE)
            #detumble()
        elif mode == 'mrwPointing':
            logging.debug("Calling ADCS MRW Pointing")
            print("Calling ADCS MRW Pointing")
            writeFile("schedulerText.txt", "no")
            #Insert ADCS function call here
            #Main_ADCS(sunsensor_input, mag_inputs, angvel_inputs, epoch_time, mode, TLE)
            #hddTest()
        elif mode == 'mrwImaging':
            logging.debug("Calling ADCS MRW Imaging function")
            print("Calling ADCS MRW Imaging function")
            writeFile("schedulerText.txt", "no")
            #Insert ADCS function call here
            #Main_ADCS(sunsensor_input, mag_inputs, angvel_inputs, epoch_time, mode, TLE)
            #mrwTest()
        elif mode == 'hddPointing':
            logging.debug("Calling ADCS HDD Pointing function")
            print("Calling ADCS HDD Pointing")
            writeFile("schedulerText.txt", "no")
            #Insert ADCS function call here
            #Main_ADCS(sunsensor_input, mag_inputs, angvel_inputs, epoch_time, mode, TLE)
            #hddImagingMode()
        elif mode == 'hddImaging':
            logging.debug("Calling ADCS HDD Imaging function")
            print("Calling ADCS HDD Imaging function")
            writeFile("schedulerText.txt", "no")
            #Insert ADCS function call here
            #Main_ADCS(sunsensor_input, mag_inputs, angvel_inputs, epoch_time, mode, TLE)
            #mrwImagingMode()
        #elif mode == "rotisserie":
            #logging.debug("Calling ADCS Rotisserie function")
            #print("Calling ADCS Rotisserie function")
            #writeFile("schedulerText.txt", "no")
            #Insert ADCS function call here
            #Main_ADCS(sunsensor_input, mag_inputs, angvel_inputs, epoch_time, mode, TLE)
main()
