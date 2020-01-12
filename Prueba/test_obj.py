import pygame
import cuadrado_class as cu

width, height = 640, 480

def compruebaTeclasMover(keys, c):
    if keys[pygame.K_RIGHT]:
        c.move(False)
    elif keys[pygame.K_d]:
        c.move(False)
        
    if keys[pygame.K_LEFT]:
        c.move(True)
    elif keys[pygame.K_a]:
        c.move(True)
        
    if keys[pygame.K_UP]:
        c.vertical_move(True)
    elif keys[pygame.K_w]:
        c.vertical_move(True)

    # if keys[pygame.K_DOWN]:
    #     c.vertical_move(False)
    # elif keys[pygame.K_s]:
    #     c.vertical_move(False)

    if keys[pygame.K_SPACE]:
        print("", end = "")
        # c.jump()

def comprobar_colision(c, c1):
    if not c == c1:
        # print(c.x, c.y, "/", c1.x, c1.y)
        if c.x <= c1.x + 20 and c.x + 19 > c1.x and c.y <= c1.y + 20 and c.y + 19 > c1.y:
            return True
        else:
            return False
    else:
        return False

cuad = pygame.image.load("Prueba\\imgs\\cuad.png")
cuad = pygame.transform.scale(cuad, (20, 20))

pygame.init()
screen = pygame.display.set_mode((width, height))
c = cu.cuadrado(0, 0, width, height, 0.3)
c1 = cu.cuadrado(320, 240, width, height, 0)
c2 = cu.cuadrado(350, 240, width, height, 0)
c3 = cu.cuadrado(380, 240, width, height, 0)
c4 = cu.cuadrado(410, 240, width, height, 0)
c5 = cu.cuadrado(440, 240, width, height, 0)
cds = [c, c1, c2, c3, c4, c5]

while True:
    colision = False
    screen.fill(0) ##Limpia la pantalla
    keys = pygame.key.get_pressed()
    for a in cds:
        a.pos(a.x, a.y+a.vel/2)
        screen.blit(cuad, (a.x, a.y))
        for b in cds:
            if not a == b:
                colision = comprobar_colision(a, b)
                if colision:
                    a.is_colliding = True
                    a.pos1(a.x_ant, a.y_ant)
        compruebaTeclasMover(keys, a)
    pygame.display.flip() ##Actualiza la pantalla
    

    
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            