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
    return cardimg

def paintCards(cards1, cards2, img, img2):
    x1pos = 40
    y1pos = 50
    x2pos = 40
    y2pos = 460
    index1 = 1
    index2 = 1
    global handimg
    handimg = canvas.create_image(655, 310, anchor = NW, image = handcard[0][0])
    global discardimg
    discardimg = canvas.create_image(840, 233, anchor = NW, image = img2)
    canvas.create_text(255, 15, font = "Times 20 bold", anchor = NW, text = "Player One")
    canvas.create_text(255, 425, font = "Times 20 bold", anchor = NW, text = "Player Two")
    global Turnthing
    Turnthing = canvas.create_text(130, 360, font = "Times 30 italic bold", anchor = NW, text = "Player One's Turn")
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
    
def roundover():
    round = False
    cards1complete = True
    cards2complete = True
    for card in cards1:
        if card[2] == False:
            cards1complete = False
    for card in cards2:
        if card[2] == False:
            cards2complete = False
    if cards1complete == True or cards2complete == True:
        round = True
    return round

def clicked(event):
    x1pos = event.x
    y1pos = event.y
    if roundover == True:
        if playeroneturn == True:
            canvas.itemconfig(Turnthing, text = "New Round: Player One's Turn")
        elif playeroneturn == False:
            canvas.itemconfig(Turnthing, text = "New Round: Player Two's Turn")
    x1bounds = 40
    y1bounds = 50
    checkinglist = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    cardcounter = 0
    for card in cards1:
        if checkinglist[cardcounter] in handcard[0][1]:
            if x1pos > x1bounds and y1pos > y1bounds and x1pos < x1bounds+113 and y1pos < y1bounds+157  and playeroneturn == True and cards1[cardcounter][2] == False:
                temp = cards1[cardcounter]
                cards1[cardcounter] = (handcard[0][0], handcard[0][1], True)
                handcard[0] = (temp[0], temp[1], False)
                canvas.itemconfig(handimg, image = handcard[0][0])
                canvas.create_image(x1bounds, y1bounds, anchor = NW, image = cards1[cardcounter][0])
                print("passed")
        cardcounter = cardcounter + 1
        x1bounds = x1bounds + 115
        if cardcounter == 5:
            x1bounds = 40
            y1bounds = y1bounds + 130
    if x1pos > 840 and y1pos > 233 and x1pos < 953 and y1pos < 390:
        canvas.itemconfig(discardimg, image = handcard[0][0])
        
    


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
global discard
discard = []
playeroneturn = True
firsthand = a.getcard(1)
playeronehand = a.getcard(playeronescore)
playertwohand = a.getcard(playertwoscore)
handcard = loadimages(firsthand)
cards1 = loadimages(playeronehand)
cards2 = loadimages(playertwohand)
img = ImageTk.PhotoImage(Image.open("Backofcard.png").resize((113,157)))
img2 = ImageTk.PhotoImage(Image.open("discard.png").resize((113, 157)))
paintCards(cards1, cards2, img, img2)
screen.mainloop()
