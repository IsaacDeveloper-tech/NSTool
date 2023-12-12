class Machine:
    
    # Private atributes
    __name:str
    __ip_direction:str

    def __init__(self, name, ip_direction):
        self.__name         = name
        self.__ip_direction = ip_direction

    # Public methods

    # Getters/Setters
    def getName(self):
        return self.__name
    def setName(self, name):
        self.__name = name
    
    def getIpDirection(self):
        return self.__ip_direction
    def setIpDirection(self, ip_direction):
        self.__ip_direction = ip_direction

