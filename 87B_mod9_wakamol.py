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
SCORE_FONT = pygame.font.SysFont('comicsans', 40)
#WHACK_SOUND = pygame.mixer.Sound (os.path.join('Assets', 'whack.mp3'))
FPS = 60

AVOCADO_HIT = pygame.USEREVENT +1


display.set_caption("G-wakamole")


class Mole (Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load (os.path.join('Assets', 'avocado.png')).convert()
        self.rect = self.image.get_rect()

    def flee (self):
        self.rect.left = random.randint(0,600)
        self.rect.top =random.randint(0,400)

    def handle_click(self):
        return



class Banner (Sprite):
    def __init__ (self):
        my_font = pygame.font(None, 24)
        self.image = my_font.render("Hello", True, (0,0,0))
        self.rect = self.image.get_rect().move(50,70)




def update(self):
    self.rect = self.rect.move(3,0)


my_mole1 = Mole()
my_mole2 = Mole()
all_sprites = Group(my_mole1, my_mole2)



def draw_window():
    pygame.draw.rect(WIN, WHITE, )
    #surface = pygame.display.set_mode (WIDTH, HEIGHT)

    WIN.fill(WHITE)
    all_sprites.draw(WHITE)
    display.update()



def main():
    #the event loop

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
                


        draw_window()

if __name__ == "__main__":
    main()
    