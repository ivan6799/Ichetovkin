import pygame, math
from pygame.locals import *
import math

class Vector:
    def __init__(self,coords):
        self.x = coords[0]
        self.y = coords[1]

    def __add__(self, other):
        return Vector((self.x+other.x,self.y+other.y))

    def __repr__(self):
        return "v(%s,%s)"%(math.floor(self.x), math.floor(self.y))

    def __mul__(self, other):
        return Vector((self.x*other,self.y*other))

    def __floordiv__(self, other):
        return Vector((self.x/other,self.y/other))

    def len(self):
        return math.sqrt(self.x**2+self.y**2)

    def normalize(self):
        try:
            return Vector((self.x/self.len(), self.y/self.len()))
        except ZeroDivisionError:
            return Vector((0,0))

    def update(self):
        pass

    def as_point(self):
        return self.x, self.y

    def rotate(self, angle):
        angle = math.radians(angle)
        x = self.x * math.cos(angle) - self.y * math.sin(angle)
        y = self.x * math.sin(angle) + self.y * math.cos(angle)
        self.x, self.y = x, y


    def render(self, screen):
        pygame.draw.line(screen, (250,0,0),(0,0),(self.x,self.y))

if __name__ == "__main__":
    v1 = Vector((10,10))
    v2 = Vector((20,20))
    print(v2)
    v2.rotate(45)
    v2.rotate(0)
    print(v2)