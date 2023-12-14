from src.classes.ComponentSystem import Component
from src.interfaces.IWindow import IWindow
from src.models.Machines import Machines

from tkinter import *

class MainView(IWindow):
    __root = {}
    __all_machines = {}

    def __init__(self, root):
        self.__root = root

        machines = Machines()
        self.__all_machines = machines.getMachines()

    # Funciones de la pantalla

    # Vista de la pantalla
    def show(self):
        component = Component()

        component.space(self.__root)

        name_machine = StringVar()
        component.valueForm(self.__root, "Buscar Máquina: ", name_machine)

        component.space(self.__root)

        for machine in self.__all_machines:
            component.machineComponent(self.__root, machine)
            component.space(self.__root)
        
        component.space(self.__root)
        component.button(self.__root, "Añadir Máquina", lambda:print("Por desarrollar"))