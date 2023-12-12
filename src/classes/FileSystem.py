import json
import os

class File:

    __path = ""

    def __init__(self, path = None):
        if(path == None):
            raise ValueError("Error necesitamos PATH")
        
        if(not os.path.exists(path)):
            file = open(path, "w")
            file.close()

        self.__path = path
    
    def writeFile(self, content = None):

        if(content == None):
            raise ValueError("No has introducido el content")
        
        file = open(self.__path, "a")

        if(isinstance(content, dict) or isinstance(content, list)):
            json.dump(content, file)
        elif(isinstance(content, str)):
            file.write(content)
        else:
            file.close()
            raise ValueError("writeFile: El tipo de contenido no es compatible")
        
        file.close()

    def readFile(self, file_type) -> str|list:
        content = ""
        file = open(self.__path, "r")

        if(file_type == "text"):
            content = file.read()
        elif(file_type == "json"):
            content = json.load(file)
        else:
            file.close()
            raise ValueError("readFile: El tipo de fichero no es compatible")
        
        file.close()
        return content
    
    def cleanFile(self):
        file = open(self.__path, "w")
        file.write("")
        file.close()

        



