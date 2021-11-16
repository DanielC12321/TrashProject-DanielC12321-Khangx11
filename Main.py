from tkinter import *
from tkinter.constants import NW
import requests
from io import BytesIO
from PIL import Image, ImageTk
from deckmethods import deckmethod

class GUI:

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
        playeronehand = a.getcard(playeronescore)
        response = requests.get(playeronehand[0][1]+"")
        img_data = response.content
        i = ImageTk.PhotoImage(Image.open(BytesIO(img_data)).resize((113, 157)))
        spots = []
        playeronehand = a.getcard(playeronescore)
        playertwohand = a.getcard(playertwoscore)
        x1pos = 100
        y1pos = 50
        index = 1
        
        print("passed")
        screen.mainloop()

a = GUI()
a.main_screen()