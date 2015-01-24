import pygame, sys, random, os
from pygame.locals import *
from Util.loads import load_image

class Block:
    def __init__(self, coords, height, width, color ):
        self.color = color
        self.select_color = (255,0,0)
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = coords
        self.draw()
