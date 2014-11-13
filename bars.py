import pygame, sys
from pygame.locals import *
from Utilities.loads import load_image
class Block:
    def __init__(self, coords, height, width, color,  image ):
        #self.x = coords[0]
        #self.y = coords[1]
        self.coords = [coords[0], coords[1]]
        self.height = height
        self.width = width
        self.color = color
        self.image = image
    def update(self):
        pass

    def render(self, screen):
        screen.blit(self.image, self.coords )

    def get_coords(self, coords):
        return coords[0], coords[1]


pygame.init()
display = pygame.display.set_mode((700,700))
screen = pygame.display.get_surface()
block1 = Block((50,50), 10, 20, )

