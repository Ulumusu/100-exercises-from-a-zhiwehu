import pygame, sys
from pygame.locals import*


pygame.init()
DISPlAYSURF=pygame.display.set_mode((400, 300))
pygame.display.set_caption('hello world!')

WHITE=(255,255,255)
GREEN=(0,255,0)
BLUE=(0,0,128)

fontObj=pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj=fontObj.render('hello world!', True, GREEN, BLUE)
textRectObj=textSurfaceObj.get_rect()
textRectObj.center=(200, 150)

soundObj = pygame.mixer.Sound('beeps.wav')
soundObj.play()


# Loading and playing background music:
pygame.mixer.music.load('beeps.wav')
pygame.mixer.music.play(-1, 0.0)
# ...some more of your code goes here...
pygame.mixer.music.stop()



while True: #main game loop
    DISPlAYSURF.fill(WHITE)
    DISPlAYSURF.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()        

