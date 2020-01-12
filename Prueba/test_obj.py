import pygame

width, height = 640, 480

class cuadrado:
    x = 320
    y = 240
    vel = 0.3 # 0.3
    

    def pos(self, x, y):
        self.x = x
        self.y = y
    
    def move(self, boolean):
        if self.x >= -50 and self.x <= width:
            if boolean:
                self.pos(self.x-self.vel, self.y)
            else:
                self.pos(self.x+self.vel, self.y)
        else:
            self.x = width-10 if self.x <= -50 else -40
    
    def vertical_move(self, boolean):
        if self.y >= -50 and self.y <= height:
            if boolean:
                self.pos(self.x, self.y-self.vel)

            else:
                self.pos(self.x, self.y+self.vel)
        else:
            self.y = height-10 if self.y <= -50 else -40

def compruebaTeclasMover(keys):
    if keys[pygame.K_RIGHT]:
        c.move(False)
    if keys[pygame.K_LEFT]:
        c.move(True)
    if keys[pygame.K_UP]:
        c.vertical_move(True)
    if keys[pygame.K_DOWN]:
        c.vertical_move(False)
    if keys[pygame.K_SPACE]:
        c.pos(320, 240)

cuad = pygame.image.load("imgs/25ab.png")
cuad = pygame.transform.scale(cuad, (100, 100))

pygame.init()
screen = pygame.display.set_mode((width, height))
c = cuadrado()

while True:
    screen.fill(0) ##Limpia la pantalla
    screen.blit(cuad, (c.x, c.y))
    pygame.display.flip() ##Actualiza la pantalla
    keys = pygame.key.get_pressed()

    compruebaTeclasMover(keys)
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            