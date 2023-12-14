from tkinter import *
from src.views.AddMachineView import AddMachineView
from src.views.MainView import MainView

root = Tk()
root.title("NSTool")
root.geometry("600x400")

ventana = MainView(root)
ventana.show()

# Loop principal para mostrar la ventana
root.mainloop()