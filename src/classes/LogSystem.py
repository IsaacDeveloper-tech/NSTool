from classes.FileSystem import File
import datetime

# Constants
PATH_LOG = ".\\NSTool.log"

# Log types
class LogTypes:
    INFO    = "INFO"
    WARNING = "WARNING"
    ERROR   = "ERROR"
    DEBUG   = "DEBUG"

# Class
class Log:
    __LogFile = File(PATH_LOG)

    def __init__(self):
        pass

    def writeLog(self, content, type_log):
        self.__LogFile.writeFile(f"{datetime.datetime.now()} | [{type_log}] | {content}\n")

        if(type_log == LogTypes.ERROR):
            raise Exception(content)
