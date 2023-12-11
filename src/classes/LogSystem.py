from classes.FileSystem import File
import datetime

# Constants
PATH_LOG = ".\\NSTool.log"

# Class
class Log:
    __LogFile = File(PATH_LOG)

    def __init__(self):
        pass

    def writeLog(self, content):
        self.__LogFile.writeFile(f"{datetime.datetime.now()} | {content}\n")