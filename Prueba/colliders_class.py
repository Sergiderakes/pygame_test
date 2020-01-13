import pygame

class colliders:
    is_horizontal = True
    x = 0
    y = 0
    height = 0
    width = 0
    HOR_IMG_URL = "imgs\\horizontal_coll.png"
    VER_IMG_URL = "imgs\\vertical_coll.png"
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
        self.img = pygame.image.load(self.HOR_IMG_URL) if self.is_horizontal else pygame.image.load(self.VER_IMG_URL)
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        self.screen = screen
    
    def move(self, mouse_x, mouse_y):
        self.set_pos(self.offset_x + mouse_x, self.offset_y + mouse_y)

    def set_pos(self, x, y):
        self.x = x
        self.y = y
    
    def horizontal(self, is_horizontal):
        self.is_horizontal = is_horizontal
        self.img = pygame.image.load(self.HOR_IMG_URL) if self.is_horizontal else pygame.image.load(self.VER_IMG_URL)
        self.img = pygame.transform.scale(self.img, (self.width, self.height))

    def set_show(self, is_shown):
        self.show = is_shown

    def draw(self):
        if self.show:
            self.screen.blit(self.img, (self.x, self.y))