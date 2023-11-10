import pygame,sys
from pygame.locals import *

pygame.init()

screen=pygame.display.set_mode((400,300))
#SETTING UP THE COLORS
blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)

pygame.display.set_caption("Ben's Game")
screen.fill(blue)

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        
    
        pygame.display.update()            
    
