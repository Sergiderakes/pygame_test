import time

class cuadrado:
    x = 320
    y = 240
    width = 0
    height = 0
    vel_x = 0
    vel_y = 0
    coll = False
    gravedad = True
    vel = 0
    tick_count = 0
    
    def __init__(self,x ,y, width, height, vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel

    def set_pos(self, x, y):
        if -50 <= self.x <= self.width:
            self.x = x
        else:
            self.x = self.width-10 if self.x <= -50 else -40

        if -50 <= self.y <= self.height:
            self.y = y
        else:
            self.y = self.height-10 if self.y <= -50 else -40
    
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
        if self.gravedad:
            # print(self.vel_y)
            self.vel_y = self.vel_y + self.vel*0.5
            
            if self.vel_y >= 4:
                self.vel_y = 4
        else:
            self.vel_y = 0

        self.set_pos(self.x, self.y + self.vel_y)
    
    def jump(self):
        self.set_vel_y(-0.5)
        self.gravedad = True

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