import pygame, sys, random, os
from pygame.locals import *
from Util.loads import load_image
from Project_Cars import  Barrier

#Показывает через сколько пикселей создается новая партия ящиков
LEN_BARREL_SPAWN = 100


class Barrel_Control:
    def __init__(self, road_x=200, road_w=299*2, window_h=700, bil=5000):
        self.barrels = []
        self.barrels_main = []
        self.x_start = road_x
        self.x_end = road_x+road_w
        # self.remove_pos = window_h
        self.barrel_score = 0
        self.random_coordinate = bil
        self.barrel_forfeit = 0

    def add_barrel(self):
        barrel_field = self.x_start + (self.x_end-self.x_start)/(self.random_coordinate+1)*random.randint(0,self.random_coordinate)
        barrel_field2 = self.x_start + (self.x_end-self.x_start)/(self.random_coordinate+1)*random.randint(0,self.random_coordinate)
        barrel_field3 = self.x_start + (self.x_end-self.x_start)/(self.random_coordinate+1)*random.randint(0,self.random_coordinate)
        if barrel_field>self.x_end-55:
            barrel_field = self.x_end-50
        if barrel_field2>self.x_end-55:
            barrel_field2 = self.x_end-50
        if barrel_field3>self.x_end-55:
            barrel_field3 = self.x_end-50
        barrel = Barrier.Barrel((barrel_field, -150))
        barrel2 = Barrier.Barrel((barrel_field2, -100))
        barrel3 = Barrier.Barrel((barrel_field3, -50))
        self.barrels.append(barrel)
        self.barrels.append(barrel2)
        self.barrels.append(barrel3)


    def remove_barrel(self, barrel):
        self.barrels.remove(barrel)

    def update(self, speed, other):
        if not self.barrels:
            self.add_barrel()
        elif self.barrels[len(self.barrels)-1].rect.y >= LEN_BARREL_SPAWN:
            self.add_barrel()
        for i in self.barrels:
            i.update(speed)
        for i in self.barrels:
            self.barrel_score+= i.test_equal(other)


    def text_render(self, screen):
        font = pygame.font.Font(None, 20)
        text = font.render("Пропущено бочек :", True, (0,255,0),None)
        i = str(self.barrel_score)
        text2 = font.render(i, True, (0,255,0),None)
        textRect = text.get_rect()
        textRect2 = text2.get_rect()
        textRect.topleft = (20,60)
        textRect2.topleft = (170,60)
        screen.blit(text, textRect)
        screen.blit(text2, textRect2)

    def text_render2(self, screen):
        font = pygame.font.Font(None, 20)
        text = font.render("Сбито бочек:", True, (255,0,0),None)
        i = str(self.barrel_forfeit)
        text2 = font.render(i, True, (255,0,0),None)
        textRect = text.get_rect()
        textRect2 = text2.get_rect()
        textRect.topleft = (20,80)
        textRect2.topleft = (130,80)
        screen.blit(text, textRect)
        screen.blit(text2, textRect2)


    def render(self,screen):
        for i in self.barrels:
            i.render(screen)
        self.text_render(screen)
        self.text_render2(screen)

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