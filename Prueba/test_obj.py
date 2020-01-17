import pygame
import os
import cuadrado_class as cu
import colliders_class as cc
import time

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

# def collision_handler(o, col, is_colliding):
#     # o.coll = True
#     if col.is_horizontal:
#         if is_colliding:
#             if o.vel_y < 0:
#                 a.set_pos(a.x, a.y + 0.15)
#             else:
#                 a.set_pos(a.x, a.y - 0.15)
#         else:
#             # print("Collision detected on (", int(o.x), ", ", int(o.y), ") with horizontal", sep = "")
#             if abs(o.vel_y) > 0.2:
#                 o.set_vel_y(-o.vel_y * 0.6)
#             else:
#                 o.gravedad = False
#     else:
#         if is_colliding:
#             if o.vel_x >= 0:
#                 a.set_pos(a.x - 0.15, a.y)
#             else:
#                 a.set_pos(a.x + 0.15, a.y)
#         else:
#             # print("Collision detected on (", int(o.x), ", ", int(o.y), ") with vertical", sep = "")
#             if abs(o.vel_x) > 0.2:
#                 o.vel_x = -o.vel_x * 0.6
#             else:
#                 o.vel_x = 0
        

# def check_collision(mouse, col):
#     if isinstance(col, cc.colliders) and not isinstance(mouse, cc.colliders):
#         if isinstance(mouse, (tuple)): # Mouse collision
#             if mouse[0] <= col.x + col.width and mouse[0]>= col.x and mouse[1] <= col.y + col.height and mouse[1] >= col.y:
#                 return True
#             else:
#                 return False

sqr = pygame.image.load(os.path.join(os.path.dirname(__file__), "imgs", "sqr.png"))
sqr = pygame.transform.scale(sqr, (20, 20))

pygame.init()
screen = pygame.display.set_mode((width, height))
c = cu.cuadrado(400, 300, width, height, 0.003, screen)
coll1 = cc.colliders(True, 0, 400, 20, 800, screen)
coll2 = cc.colliders(False, 400, 0, 800, 20, screen)
coll3 = cc.colliders(True, 0, 200, 20, 800, screen)
coll4 = cc.colliders(False, 200, 0, 800, 20, screen)
# c.show_colliders(True)
circle = cc.circle_collider(100, 100, 30, screen)
cds_moveables = [c]
colliders_l = [coll1, coll2, coll3, coll4, circle]
drawble = cds_moveables + colliders_l
for coll in colliders_l:
    coll.show = True
    coll.draw()
mouse_x = 0
mouse_y = 0
mov = False

i = 0
t = 0
t1 = 0

while True:
    t_inicial = time.time()
    keys = pygame.key.get_pressed()
    left, center, right = pygame.mouse.get_pressed()
    
    for a in cds_moveables:
        # s = pygame.Surface((120, 100))
        # pygame.draw.circle(s, (0, 0, 255), (60, 60), 60, 2)
        # screen.blit(s, (0, 150))
        x, y = a.x, a.y
        a.move_x()
        a.move_y()
        for coll in colliders_l:
            if not isinstance(coll, cc.circle_collider):
                if coll.show:
                    a.collision_handler(coll)
            # collision = check_collision(a, coll)
            # while collision:
            #     collision = check_collision(a, coll)
            #     collision_handler(a, coll, collision)
        compruebaTeclasMover(keys, a)
    

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
            clicking = False
            for coll in colliders_l[::-1]:
                if coll.is_mouse_colliding(pos) and not clicking:
                    coll.clicked = True
                    clicking = True
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
    t_final = time.time()
    t = t + t_final - t_inicial
    t1 = t1 + t_final - t_inicial
    if t >= 1 / 60:
        i+=1
        # if i % 60 == 0:
            # print(i, "imgs: ", int(t1), "s", sep = "")
        screen.fill(0) ##Limpia la pantalla
        titl = "pygame_test | fps: {0:.2f}".format(i / t1)
        pygame.display.set_caption(titl)
        for dr in drawble:
            dr.draw()
        pygame.display.flip() ##Actualiza la pantalla
        t = 0


    
            