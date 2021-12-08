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
    playeroneturn.append("True")
    global handimg
    handimg = canvas.create_image(655, 310, anchor = NW, image = handcard[0][0])
    global discardimg
    discard.append((img2, "", False))
    discardimg = canvas.create_image(840, 233, anchor = NW, image = img2)
    canvas.create_text(255, 15, font = "Times 20 bold", anchor = NW, text = "Player One")
    canvas.create_text(255, 425, font = "Times 20 bold", anchor = NW, text = "Player Two")
    global Turnthing
    Turnthing = canvas.create_text(100, 360, font = "Times 30 italic bold", anchor = NW, text = "Player One's Turn")
    canvas.create_image(840, 400, anchor = NW, image = img)
    canvas.create_rectangle(840, 233, 953, 390)
    global images1
    global images2 
    images1 = []
    images2 = []
    for card in cards1:
        images1.append(canvas.create_image(x1pos, y1pos, anchor = NW, image = img))
        x1pos = x1pos + 115
        index1 = index1+1
        if index1 == 6:
            y1pos = y1pos + 130
            x1pos = 40
    for card in cards2:
        images2.append(canvas.create_image(x2pos, y2pos, anchor = NW, image = img))
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
def turnover():
    if "True" in playeroneturn[0]:
        playeroneturn[0] = "False"
    elif "False" in playeroneturn[0]:
        playeroneturn[0] = "True"
    if "True" in playeroneturn[0]:
        canvas.itemconfig(Turnthing, text = "Player One's Turn")
    elif "False" in playeroneturn[0]:
        canvas.itemconfig(Turnthing, text = "Player Two's Turn")
    
def loadnewdeck():
    a.getnew()
    newp1 = a.getcard(playeronescore[0])
    new1 = loadimages(newp1)
    newp2 = a.getcard(playertwoscore[0])
    new2 = loadimages(newp2)
    newhand = a.getcard(1)
    han = loadimages(newhand)
    handcard[0] = han[0]
    print(handcard[0])
    print(cards1)
    print(cards2)
    for card in cards1:
        cards1.pop()
    for card in new1:
        cards1.append(card)
    for card in cards2:
        cards2.pop()
    for card in new2:
        cards2.append(card)


