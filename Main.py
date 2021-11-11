from tkinter import *
from tkinter import ttk
import tkinter

from deckmethods import deckmethod
root = tkinter.Tk()




a = deckmethod()

canvas = tkinter.Canvas(root, bg ='green', height = 750, width = 1000)




canvas.pack()
root.mainloop()
