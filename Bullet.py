from GameObject import GameObject
from sys import exit
import pygame


class Bullet(GameObject):
    src = "Bullet{0}.png"

    def __init__(self, screen, direction, start_x):
        images = dict()
 
        for face in ["Left", "Right"]:
            try:
                images[face] = pygame.image.load(Bullet.src.format(face))
            except:
                print("Could not load bullet {0} image".format(face))
                exit(-1)
        
        new_y = screen.get_rect().bottom - images[direction].get_rect().top - 50
        
        if direction == "Left":
            dx = 15
        else:
            dx = -15
        GameObject.__init__(self, screen, images, direction, start_x, new_y, dx, 0, False)


    def move(self, dx = 0, dy = 0):
        """ Move bullet. """
        screenRect = self.screen.get_rect()

        self.vx += dx
        if ((self.rect.left + self.vx) < screenRect.left) or \
           ((self.rect.right + self.vx) > screenRect.right):
            self.kill()

        if self.onGround:
            self.kill()
        else:   
            if screenRect.bottom < (self.rect.bottom + self.vy):
                self.onGround = True

        self.rect = self.rect.move(self.vx, self.vy)            
      #  print('({0}, {1})'.format(self.vx, self.vy))
