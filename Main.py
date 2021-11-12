from tkinter import *
from tkinter.constants import NW
import requests
from io import BytesIO
from PIL import Image, ImageTk
from deckmethods import deckmethod

class GUI:
    
    def paintcards(self):
        pass
    def round(self):
        self.playeronehand = a.getcard(playeronescore)
        self.playertwohand = a.getcard(playertwoscore)
        paintcards()

    def display_coordinates(self, event):
        print(f'x={event.x} y={event.y}')

    def main_screen(self):
        global screen
        global canvas
        screen = Tk()
        global a
        a = deckmethod()
        canvas = Canvas(screen, bg ='green', height = 750, width = 1000)
        global playeronehand
        global playertwohand
        global playeronescore
        global playertwoscore
        playeronehand = []
        playertwohand = []
        playeronescore = 10
        playertwoscore = 10
        canvas.bind('<Button-1>', self.display_coordinates)
        canvas.pack()
        round()
        screen.mainloop()

a = GUI()
a.main_screen()