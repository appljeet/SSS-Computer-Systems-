import logging
import os

def writeFile(file_name, message):
    #Format follows convention of: Level of Warning, Time (down to the ms), Message
    LOG_FORMAT = "%(levelname)s %(asctime)s -> %(message)s"
    logging.basicConfig(filename = "logger.txt", level = logging.DEBUG, format = LOG_FORMAT)
    logger = logging.getLogger()
    
    home = os.path.expanduser("~") #determines home path regardless of OS
    file_path = '../SSS-Computer-Systems-/asyncTextFiles'
    completeName = os.path.join(file_path, file_name)
    w = open(completeName, "w")
    w.write(message)
    w.close()
    logging.info("Wrote " + message + " to " + file_name)
