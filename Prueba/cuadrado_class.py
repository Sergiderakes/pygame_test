import colliders_class as cc
import pygame
import os

class cuadrado:
    x = 320
    y = 240
    width = 0
    height = 0
    vel_x = 0
    vel_y = 0
    # coll = False
    vel = 0
    # tick_count = 0
    right_coll = None
    left_coll = None
    top_coll = None
    bot_coll = None
    screen = None
    sqr = pygame.image.load(os.path.join(os.path.dirname(__file__), "imgs", "sqr.png"))

    
    def __init__(self,x ,y, width, height, vel, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.screen = screen
        tam_sqr = 20
        collider_bars_width = 2
        self.right_coll = cc.colliders(False, self.x + tam_sqr - collider_bars_width, self.y, tam_sqr, collider_bars_width, self.screen)
        self.left_coll = cc.colliders(False, self.x, self.y, tam_sqr, collider_bars_width, self.screen)
        self.top_coll = cc.colliders(True, self.x, self.y, collider_bars_width, tam_sqr, self.screen)
        self.bot_coll = cc.colliders(True, self.x, self.y + tam_sqr - collider_bars_width, collider_bars_width, tam_sqr, self.screen)
        self.sqr = pygame.transform.scale(self.sqr, (20, 20))

    def show_colliders(self, show):
        self.right_coll.set_show(show)
        self.left_coll.set_show(show)
        self.top_coll.set_show(show)
        self.bot_coll.set_show(show)

    def set_pos(self, x, y):
        if -50 <= self.x <= self.width:
            self.x = x
        else:
            self.x = self.width-10 if self.x <= -50 else -40

        if -50 <= self.y <= self.height:
            self.y = y
        else:
            self.y = self.height-10 if self.y <= -50 else -40
        self.right_coll.set_pos(self.x + 20 - 3, self.y)
        self.left_coll.set_pos(self.x, self.y)
        self.top_coll.set_pos(self.x, self.y)
        self.bot_coll.set_pos(self.x, self.y + 20 - 3)

    def draw(self):
        self.screen.blit(self.sqr, (self.x, self.y))
        self.right_coll.draw()
        self.left_coll.draw()
        self.top_coll.draw()
        self.bot_coll.draw()
        
    
    def set_vel_x(self, x_vel):
        if x_vel > 0:
            if self.vel_x >= x_vel:
                self.vel_x = x_vel
            else:
                self.vel_x = self.vel_x + self.vel*2
        else:
            if self.vel_x <= x_vel:
                self.vel_x = x_vel
            else:
                self.vel_x = self.vel_x - self.vel*2
        
    def set_vel_y(self, y_vel):
        self.vel_y = y_vel

    def move_x(self):
        self.set_pos(self.x + self.vel_x, self.y)
        self.vel_x = self.vel_x - self.vel*self.vel_x

    def move_y(self):
        # print(self.vel_y)
        self.vel_y = self.vel_y + self.vel*0.5
            
        if self.vel_y >= 4:
            self.vel_y = 4
        

        self.set_pos(self.x, self.y + self.vel_y)
    
    def jump(self):
        self.set_vel_y(-0.5)

    def is_colliding(self, coll1):
        li_h = [self.top_coll, self.bot_coll]
        li_v = [self.right_coll, self.left_coll]
        i = 0
        t =[0,0,0,0]
        if coll1.is_horizontal:
            for coll in li_h:
                if coll.x <= coll1.x + coll1.width and coll.x + coll.width >= coll1.x and coll.y <= coll1.y + coll1.height and coll.y + coll.height >= coll1.y:
                    t[i] = 1
                else:
                    t[i] = 0
                i+=1
        else:
            i = 2
            for coll in li_v:
                if coll.x <= coll1.x + coll1.width and coll.x + coll.width >= coll1.x and coll.y <= coll1.y + coll1.height and coll.y + coll.height >= coll1.y:
                    t[i] = 1
                else:
                    t[i] = 0
                i+=1
        return t
    
    def collision_handler(self, coll):
        top, bot, right, left = self.is_colliding(coll)
        if top:
            while top:
                top, bot, right, left = self.is_colliding(coll)
                self.set_pos(self.x, self.y + 0.1)
            self.set_vel_y(-self.vel_y*0.6)
        if bot:
            while bot:
                _, bot, right, left = self.is_colliding(coll)
                self.set_pos(self.x, self.y - 0.1)
            self.set_vel_y(-self.vel_y*0.6)
        if right:
            while right:
                _, _, right, left = self.is_colliding(coll)
                self.set_pos(self.x - 0.1, self.y)
            self.vel_x = -self.vel_x*0.6
        if left:
            while left:
                _, _, _, left = self.is_colliding(coll)
                self.set_pos(self.x + 0.1, self.y)
            self.vel_x = -self.vel_x*0.6


    # def move(self, boolean):
    #     # if self.x >= -50 and self.x <= self.width:
    #     if not self.x in [-50, self.width]:
    #         if boolean:
    #             self.pos(self.x-self.vel, self.y)
    #         else:
    #             self.pos(self.x+self.vel, self.y)
    #     else:
    #         self.x = self.width-10 if self.x <= -50 else -40
    
    # def vertical_move(self, boolean):
    #     if not self.coll:
    #         # if self.y >= -50 and self.y <= self.height:
    #         if not self.y in [-50, self.height]:
    #             if boolean:
    #                 self.pos(self.x, self.y-self.vel)

    #             else:
    #                 self.pos(self.x, self.y+self.vel)
    #         else:
    #             self.y = self.height-10 if self.y <= -50 else -40