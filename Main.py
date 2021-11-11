import pygame
import io
try:
    # Python2
    from urllib2 import urlopen
except ImportError:
    # Python3
    from urllib.request import urlopen

from deckmethods import deckmethod
pygame.init()

WIDTH, HEIGHT = 1200, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Trash")

GREEN = (0, 128, 0)

FPS = 20
RoundOver = True
global playeronehand
global playertwohand


def draw_window():
    WIN.fill(GREEN)
    pygame.display.update()

def draw_cards():
    a = deckmethod()
    playeronehand = a.getCard(10)
    playertwohand = a.getCard(10)
    print(playeronehand)

def draw_allcards():

    for card in playeronehand:
        image_url = card[1]
        image_str = urlopen(image_url).read
        image_file = io.BytesIO(image_str)
        image = pygame.image.load(image_file)
        WIN.blit(image, 40, 40)
        print("drawn")

def main():
    a = deckmethod()
    card = a.getCard(1)
    image_url = card[0][1]
    print(image_url)
    image_str = urlopen(image_url).read
    image_file = io.BytesIO(image_str)
    image = pygame.image.load(image_file)
    WIN.blit(image, 40, 40)
    RoundOver = False
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type  == pygame.QUIT:
                run = False
        if RoundOver == True:
            draw_cards()
            RoundOver = False
        draw_window()
    pygame.quit()

if __name__ == "__main__":
    main()
