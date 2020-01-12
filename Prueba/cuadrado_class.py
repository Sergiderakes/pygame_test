import time

class cuadrado:
    x = 320
    y = 240
    x_ant = x
    y_ant = y
    width = 0
    height = 0
    vel = 0.3 # 0.3
    coll = False
    
    def __init__(self,x ,y, width, height, vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel

    def pos(self, x, y):
        self.x_ant = self.x
        self.y_ant = self.y
        if self.x >= -50 and self.x <= self.width:
            self.x = x
        else:
            self.x = self.width-10 if self.x <= -50 else -40

        if self.y >= -50 and self.y <= self.height:
            self.y = y
        else:
            self.y = self.height-10 if self.y <= -50 else -40
    
    def pos1(self, x, y):
        self.x = x
        self.y = y
    
    def jump(self):
        if not self.vel == 0:
            self.y = self.y - 40

    def move(self, boolean):
        if self.x >= -50 and self.x <= self.width:
            if boolean:
                self.pos(self.x-self.vel, self.y)
            else:
                self.pos(self.x+self.vel, self.y)
        else:
            self.x = self.width-10 if self.x <= -50 else -40
    
    def vertical_move(self, boolean):
        if not self.coll:
            if self.y >= -50 and self.y <= self.height:
                if boolean:
                    self.pos(self.x, self.y-self.vel)

                else:
                    self.pos(self.x, self.y+self.vel)
            else:
                self.y = self.height-10 if self.y <= -50 else -40