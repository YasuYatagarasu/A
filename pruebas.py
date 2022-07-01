from tkinter import *


root = Tk()
root.geometry("400x400")

Colores = ["blue", "red", "purple", "green"]
colore = StringVar()
colore.set("blue")
cuadroColor = OptionMenu(root, colore, *Colores)
cuadroColor.pack()

root.mainloop()