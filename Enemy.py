from GameObject import GameObject
from Bullet import Bullet
from sys import exit
import pygame

class Enemy(GameObject):

    src = "Boss{0}.png"

    def __init__(self, screen):
        images = dict()
 
        for face in ["Left", "Right"]:
            try:
                images[face] = pygame.image.load(Enemy.src.format(face))
            except:
                print("Could not load enemy {0} image".format(face))
                exit(-1)


        screenRect = screen.get_rect()
        imgRect = images["Right"].get_rect()
        new_x = screenRect.right - imgRect.right - 5
        new_y = screenRect.bottom - imgRect.bottom
            
        GameObject.__init__(self, screen, images, "Right", new_x, new_y, -1, 0, False)
        self.dirty = 2


    def move(self, dx = 0, dy = 0):
        """ Move the enemy. """
        screenRect = self.screen.get_rect()
        self.vx += dx

        if ((self.rect.left + self.vx) < screenRect.left) or \
           ((self.rect.right + self.vx) > screenRect.right):
            self.vx = -self.vx

        if self.vx < 0:
            self.direction = "Right"
        else:
            self.direction = "Left"
        self.image = self.images[self.direction]
        
        if self.onGround:
            self.vy = 0
        else:
            self.vy += GameObject.g   
            if screenRect.bottom < (self.rect.bottom + self.vy):
                self.onGround = True
                self.vy = screenRect.bottom - self.rect.bottom
        self.rect = self.rect.move(self.vx, self.vy)


    def seesTarget(self, target):
        """ Detect a target to fire at. """
        if (self.image == self.images["Left"]) and \
           (self.rect.right < target.rect.left):
            return True
        elif (self.image == self.images["Right"]) and \
             (self.rect.left > target.rect.right):
            return True
        else:
            self.vx = -self.vx
            return False


    def fire(self):
        """ Fire at a target. """
        if self.direction == "Left":
            x = self.rect.right
        else:
            x = self.rect.left

        return Bullet(self.screen, self.direction, x)
