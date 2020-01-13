import pygame
import os

class colliders:
    is_horizontal = True
    x = 0
    y = 0
    height = 0
    width = 0
    # HOR_IMG_URL = os.path.join(os.path.dirname(__file__), "imgs", "horizontal_coll.png")
    # VER_IMG_URL = os.path.join(os.path.dirname(__file__), "imgs", "vertical_coll.png")
    show = True
    img = None
    screen = None
    offset_x = 0
    offset_y = 0
    clicked = False


    def __init__(self, is_horizontal, x, y, height, width, screen):
        self.is_horizontal = is_horizontal
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.img = pygame.Surface((width, height))
        self.img.fill((255, 0, 0)) if self.is_horizontal else self.img.fill((0, 0, 255))
        self.screen = screen
    
    def move(self, mouse_x, mouse_y):
        self.set_pos(self.offset_x + mouse_x, self.offset_y + mouse_y)

    def set_pos(self, x, y):
        self.x = x
        self.y = y
    
    def horizontal(self, is_horizontal):
        self.is_horizontal = is_horizontal
        self.img.fill((255, 0, 0)) if self.is_horizontal else self.img.fill((0, 0, 255))

    def set_show(self, is_shown):
        self.show = is_shown

    def draw(self):
        if self.show:
            self.screen.blit(self.img, (self.x, self.y))
            if self.clicked:
                sup = pygame.Surface((self.width, 2))
                sup.fill((255, 255, 255))
                lef = pygame.Surface((2, self.height))
                lef.fill((255, 255, 255))

                self.screen.blit(sup, (self.x, self.y))
                self.screen.blit(sup, (self.x, self.y + self.height)) # inf
                self.screen.blit(lef, (self.x, self.y))
                self.screen.blit(lef, (self.x + self.width, self.y)) # rig