import pygame
import cuadrado_class as cu

width, height = 640, 480

def compruebaTeclasMover(keys, c, colision):
    if not colision:
        if keys[pygame.K_RIGHT]:
            c.vel_x = 1
        # elif keys[pygame.K_d]:
            
            
        # if keys[pygame.K_LEFT]:
           
        # elif keys[pygame.K_a]:
            
            
        # if keys[pygame.K_UP]:
            
        # elif keys[pygame.K_w]:
            

        # if keys[pygame.K_DOWN]:
            
        # elif keys[pygame.K_s]:
            

        if keys[pygame.K_SPACE]:
            print("", end = "")
            # c.jump()

def comprobar_colision(c, c1):
    if not c == c1:
        # print(c.x, c.y, "/", c1.x, c1.y)
        if c.x <= c1.x + 20 and c.x + 19 >= c1.x and c.y <= c1.y + 20 and c.y + 19 >= c1.y:
            return True
        else:
            return False
    else:
        return False

cuad = pygame.image.load("Prueba\\imgs\\cuad.png")
cuad = pygame.transform.scale(cuad, (20, 20))

pygame.init()
screen = pygame.display.set_mode((width, height))
c = cu.cuadrado(0, 0, width, height, 0.003)
c1 = cu.cuadrado(320, 240, width, height, 0)
c2 = cu.cuadrado(340, 240, width, height, 0)
c3 = cu.cuadrado(360, 240, width, height, 0)
c4 = cu.cuadrado(380, 240, width, height, 0)
c5 = cu.cuadrado(400, 240, width, height, 0)
cds_moveables = [c]
cds_not_moveables = [cu.cuadrado(x*20, 400, width, height, 0) for x in range(-20, int(width/20))]

while True:
    screen.fill(0) ##Limpia la pantalla
    keys = pygame.key.get_pressed()
    for a in cds_moveables:
        a.move_x()
        a.set_pos(a.x, a.y+0.15)
        screen.blit(cuad, (a.x, a.y))
        for nm in cds_not_moveables:
            screen.blit(cuad, (nm.x, nm.y))
            collision = comprobar_colision(a, nm)
            while collision:
                a.coll = True
                a.set_pos(a.x, a.y-0.15)
                collision = comprobar_colision(a, nm)
            a.coll = False
        compruebaTeclasMover(keys, a, False)
    pygame.display.flip() ##Actualiza la pantalla
    

    
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            