import pygame, sys
from pygame.locals import*

pygame.init()

#set window
DISPLAYSURF= pygame.display.set_mode((800,600), 0, 32)
pygame.display.set_caption("Drawing")

#set the color
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)

# draw on the surface object
DISPLAYSURF.fill(GREEN)
pygame.draw.rect(DISPLAYSURF, BLUE, (20, 50, 10, 5))
pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50))
pygame.draw.line(DISPLAYSURF, BLUE, (60, 300), (300, 120), 4)
pygame.draw.circle(DISPLAYSURF, BLUE, (60, 50), 20, 0)
pygame.draw.ellipse(DISPLAYSURF, RED, (30, 150, 400, 480), 1)
pixObj = pygame.PixelArray(DISPLAYSURF)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
