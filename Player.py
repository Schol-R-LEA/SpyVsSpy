from GameObject import GameObject
from sys import exit
import pygame

class Player(GameObject):
    src = "GoodGuy{0}.png"

    def __init__(self, screen):
        images = dict()
 
        for face in ["Front", "Left", "Right"]:
            try:
                images[face] = pygame.image.load(Player.src.format(face))
            except:
                print("Could not load player {0} image".format(face))
                exit(-1)
        
        new_y = screen.get_rect().bottom - images["Front"].get_rect().top
        GameObject.__init__(self, screen, images, "Front", 0, new_y, 0, 0, False)
        


    def move(self, dx, dy):
        """Move the Player. """
        screenRect = self.screen.get_rect()

        self.vx = dx

        if self.rect.left + self.vx < screenRect.left:
            self.vx = screenRect.left + self.rect.left
        elif self.rect.right + self.vx > screenRect.right:
            self.vx = screenRect.right - self.rect.right

        if self.vx == 0:
            self.direction = "Front"
        elif self.vx < 0:
            self.direction = "Left"
        else:
            self.direction = "Right"

        self.image = self.images[self.direction]
                
        
        if not self.onGround:
            self.vy += GameObject.g   
             
            if screenRect.bottom < self.rect.bottom + self.vy:
                self.onGround = True
                self.vy = screenRect.bottom - self.rect.bottom
                
        elif dy < 0:                # jumping
            self.vy = dy
            self.onGround = False
        else:
            self.vy = 0


        if self.vx == 0 and self.vy == 0:
            self.dirty = 0
        else:
            self.rect = self.rect.move(self.vx, self.vy)
            self.dirty = 1
            
