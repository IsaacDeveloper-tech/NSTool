import json
import os

class File:

    __path = ""

    def __init__(self, path = None):
        if(path == None):
            raise ValueError("No has introducido el path")
        
        if(not os.path.exists(path)):
            file = open(path, "w")
            file.close()

        self.__path = path
    
    def writeFile(self, content = None):

        if(content == None):
            raise ValueError("Falta introducir valor en el 'content'")
        
        file = open(self.__path, "a")

        if(isinstance(content, dict)):
            json.dump(content, file)
        elif(isinstance(content, str)):
            file.write(content)
        else:
            file.close()
            raise ValueError("Tipo del contenido NO COMPATIBLE")
        
        file.close()
    
    def cleanFile(self):
        file = open(self.__path, "w")
        file.write("")
        file.close()

        



