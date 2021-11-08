import pygame
pygame.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Trash")

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type  == pygame.QUIT:
                run = False
    
    pygame.quit()

if __name__ == "__main__":
    main()
