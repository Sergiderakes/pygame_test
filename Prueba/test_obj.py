import pygame
import os
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
            if o.vel_y < 0:
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
        if isinstance(o, (tuple)): # Mouse collision
            if o[0] <= col.x + col.width and o[0]>= col.x and o[1] <= col.y + col.height and o[1] >= col.y:
                return True
            else:
                return False
        else:
            if o.x <= col.x + col.width and o.x + 20 >= col.x and o.y <= col.y + col.height and o.y + 20 >= col.y:
                return True
            else:
                return False

def draw_sqr_black(screen, c):
    screen.blit(sqr_blk, (c.x, c.y))

sqr = pygame.image.load(os.path.join(os.path.dirname(__file__), "imgs", "sqr.png"))
# sqr_blk = pygame.image.load(os.path.join(os.path.dirname(__file__), "imgs", "black_sqr.png"))
sqr = pygame.transform.scale(sqr, (20, 20))
# sqr_blk = pygame.transform.scale(sqr_blk, (20, 20))

pygame.init()
screen = pygame.display.set_mode((width, height))
c = cu.cuadrado(400, 300, width, height, 0.003)
coll1 = cc.colliders(True, 0, 400, 20, 800, screen)
coll2 = cc.colliders(False, 400, 0, 800, 20, screen)
coll3 = cc.colliders(True, 0, 200, 20, 800, screen)
coll4 = cc.colliders(False, 200, 0, 800, 20, screen)
cds_moveables = [c]
colliders_l = [coll1, coll2, coll3, coll4]
for coll in colliders_l:
    # coll.show = False
    coll.draw()
mouse_x = 0
mouse_y = 0
mov = False

while True:
    screen.fill(0) ##Limpia la pantalla
    keys = pygame.key.get_pressed()
    left, center, right = pygame.mouse.get_pressed()
    for a in cds_moveables:
        # draw_sqr_black(screen, a)
        a.move_x()
        a.move_y()
        # print(a.vel_y)
        screen.blit(sqr, (a.x, a.y))
        for coll in colliders_l:
            if coll.show:
                coll.draw()
            collision = check_collision(a, coll)
            while collision:
                collision = check_collision(a, coll)
                collision_handler(a, coll, collision)
        compruebaTeclasMover(keys, a)
    pygame.display.flip() ##Actualiza la pantalla

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONUP:
            left, _, _ = pygame.mouse.get_pressed()
            if not left:
                for coll in colliders_l:
                    coll.clicked = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for coll in colliders_l:
                if check_collision(pos, coll):
                    coll.clicked = True
                    mouse_x = pos[0]
                    mouse_y = pos[1]
                    coll.offset_x = coll.x - mouse_x
                    coll.offset_y = coll.y - mouse_y

        if event.type == pygame.MOUSEMOTION:
            if left:
                for coll in colliders_l:
                    if coll.clicked:
                        pos = pygame.mouse.get_pos()
                        coll.move(pos[0], pos[1])
            