import pygame, sys, random, os
from pygame.locals import *
from Util.loads import load_image
from Project_Cars import  Barrier


LEN_BARREL_SPAWN = 300


class Barrel_Control:
    def __init__(self, road_x=200, road_w=299, window_h=700, bil=5):
        self.barrels = []
        self.x_start = road_x
        self.x_end = road_x+road_w
        self.remove_pos = window_h
        self.max_barrels_in_line = bil
        self.road_parts = self.max_barrels_in_line+1

    def add_barrel(self):
        barrel_field = self.x_start + (self.x_end-self.x_start)/self.road_parts*random.randint(0,self.max_barrels_in_line)
        barrel = Barrier.Barrel((barrel_field, -50))
        self.barrels.append(barrel)


    def remove_barrel(self, barrel):
        self.barrels.remove(barrel)

    def update(self, speed):
        if not self.barrels:
            self.add_barrel()
        elif self.barrels[len(self.barrels)-1].rect.y >= LEN_BARREL_SPAWN:
            self.add_barrel()
        for i in self.barrels:
            i.update(speed)

    def render(self,screen):
        for i in self.barrels:
            i.render(screen)

if __name__== '__main__':

    FPS = 40
    clock = pygame.time.Clock()
    pygame.init()
    display = pygame.display.set_mode((750,650))
    screen = pygame.display.get_surface()
    test = Barrel_Control()

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
        test.update(10)            #обновляем состояние объекта
        screen.fill((0,0,0))
        test.render(screen)
        pygame.display.flip()