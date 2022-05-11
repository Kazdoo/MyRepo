import sys
import os
import pygame
import random
from pygame import *
from pygame.locals import *
from pygame.sprite import *

#yoyo


WIDTH = 1024
HEIGHT = 768
SCREEN = (255,255,255)

display.set_caption("wakamole")
screen = display.set_mode ((WIDTH, HEIGHT)) # a surface


class Mole (Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load (os.path.join('Assets', 'avocado.png')).convert()
        self.rect = self.image.get_rect()


class Banner (Sprite):
    def __init__ (self):
        my_font = pygame.font(None, 24)
        self.image = my_font.render("Hello", True, (0,0,0))
        self.rect = self.image.get_rect().move(50,70)


def flee (self):
    self.rect.left = random.randint(0,600)
    self.rect.top =random.randint(0,400)

def update(self):
    self.rect = self.rect.move(3,0)


my_mole1 = Mole()
my_mole2 = Mole()
all_sprites = Group(my_mole1, my_mole2)





def main():
    #the event loop

    pygame.init()

    while True:
        e = event.wait()
        if e.type == QUIT:
            pygame.quit()
            break
        elif e.type == MOUSEBUTTONDOWN:
            if my_mole1.rect.collidepoint (mouse.get_pos()):
                my_mole1.flee()
            
            screen.fill(SCREEN)
            all_sprites.draw(SCREEN)
        display.update()


if __name__ == "__main__":
    main()
    