def clicked(event):
    x1pos = event.x
    y1pos = event.y
    x1bounds = 40
    y1bounds = 50
    checkinglist = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    cardcounter = 0
    for card in cards1:
        if checkinglist[cardcounter] in handcard[0][1] or "J" in handcard[0][1]:
            if x1pos > x1bounds and y1pos > y1bounds and x1pos < x1bounds+113 and y1pos < y1bounds+157  and "True" in playeroneturn[0] and cards1[cardcounter][2] == False:
                temp = cards1[cardcounter]
                cards1[cardcounter] = (handcard[0][0], handcard[0][1], True)
                handcard[0] = (temp[0], temp[1], False)
                canvas.itemconfig(handimg, image = handcard[0][0])
                canvas.itemconfig(images1[cardcounter], image = cards1[cardcounter][0])
            elif "J" in cards1[cardcounter][1] and x1pos > x1bounds and y1pos > y1bounds and x1pos < x1bounds+113 and y1pos < y1bounds+157  and "True" in playeroneturn[0]:
                temp = cards1[cardcounter]
                cards1[cardcounter] = (handcard[0][0], handcard[0][1], True)
                handcard[0] = (temp[0], temp[1], False)
                canvas.itemconfig(handimg, image = handcard[0][0])
                canvas.itemconfig(images1[cardcounter], image = cards1[cardcounter][0])
        cardcounter = cardcounter + 1
        x1bounds = x1bounds + 115
        if cardcounter == 5:
            x1bounds = 40
            y1bounds = y1bounds + 130
    cardcounter = 0
    x2bounds = 40
    y2bounds = 460
    for card in cards2:
        if checkinglist[cardcounter] in handcard[0][1] or "J" in handcard[0][1]:
            if x1pos > x2bounds and y1pos > y2bounds and x1pos < x2bounds+113 and y1pos < y2bounds+157  and "False" in playeroneturn[0] and cards2[cardcounter][2] == False:
                temp = cards2[cardcounter]
                cards2[cardcounter] = (handcard[0][0], handcard[0][1], True)
                handcard[0] = (temp[0], temp[1], False)
                canvas.itemconfig(handimg, image = handcard[0][0])
                canvas.itemconfig(images2[cardcounter], image = cards2[cardcounter][0])
            elif "J" in cards2[cardcounter][1] and x1pos > x2bounds and y1pos > y2bounds and x1pos < x2bounds+113 and y1pos < y2bounds+157  and "False" in playeroneturn[0]:
                temp = cards2[cardcounter]
                cards2[cardcounter] = (handcard[0][0], handcard[0][1], True)
                handcard[0] = (temp[0], temp[1], False)
                canvas.itemconfig(handimg, image = handcard[0][0])
                canvas.itemconfig(images2[cardcounter], image = cards2[cardcounter][0])
        cardcounter = cardcounter + 1
        x2bounds = x2bounds + 115
        if cardcounter == 5:
            x2bounds = 40
            y2bounds = y2bounds + 130
    if x1pos > 840 and y1pos > 233 and x1pos < 953 and y1pos < 390 and handcard[0][2] == False:
        discard.append(handcard[0])
        canvas.itemconfig(discardimg, image = discard[-1][0])
        handcard[0] = ((ImageTk.PhotoImage(Image.open("Empty.png").resize((113, 157))), "", True))
        canvas.itemconfig(handimg, image = handcard[0][0])
        turnover()
    elif x1pos > 840 and y1pos > 233 and x1pos < 953 and y1pos < 390 and handcard[0][2] == True:
        handcard[0] = discard[-1]
        discard.pop()
        canvas.itemconfig(handimg, image = handcard[0][0])
        canvas.itemconfig(discardimg, image = discard[-1][0])
    if x1pos > 840 and y1pos > 400 and x1pos < 952 and y1pos < 557 and handcard[0][2] == True:
        drawn = a.getcard(1)
        newimage = loadimages(drawn)
        handcard[0] = newimage[0]
        canvas.itemconfig(handimg, image = handcard[0][0])
    roundcheck = roundover()
    if roundcheck == True:
        loadnewdeck()
        playeronescore[0] = playeronescore[0] - 1
        counter = 0
        for im in images1:
            if counter <= playeronescore[0]-1:
                canvas.itemconfig(images1[counter], image = img)
            else:
                canvas.itemconfig(images1[counter], image = img3)
            counter = counter + 1
        counter = 0
        for im in images2:
            if counter <= playertwoscore[0]-1:
                canvas.itemconfig(images2[counter], image = img)
            else:
                canvas.itemconfig(images2[counter], image = img3)
            counter = counter + 1
        for dis in discard:
            discard.pop()
        discard.append((img2, "", False))
        canvas.itemconfig(handimg, image = handcard[0][0])
        canvas.itemconfig(discardimg, image = discard[0][0])
        canvas.itemconfig(Turnthing, text = "New Round: Player One's Turn")
        

        

        
    


global a
a = deckmethod()
global playeronehand
global playertwohand
global playeronescore
global playertwoscore
playeronehand = []
playertwohand = []
playeronescore = [10]
playertwoscore = [10]
canvas.bind('<Button-1>', clicked)
canvas.pack()
global start
global cards1
global cards2
global firsthand
global handcard
global playeroneturn
global discard
global img
global img2
global img3
discard = []
playeroneturn = []
firsthand = a.getcard(1)
playeronehand = a.getcard(playeronescore[0])
playertwohand = a.getcard(playertwoscore[0])
handcard = loadimages(firsthand)
cards1 = loadimages(playeronehand)
cards2 = loadimages(playertwohand)
img = ImageTk.PhotoImage(Image.open("Backofcard.png").resize((113,157)))
img2 = ImageTk.PhotoImage(Image.open("discard.png").resize((113, 157)))
img3 = ImageTk.PhotoImage(Image.open("Empty.png").resize((113, 157)))
paintCards(cards1, cards2, img, img2)
screen.mainloop()
