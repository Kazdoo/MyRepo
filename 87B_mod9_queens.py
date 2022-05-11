from dis import dis
import pygame
import time
import os



gravity = 0.0500

class QueenSprite:
    def __init__ (self, img, target_posn):
        self.image = img
        self.target_posn = target_posn
        (x,y) = target_posn
        self.posn = (x,0)
        self.y_velocity = 0

    def update(self):
        self.y_velocity += gravity
        (x,y) = self.posn
        new_y_pos = y + self.y_velocity
        (target_x, target_y) = self.target_posn
        dist_to_go = target_y - new_y_pos

        if dist_to_go <0 :
            self.y_velocity = -0.65 * self.y_velocity
            new_y_pos = target_y + dist_to_go
        
        self.posn = (x, new_y_pos)
      
    def draw(self, target_surface):
        target_surface.blit (self.image, self.posn)

    def contains_point (self, pt):
    #return True if my sprite rectangle contains point pt

        (my_x, my_y) = self.posn
        my_width     = self.image.get_width()
        my_height    = self.image.get_height()
        (x,y)        = pt
        return (x >= my_x and x <my_x + my_width and
                y >= my_y and y <my_y + my_height)

    def handle_click(self):
        self.y_velocity += -2 #kick it up

class DukeSprite:

    def __init__ (self, img, target_posn):
        self.image = img
        self.posn = target_posn
        self.anim_frame_count = 0 
        self.curr_patch_num = 0
    
    def update(self):
        if self.anim_frame_count >0:
           self.anim_frame_count = (self.anim_frame_count +1) % 60
           self.curr_patch_num = self.anim_frame_count // 6


    def draw (self, target_surface):
        patch_rect = (self.curr_patch_num *50,0,50, self.image.get_height())
        target_surface.blit(self.image, self.posn, patch_rect)
        
    
    def handle_click (self):
        if self.anim_frame_count == 0:
           self.anim_frame_count = 5


    def contains_point (self, pt):
    # Return True if my sprite rectangle contains  pt 
        (my_x, my_y) = self.posn 
        my_width = self.image.get_width()-450
        my_height = self.image.get_height() 
        (x, y) = pt 
        return ( x >= my_x and x < my_x + my_width and 
                 y >= my_y and y < my_y + my_height) 
  



def draw_board(the_board):

    pygame.init()
    my_clock = pygame.time.Clock()
    colors      = [(255,0,0), (0,0,0)]
    n           = len(the_board)
    surface_sz  = 480 #initial size
    sq_sz       = surface_sz // n #how many square can we cut?
    surface_sz  = n * sq_sz #final size
    
    ball        =pygame.transform.scale(pygame.image.load (os.path.join('Assets', 'avocado2.png')), ((surface_sz//n),(surface_sz//n)))
    ball_offset = (sq_sz - ball.get_width())//2

    #load the sprite sheet
    duke_sprite_sheet = pygame.image.load (os.path.join('Assets', 'duke_spritesheet.png'))

    #instantiate 2 dukes instances, put them on the board
    duke1 = DukeSprite(duke_sprite_sheet, (sq_sz*2, 0))
    duke2 = DukeSprite(duke_sprite_sheet, (sq_sz*5, sq_sz))
    
    #add them to the list of sprites which our game loop manages




    surface = pygame.display.set_mode ((surface_sz, surface_sz))

    all_sprites = []

    for (col, row) in enumerate (the_board):
        a_queen = QueenSprite(ball, (col*sq_sz + ball_offset, row*sq_sz + ball_offset))
        all_sprites.append(a_queen)
    
    all_sprites.append(duke1)
    all_sprites.append(duke2)

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break;
        if ev.type == pygame.KEYDOWN:
            key = ev.dict ["key"]
            if key == 27: #escape key
                break
            if key == ord ("r"): 
                colors[0] = (255,0,0) #change colors red + black
            elif key == ord ("g"):
                colors[0] = (0,255,0) #change colors green + black
            elif key == ord ("b"):
                colors[0] = (0,0,255) #change colors blue + black

        if ev.type == pygame.MOUSEBUTTONDOWN:
            posn_of_click = ev.dict ["pos"]
            for sprite in all_sprites:
                if sprite.contains_point (posn_of_click):
                    sprite.handle_click()
                    break


        for sprite in all_sprites:
            sprite.update()

        for row in range (n):
            c_indx = row %2 # will flip each line
            for col in range(n):
                the_square =  (col* sq_sz, row*sq_sz, sq_sz, sq_sz)
                surface.fill(colors[c_indx], the_square)

                c_indx = (c_indx+1)%2 #flip the color for next square

        for sprite in all_sprites:
            sprite.draw(surface)

        #draw a queen at col, row
        # for (col, row) in enumerate (the_board):
        #     surface.blit(ball, (col*sq_sz+ball_offset, row*sq_sz+ball_offset))
        my_clock.tick(60)  # Waste time so that frame rate becomes 60 fps 
        pygame.display.flip()

    pygame.quit()

    # def main():
    #     main_surface = pygame.display.set_mode((480,240))  
    #     my_font = pygame.font.SysFont("Courier", 16) 
        
    #     main()
    
    
    
if __name__ == "__main__":
    draw_board([0, 5, 3, 1, 6, 4, 2])    # 7 x 7 to test window size 
    #draw_board([6, 4, 2, 0, 5, 7, 1, 3]) 
    #draw_board([9, 6, 0, 3, 10, 7, 2, 4, 12, 8, 11, 5, 1])  # 13 x 13 
    #draw_board([11, 4, 8, 12, 2, 7, 3, 15, 0, 14, 10, 6, 13, 1, 5, 9])
    