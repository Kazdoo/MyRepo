"""
Program: Multiplayer Whack A Mole Game

Player Avocado can move the avocado sprite around.
Player 2 can whack it with the mouse.

Date: 5/13/2022
Coder: @Olivier Ged
"""


import sys
import os
from matplotlib.style import available
import pygame
import random
from pygame import *
from pygame.locals import *
from pygame.sprite import *
pygame.mixer.init()
pygame.font.init()

#creating a lot of global variables to be able to easily change the difficulty of the game
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption ("Guack me if you can")
FPS = 120
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'background.png')), (WIDTH, HEIGHT))

VEL = 3 #velocity for player movement.
HIT_SOUND =  pygame.mixer.Sound (os.path.join('Assets', 'splooge.wav')) #what does a whack avocado sounds like?

PLAYER_WIDTH, PLAYER_HEIGHT = 100,100
AVOCADO_IMAGE =pygame.image.load (os.path.join('Assets', 'avo.png'))
AVOCADO = pygame.transform.scale(AVOCADO_IMAGE, (PLAYER_WIDTH,PLAYER_HEIGHT))

#this is for the scoring system
WHACK = pygame.USEREVENT +1
SCORE_FONT = pygame.font.SysFont('comicsans', 40)
SCORE = 0


class Player (Sprite):
    def __init__(self,img,x,y):
        Sprite.__init__(self)
        self.image = img
        self.x = x
        self.y = y
        self.posn = (x,y)
        self.rect = self.image.get_rect()

     

    def draw(self, target_surface):
        target_surface.blit (self.image, self.posn)

    def handle_click(self):

        #if avocado is clicked, we move it to a random position, play a sound and increase score by 1
        x = random.randint(0,WIDTH-PLAYER_WIDTH)
        y = random.randint(0,HEIGHT-PLAYER_HEIGHT)        
        self.posn = (x,y)
        pygame.event.post(pygame.event.Event(WHACK))
        HIT_SOUND.play()
   
    def contains_point (self, pt):
    #return True if my sprite rectangle contains point pt
        (my_x, my_y) = self.posn
        my_width     = self.image.get_width()
        my_height    = self.image.get_height()
        (x,y)        = pt
        return (x >= my_x and x <my_x + my_width and
                y >= my_y and y <my_y + my_height)

    def move(self, delta_x , delta_y):
        
        new_x = self.posn[0] + delta_x
        new_y = self.posn[1] + delta_y
        
        #containing avocadco within the border of the screen
        if new_x < 0:
            new_x = 0
        if new_x > WIDTH - PLAYER_WIDTH:
            new_x = WIDTH - PLAYER_WIDTH

        if new_y < 0:
            new_y = 0
        if new_y > HEIGHT-PLAYER_HEIGHT:
            new_y = HEIGHT-PLAYER_HEIGHT

        self.posn = (new_x, new_y)
    
    
def avocado_handle_movement(keys_pressed, avocado):
    #This function is for the avocado player to move around.

        if keys_pressed[pygame.K_a]: #this is left
            avocado.move(-VEL,0) 
        if keys_pressed[pygame.K_d]: #this is right
            avocado.move(VEL,0) 
        if keys_pressed[pygame.K_w]: #this is up
            avocado.move(0,-VEL) 
        if keys_pressed[pygame.K_s]: #this is down
            avocado.move(0,VEL)


def score_update (score):
    score_text = SCORE_FONT.render("Whack O Meter:" + str (score), 1, (255,255,255))
    WIN.blit(score_text, (10,10))
    
 


def main():
    
    all_sprites = []
    clock = pygame.time.Clock()
    score = 0


    #creating the avocado player and giving it a starting position
    avocado = Player (AVOCADO, 300, 300)
    all_sprites.append(avocado)

   
    run = True
    while run:
    
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        
            WIN.blit(BACKGROUND, (0,0))
            

            #player 2 is trying to whack player 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                posn_of_click = event.dict ["pos"]
                for sprite in all_sprites:
                    if sprite.contains_point (posn_of_click):
                        sprite.handle_click()
                        score += 1
                        
                        break
            
            score_update(score)

            for sprite in all_sprites:
                sprite.draw(WIN)

        #this function is called repeatidly for avocado movement.
        keys_pressed = pygame.key.get_pressed()
        avocado_handle_movement(keys_pressed, avocado)        

        pygame.display.flip() 

    main()

if __name__ == "__main__":
    main()
    