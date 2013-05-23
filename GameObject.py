import pygame

class GameObject(pygame.sprite.DirtySprite):
    g = 2

    def __init__(self, screen, images, facing, x, y, dx, dy, onGround):
        """C'tor for parent class of the game images.

        @param screen - the PyGame Display object the GameObject will write to.
        @param images - a dictionary of images of the GameObject.
        @param facing - the key for the starting image in the images dictionary
        @param x - the starting X coordinate.
        @param y - the starting Y coordinate.
        @param dx - the starting x motion.
        @param dy - the starting Y motion.
        @param onGround - flag to indicate if the object is on the ground or not. 

        """
        self.screen = screen
        self.images = images
        self.image = images[facing]
        self.rect = self.image.get_rect()
        pygame.sprite.DirtySprite.__init__(self)
        self.rect = self.rect.move(x, y)

        self.vx = dx
        self.vy = dy
        self.direction = facing
        self.onGround = onGround
        


    def move(self, dx = 0, dy = 0):
        """Move the GameObject. 

        This is an 'abstract' method, in that it doesn't implement anything.
        """
        pass
