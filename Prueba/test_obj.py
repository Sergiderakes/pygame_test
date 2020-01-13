import pygame
import cuadrado_class as cu
import colliders_class as cc

width, height = 640, 480

def compruebaTeclasMover(keys, c):
        if keys[pygame.K_RIGHT]:
            c.set_vel_x(1)
        elif keys[pygame.K_d]:
            c.set_vel_x(1)
            
        if keys[pygame.K_LEFT]:
            c.set_vel_x(-1)
        elif keys[pygame.K_a]:
            c.set_vel_x(-1)
            
        if keys[pygame.K_UP]:
            c.jump()
        elif keys[pygame.K_w]:
            c.jump()

        # if keys[pygame.K_DOWN]:
            
        # elif keys[pygame.K_s]:
            

        if keys[pygame.K_SPACE]:
            print("", end = "")
            # c.jump()

def collision_handler(o, col, is_colliding):
    # o.coll = True
    if col.is_horizontal:
        if is_colliding:
            if o.vel_y <= 0:
                a.set_pos(a.x, a.y + 0.15)
            else:
                a.set_pos(a.x, a.y - 0.15)
        else:
            print("Collision detected on (", int(o.x), ", ", int(o.y), ") with horizontal", sep = "")
            if abs(o.vel_y) > 0.2:
                o.set_vel_y(-o.vel_y * 0.6)
            else:
                o.gravedad = False
    else:
        if is_colliding:
            if o.vel_x >= 0:
                a.set_pos(a.x - 0.15, a.y)
            else:
                a.set_pos(a.x + 0.15, a.y)
        else:
            print("Collision detected on (", int(o.x), ", ", int(o.y), ") with vertical", sep = "")
            if abs(o.vel_x) > 0.2:
                o.vel_x = -o.vel_x * 0.6
            else:
                o.vel_x = 0
        

def check_collision(o, col):
    if isinstance(col, cc.colliders) and not isinstance(o, cc.colliders):
        if o.x <= col.x + col.width and o.x + 20 >= col.x and o.y <= col.y + col.height and o.y + 20 >= col.y:
            return True
        else:
            return False

sqr = pygame.image.load("imgs\\sqr.png")
sqr = pygame.transform.scale(sqr, (20, 20))

pygame.init()
screen = pygame.display.set_mode((width, height))
c = cu.cuadrado(0, 0, width, height, 0.003)
coll1 = cc.colliders(True, 0, 400, 20, 800, screen)
coll2 = cc.colliders(False, 400, 0, 800, 20, screen)
cds_moveables = [c]
colliders_l = [coll1, coll2]

while True:
    screen.fill(0) ##Limpia la pantalla
    keys = pygame.key.get_pressed()
    for a in cds_moveables:
        a.move_x()
        a.move_y()
        # print(a.vel_y)
        screen.blit(sqr, (a.x, a.y))
        for coll in colliders_l:
            coll.draw()
            collision = check_collision(a, coll)
            if collision:
                while collision:
                    collision = check_collision(a, coll)
                    collision_handler(a, coll, collision)
        compruebaTeclasMover(keys, a)
    pygame.display.flip() ##Actualiza la pantalla
    

    
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            