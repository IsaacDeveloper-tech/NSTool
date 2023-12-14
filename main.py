from tkinter import *
from src.views.AddMachineView import AddMachineView

root = Tk()
root.title("NSTool")
root.geometry("600x400")

ventana = AddMachineView(root)
ventana.show()

# Loop principal para mostrar la ventana
root.mainloop()