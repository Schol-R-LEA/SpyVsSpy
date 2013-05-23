import pygame

class GameObject(Object):
    g = 2

    def __init__(self, front_img, left_img, right_img, dx, dy, onGround):
        """C'tor for parent class of the characters."""
        self.image_front = front_img
        self.image_left = left_img
        self.image_right = right_img
        self.position = self.image_front.get_rect().move(0, height)
        self.saved_bg = None
        self.vx = dx
        self.vy = dy
        self.curr_dx = 0
        self.onGround = onGround
        

    def move(dx, dy, floor, screen):
        """  """
        self.clear(screen)
    
        if not onGround:          
            self.vy += g
            self.y += self.vy
            if self.y >= floor:
                self.onGround = True
                self.y = floor
                self.vy = 0
                self.positionx += self.curr_dx 
        else:
            if dy < 0:                # jumping
                self.vy = dy
                self.y += self.vy

            self.vx = self.curr_dx = dx
            self.x += vx
        
        self.show(screen)
                                

        
    def clear(self, screen):
        """   """
        if self.saved_bg is not None:
            screen.blit(self.saved_bg, (self.position, self.position))
            

    def show(self, screen):
        """ """
        if dx == 0:
            curr_image = self.image_front
        elif dx < 0:
            curr_image = self.image_left
        else:
            curr_image = self.image_right

        self.position = self.position.move(self.vx, self.vy)
        self.saved_bg = 
