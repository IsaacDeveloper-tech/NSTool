from tkinter import *

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