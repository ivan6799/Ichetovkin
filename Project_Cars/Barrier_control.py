import pygame, sys, random, os
from pygame.locals import *
from Util.loads import load_image
from Project_Cars import  Barrier
class Barrel:
    def __init__(self):
           self.barrels = []

    def update(self):
        a = Barrel(50,50)

    def render(self,screen):
        screen.blit(self.image,self.rect)

if __name__=='__main__':

    FPS = 40
    clock = pygame.time.Clock()
    pygame.init()
    display = pygame.display.set_mode((750,650))
    screen = pygame.display.get_surface()

    done = False
    while not done:
        # i = 0
        for e in pygame.event.get():

            if e.type == pygame.QUIT :
                done = True

            if e.type == pygame.KEYDOWN:
                if e.key == K_ESCAPE:
                    done = True

        dt = clock.tick(FPS)
        # test.update()            #обновляем состояние объекта
        screen.fill((0,0,0))
        # test.render(screen)
        pygame.display.flip()