import pygame
import os
width,height=800,600 #width and height

FPS=60 #frames per second, after how long should the game be updating

GScreen=pygame.display.set_mode((width,height))#displaying screen
pygame.display.set_caption("My first python game")#screen name
PICTURE=pygame.image.load(os.path.join('car.jpg'))
SONG=os.path.join(os.getcwd(), 'jaymelo.mp3')

red=(255,255,255)


def draw_fn(): #A function to fill color and updating content
    GScreen.fill((255,255,105)) #Assigning color to the screen
    GScreen.blit(PICTURE,(0,0))
    pygame.display.update()#updating the codes
    

def main():
    pygame.mixer.init()
    pygame.mixer.music.load(SONG)
    pygame.mixer.music.play(-1)
    
    run=True
    clock=pygame.time.Clock() 
    
    while run:
        clock.tick(FPS) #clock updating
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()#quiting the screen
        draw_fn()        
        

if __name__ =="__main__":
    main()
