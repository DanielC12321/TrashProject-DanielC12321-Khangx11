import tkinter as tk
from tkinter.constants import NW
import requests
from io import BytesIO
from PIL import Image, ImageTk
from deckmethods import deckmethod
root = tk.Tk()




a = deckmethod()

canvas = tk.Canvas(root, bg ='green', height = 750, width = 1000)

card = a.getcard(1)
url = card[0][1]
response = requests.get(url)
img_data = response.content
img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)).resize((113, 157)))
canvas.pack()
canvas.create_image(15, 15, anchor = NW, image = img)
def round():
    pass
gameover = False
while gameover == False:
    round
    




root.mainloop()
