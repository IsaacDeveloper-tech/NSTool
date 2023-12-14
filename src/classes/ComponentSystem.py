from tkinter import *
from src.models.Machine import Machine

class Component:

    def valueForm(self, root, text_label, value):
        frame = Frame(root)
        frame.pack()

        label = Label(frame,text=text_label)
        label.pack(side="left")

        entry = Entry(frame, textvariable=value)
        entry.pack()
    
    def button(self, root, text_button, action):
        frame = Frame(root)
        frame.pack()

        Button(text=text_button, command=action).pack()

    def space(self, root):
        frame = Frame(root, width=100,height=20)
        frame.pack()

    def label(self, root, text_label, align="left"):
        frame = Frame(root)
        frame.pack()

        label = Label(frame,text=text_label)
        label.pack(side=align)

    def machineComponent(self, root, machine:Machine):
        frame = Frame(root)
        frame.pack()

        self.label(frame, machine.getName())
        self.label(frame, machine.getIpDirection())

        self.button(frame, "Editar", lambda:print("Por desarrollar"))
        self.button(frame, "Eliminar", lambda:print("Por desarrollar"))