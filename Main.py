from tkinter import *
from tkinter.constants import NW
from typing import Tuple
import requests
from io import BytesIO
from PIL import Image, ImageTk
from deckmethods import deckmethod

global screen
global canvas
screen = Tk()
screen.resizable(False, False)
canvas = Canvas(screen, bg ='green', height = 750, width = 1000)

def loadimages(playeronehand):
    cardimg = []
    for card in playeronehand:
        response = requests.get(card[1]+"")
        img_data = response.content
        i = ImageTk.PhotoImage(Image.open(BytesIO(img_data)).resize((113, 157)))
        cardimg.append((i, card[0], False))

def paintCards(cards1, cards2, img):
    x1pos = 40
    y1pos = 50
    x2pos = 40
    y2pos = 460
    index1 = 1
    index2 = 1
    global handimg
    handimg = canvas.create_image(655, 310, anchor = NW, image = handcard[0][0])
    canvas.create_text(255, 15, font = "Times 20 bold", anchor = NW, text = "Player One")
    canvas.create_text(255, 425, font = "Times 20 bold", anchor = NW, text = "Player Two")
    canvas.create_image(840, 400, anchor = NW, image = img)
    canvas.create_rectangle(840, 233, 953, 390)
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
    

def clicked(event):
    x1pos = event.x
    y1pos = event.y
    if x1pos > 40 and y1pos > 50 and x1pos < 153 and y1pos < 207 and playeroneturn == True and "A" in handcard[0][1] and cards1[0][3]:
        temp = cards1[0]
        cards1[0] = handcard[0]
        handcard[0] = temp
        cards1[0][3] = True
        handcard[0][3] = False
        canvas.itemconfig(handimg, image = handcard[0][0])
        canvas.create_image(40, 50, anchor = NW, image = cards1[0][0])
    
    


global a
a = deckmethod()
global playeronehand
global playertwohand
global playeronescore
global playertwoscore
playeronehand = []
playertwohand = []
playeronescore = 10
playertwoscore = 10
canvas.bind('<Button-1>', clicked)
canvas.pack()
global start
global cards1
global cards2
global firsthand
global handcard
global playeroneturn
playeroneturn = True
firsthand = a.getcard(1)
playeronehand = a.getcard(playeronescore)
playertwohand = a.getcard(playertwoscore)
handcard = loadimages(firsthand)
cards1 = loadimages(playeronehand)
cards2 = loadimages(playertwohand)
img = ImageTk.PhotoImage(Image.open("Backofcard.png").resize((113,157)))
paintCards(cards1, cards2, img)
screen.mainloop()
