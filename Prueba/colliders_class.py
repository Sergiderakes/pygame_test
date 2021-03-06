import pygame
import os
import math

class colliders:
    is_horizontal = True
    x = 0
    y = 0
    height = 0
    width = 0
    # HOR_IMG_URL = os.path.join(os.path.dirname(__file__), "imgs", "horizontal_coll.png")
    # VER_IMG_URL = os.path.join(os.path.dirname(__file__), "imgs", "vertical_coll.png")
    show = False
    img = None
    screen = None
    offset_x = 0
    offset_y = 0
    clicked = False


    def __init__(self, is_horizontal, x, y, height, width, screen):
        self.is_horizontal = is_horizontal
        self.x = x
        self.y = y
        if is_horizontal:
            self.width = width if width>height else height
            self.height = width if width<=height else height
        else:
            self.width = width if width<=height else height
            self.height = width if width>height else height
        self.img = pygame.Surface((self.width, self.height))
        self.img.fill((255, 0, 0)) if self.is_horizontal else self.img.fill((0, 0, 255))
        self.screen = screen
    
    def move(self, mouse_x, mouse_y):
        if self.show:
            self.set_pos(self.offset_x + mouse_x, self.offset_y + mouse_y)

    def set_pos(self, x, y):
        self.x = x
        self.y = y
    
    def horizontal(self, is_horizontal):
        self.is_horizontal = is_horizontal
        self.img.fill((255, 0, 0)) if self.is_horizontal else self.img.fill((0, 0, 255))
        if is_horizontal:
            self.height = 20
            self.width = width if width>height else height
        else:
            self.width = 20
            self.height = width if width>height else height

    def set_show(self, is_shown):
        self.show = is_shown
    
    def is_mouse_colliding(self, mouse_pos):
        if isinstance(mouse_pos, tuple):
            if mouse_pos[0] <= self.x + self.width and mouse_pos[0]>= self.x and mouse_pos[1] <= self.y + self.height and mouse_pos[1] >= self.y:
                return True
                
            else:
                return False
        else:
            return False

    def draw(self):
        if self.show:
            self.screen.blit(self.img, (self.x, self.y))
            if self.clicked:
                sup = pygame.Surface((self.width, 2))
                sup.fill((255, 255, 255))
                lef = pygame.Surface((2, self.height))
                lef.fill((255, 255, 255))

                self.screen.blit(sup, (self.x, self.y))
                self.screen.blit(sup, (self.x, self.y + self.height -2)) # inf
                self.screen.blit(lef, (self.x, self.y))
                self.screen.blit(lef, (self.x + self.width -2, self.y)) # rig
    
class circle_collider:
    x = 0
    y = 0
    r = 0
    width = 4
    img = None
    show = False
    screen = None
    offset_x = 0
    offset_y = 0
    clicked = False
    ring = None # When clicked

    def __init__(self, x, y, r, screen):
        self.x = x
        self.y = y
        self.r = r
        self.screen = screen
        self.img = pygame.Surface((2 * self.r, 2 * self.r))
        self.img.set_colorkey((0, 0, 0))
        pygame.draw.circle(self.img, (0, 0, 255), (self.r, self.r), self.r, self.width)
        self.ring = pygame.Surface((2 * self.r, 2 * self.r))
        self.ring.set_colorkey((0, 0, 0))
        pygame.draw.circle(self.ring, (255, 255, 255), (self.r, self.r), self.r, 1)
    
    def set_pos(self, x, y):
        self.x = x
        self.y = y
    
    def move(self, mouse_x, mouse_y):
        if self.show:
            self.set_pos(self.offset_x + mouse_x, self.offset_y + mouse_y)
        
    def draw(self):
        self.screen.blit(self.img, (self.x, self.y))
        if self.clicked:
            self.screen.blit(self.ring, (self.x, self.y))
            
    
    def get_center_pos(self):
        return (self.x + self.r, self.y + self.r)
    
    def is_mouse_colliding(self, mouse_pos):
        if isinstance(mouse_pos, tuple):
            x, y = self.get_center_pos()
            if math.sqrt(((mouse_pos[0] - x) ** 2 + (mouse_pos[1] - y) ** 2)) <= self.r:
                return True
                
            else:
                return False
        else:
            return False

