def readFile(file_name):
    #Format follows convention of: Level of Warning, Time (down to the ms), Message
    LOG_FORMAT = "%(levelname)s %(asctime)s -> %(message)s"
    logging.basicConfig(filename = "logger.txt", level = logging.DEBUG, format = LOG_FORMAT)
    logger = logging.getLogger()

    home = os.path.expanduser("~") #determines home path regardless of OS
    file_path = home + '/SSS-Computer-Systems-/asyncTextFiles'
    completeName = os.path.join(file_path, file_name)
    r = open(completeName, "r")
    text = r.readline()
    r.close()
    logging.info("Read from " + file_name)
    return text
