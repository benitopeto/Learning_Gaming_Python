import pygame, sys #MODULES that allow function and music
from pygame.locals import * #imports all functions in module pygame

pygame.init()#initializing pygame
DISPLAYSURF = pygame.display.set_mode((500, 400),0,32)#size of screen
pygame.display.set_caption('Hello World!')#title

BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)

pygame.draw.polygon(DISPLAYSURF, RED, ((146, 0), (291, 106), (236, 277),
(56, 277), (0, 106)))
pygame.draw.line(DISPLAYSURF, BLUE, (60, 60), (120, 60), 4)
#pygame.draw.line(DISPLAYSURF, BLUE, (120, 60), (60, 120))
#pygame.draw.line(DISPLAYSURF, BLUE, (60, 120), (120, 120), 4)
#pygame.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20, 0)
#pygame.draw.ellipse(DISPLAYSURF, RED, (300, 250, 40, 80), 1)
#pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50))

pixObj = pygame.PixelArray(DISPLAYSURF)

pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK

while True: # main game loop
    
    for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
    pygame.display.update()

