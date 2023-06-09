from .libs import *


class Space:
    def __init__(self, actual_time, air_damping=0,gravitational_constant=9.80 , gravity_coord=None):
        self.relative_gravity = gravity_coord #most are unused due to the fact that it's unfinish
        self.air_damping = air_damping
        self.time = actual_time / 1000
        self.gravitational_constant = gravitational_constant

    def update(self):
        self.time = time() - self.time / 1000

class String:
    def __init__(self, lenght, top_elm, bottom_elm, angle=1, force=0.2):
        self.lenght = lenght
        self.angle = angle
        self.relative = 0

        self.top = top_elm
        self.bottom = bottom_elm

        self.bottom.y = self.top.y + self.lenght

        self.force = self.bottom.mass

    def add_node_top():
        pass

    def add_node_bottom():
        pass

    def calc_next_coords(self, space):
        if self.top.fixed and not self.bottom.fixed:
            relative = self.relative
            angle = self.angle
            self.angle = angle - (space.gravitational_constant/self.lenght)*sin(relative)*self.force
            self.relative = relative + self.angle*self.force

            self.bottom.x -= self.angle
            self.bottom.y = self.bottom.initial_y + (self.angle*self.angle -  self.lenght*self.lenght) / 2

            # old code
            #actual_x = self.bottom.x

            #self.bottom.x = self.angle * sin(self.bottom.weight * space.time + self.force)
            #self.bottom.y = sqrt(self.lenght * self.lenght - self.bottom.x * self.bottom.x)

            #self.bottom.x += actual_x

    def update(self, space):
        self.bottom.weight = sqrt(space.gravitational_constant / self.lenght)
        self.calc_next_coords(space)

class Obj:
    def __init__(self, x, y, mass, gravity, fixed):
        self.x,self.y = x,y
        self.initial_y = y
        self.initial_x = x
        self.fixed = fixed #unused for now
        self.mass = mass
        self.gravity = gravity