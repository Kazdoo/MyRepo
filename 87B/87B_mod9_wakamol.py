import sys
import os
import pygame
import random
from pygame import *
from pygame.locals import *
from pygame.sprite import *
pygame.font.init()
pygame.mixer.init()

WIDTH = 900
HEIGHT = 500
WHITE = (255,255,255)
WIN = pygame.display.set_mode ((WIDTH, HEIGHT)) # a surface
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'background.png')), (WIDTH, HEIGHT))
BORDER = pygame.Rect(WIDTH, 0, 10, HEIGHT)
FPS = 60

#SCORE_FONT = pygame.font.SysFont('comicsans', 40)
#WHACK_SOUND = pygame.mixer.Sound (os.path.join('Assets', 'whack.mp3'))
#AVOCADO_HIT = pygame.USEREVENT +1

AVOCADO_WIDTH, AVOCADO_HEIGHT = 50,40
AVOCADO_IMAGE = image.load (os.path.join('Assets', 'avocado.png'))
AVOCADO = pygame.transform.scale(AVOCADO_IMAGE, (AVOCADO_WIDTH,AVOCADO_HEIGHT))

    

display.set_caption("G-wakamole")


class Mole (Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load(os.path.join('Assets', 'avocado.png'))
        self.rect = self.image.get_rect()

    def flee (self):
        self.rect.left = random.randint(0,WIDTH)
        self.rect.top =random.randint(0,HEIGHT)

    def handle_click(self):
        return


class Banner (Sprite):
    def __init__ (self):
        my_font = pygame.font(None, 24)
        self.image = my_font.render("Hello", True, (0,0,0))
        self.rect = self.image.get_rect().move(50,70)




def main():
    #the event loop
    pygame.init()

    #instantiate 2 mules instances, put them on the board
    my_mole1 = Mole()
    my_mole2 = Mole()
    all_sprites = Group(my_mole1, my_mole2)
    
    
    WIN.blit(BACKGROUND, (0,0))
    pygame.draw.rect(WIN, WHITE, BORDER)
    #surface = pygame.display.set_mode (WIDTH, HEIGHT)




    for sprite in all_sprites:
        sprite.draw(WIN)        

    


    display.update()


    pygame.init()

    score = 0

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()


            if event.type == MOUSEBUTTONDOWN:
                if my_mole1.rect.collidepoint (mouse.get_pos()):
                    my_mole1.flee()
                    score += 1
                    #SOUND.play()
                


        #draw_window()

if __name__ == "__main__":
    main()
    