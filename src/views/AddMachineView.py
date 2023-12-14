from src.interfaces.IWindow import IWindow
from src.classes.ComponentSystem import Component
from src.models.Machines import Machines
from src.models.Machine import Machine
from tkinter import *

class AddMachineView(IWindow):
    __root = {}

    def __init__(self, root):
        self.__root = root

    # Funciones de la pantalla
    def checkValue(self): # TODO: Necesitamos comprobar que los campos introducidos sean correctos
        pass

    def saveMachine(self, name_machine, ip_machine):
        machines = Machines()
        machines.createMachine(Machine(name_machine, ip_machine))

    # Vista de la pantalla
    def show(self):
        component = Component()

        name_machine = StringVar()
        ip_machine = StringVar()

        component.valueForm(self.__root, "Nombre máquina", name_machine)
        component.valueForm(self.__root, "IP de la máquina", ip_machine)

        component.button(
            self.__root, 
            "Guardar", 
            lambda:self.saveMachine(name_machine.get(), ip_machine.get()))

    