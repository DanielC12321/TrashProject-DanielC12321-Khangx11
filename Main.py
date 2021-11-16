from tkinter import *
from tkinter.constants import NW
import requests
from io import BytesIO
from PIL import Image, ImageTk
from deckmethods import deckmethod

class GUI:

    def loadimages(self, playeronehand):
        cardimg = []
        for card in playeronehand:
            response = requests.get(card[1]+"")
            img_data = response.content
            i = ImageTk.PhotoImage(Image.open(BytesIO(img_data)).resize((113, 157)))
            cardimg.append((i, card[0]))
        return cardimg
    def paintCards(self, cards1, cards2, img):
        x1pos = 40
        y1pos = 50
        x2pos = 40
        y2pos = 460
        index1 = 1
        index2 = 1
        for card in cards1:
            canvas.create_image(x1pos, y1pos, anchor = NW, image = img)
            x1pos = x1pos + 115
            index1 = index1+1
            if index1 == 6:
                y1pos = y1pos + 130
                x1pos = 40
        for card in cards2:
            canvas.create_image(x2pos, y2pos, anchor = NW, image = img)
            x2pos = x2pos + 115
            index2 = index2+1
            if index2 == 6:
                y2pos = y2pos + 130
                x2pos = 40

    def display_coordinates(self, event):
        print(f'x={event.x} y={event.y}')

    def main_screen(self):
        global screen
        global canvas
        screen = Tk()
        screen.resizable(False, False)
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
        gameover = False
        while gameover == False:
            playeronehand = a.getcard(playeronescore)
            playertwohand = a.getcard(playertwoscore)
            cards1 = self.loadimages(playeronehand)
            cards2 = self.loadimages(playertwohand)
            img = ImageTk.PhotoImage(Image.open("Backofcard.png").resize((113,157)))
            self.paintCards(cards1, cards2, img)
            gameover = True
        print("passed")
        screen.mainloop()

a = GUI()
a.main_screen()