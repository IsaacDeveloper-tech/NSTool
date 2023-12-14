from src.classes.FileSystem import File
from src.classes.LogSystem import Log, LogTypes
from src.models.Machine import Machine
# TODO: Pasar __machines de Dict a Machine (REPASAR)

MACHINES_FILE = ".\\machines.json"
class Machines:

    __machines = []
    __file = None
    __log = Log()

    def __init__(self):
        self.__file = File(MACHINES_FILE)

        temp_content = ""
        temp_content = self.__file.readFile("text")
        
        if(len(temp_content) == 0):
            self.__file.writeFile([])
        
        # Guardar en objetos Machine
        machines_dict = self.__file.readFile("json")
        
        if(len(self.__machines) == 0):
            for machine in machines_dict:
                self.__machines.append(Machine(machine["name"], machine["ip"]))

    def saveDataMachine(self):
        self.__file.cleanFile()

        machines_dict = []

        for index in range(0, len(self.__machines)):
            machines_dict.append({
                "name": self.__machines[index].getName(),
                "ip" : self.__machines[index].getIpDirection()
            })

        self.__file.writeFile(machines_dict)
        self.__log.writeLog("saveDataMachine: Se han guardado los datos correctamente", LogTypes.INFO)

    def createMachine(self, machine:Machine = None):
        if(machine == None):
            self.__log.writeLog("createMachine: NO se han introducido los parámetros necesarios", LogTypes.ERROR)

        self.__machines.append(machine)
        self.saveDataMachine()

    def updateMachine(self, machine_updated:Machine = None, index:int = None):
        if(machine_updated == None or index == None):
            self.__log.writeLog("updateMachine: NO se han introducido los parámetros necesarios", LogTypes.ERROR)
        
        if(index < 0 or index > len(self.__machines)):
            self.__log.writeLog("updateMachine: Indice erróneo, se sale del array", LogTypes.ERROR)
        
        self.__machines[index] = machine_updated
        self.saveDataMachine()
                
    def deleteMachine(self, index:int = None):
        if(index == None):
            self.__log.writeLog("deleteMachine: NO se han introducido los parámetros necesarios", LogTypes.ERROR)
        
        if(index < 0 or index > len(self.__machines)):
            self.__log.writeLog("deleteMachine: Indice erróneo, se sale del array", LogTypes.ERROR)
        
        self.__machines.pop(index)
        self.saveDataMachine()
        

    def getMachine(self, index:int = None) -> dict:
        if(index == None):
            self.__log.writeLog("getMachine: NO se han introducido los parámetros necesarios", LogTypes.ERROR)
        
        if(index < 0 or index > len(self.__machines)):
            self.__log.writeLog("getMachine: Indice erróneo, se sale del array", LogTypes.ERROR)

        return self.__machines[index]

    def getMachinesByName(self, machine_name:str) -> list:
        machines_found = []

        for machine in self.__machines:
            if machine_name in machine["name"] :
                machines_found.append(machine)
        
        return machines_found

    def getMachines(self) -> list:
        return self.__machines