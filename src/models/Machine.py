class Machine:

    # Private Atributes
    __name              = ""
    __ip_direction      = ""
    __paths_of_change   = {}
    __paths_of_log      = {}

    def __init__(self, name, ip_direction, paths_of_change, paths_of_log):
        self.__name = name
        self.__ip_direction = ip_direction
        self.__paths_of_change = paths_of_change
        self.__paths_of_log = paths_of_log
    
    def __str__(self):
        return f"{self.__name} with ip '{self.__ip_direction}'"
    
    # Public Methods
    
    
    # Getters/Setters
    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name
    
    def getIpDirection(self):
        return self.__ip_direction
    
    def setIpDirection(self, ip_direction):
        self.__ip_direction = ip_direction
    
    def getPathsOfChange(self):
        return self.__paths_of_change

    def setPathsOfChange(self, paths_of_change):
        self.__paths_of_change = paths_of_change
    
    def getPathsOfLog(self):
        return self.__paths_of_log
    
    def setPathsOfLog(self, paths_of_log):
        self.__paths_of_log = paths_of_log

