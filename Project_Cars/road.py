import pygame, sys, random, os, math
from pygame.locals import *
from Classes.Vector import Vector
from Util.loads import load_image

class Road:
    def __init__(self, pos):
        self.image = load_image('pdn_road_example.jpg', alpha_cannel=True, path='../Images/road parts')
        self.image2 = load_image('pdn_road_example.jpg', alpha_cannel=True, path='../Images/road parts')
        self.image3 = load_image('pdn_road_example.jpg', alpha_cannel=True, path='../Images/road parts')
        self.image4 = load_image('pdn_road_example.jpg', alpha_cannel=True, path='../Images/road parts')
        self.image5 = load_image('pdn_road_example.jpg', alpha_cannel=True, path='../Images/road parts')
        self.image6 = load_image('pdn_road_example.jpg', alpha_cannel=True, path='../Images/road parts')
        self.rect = self.image.get_rect()
        self.rect2 = self.image2.get_rect()
        self.rect3 = self.image3.get_rect()
        self.rect4 = self.image4.get_rect()
        self.rect5 = self.image5.get_rect()
        self.pos = pos
        self.pos2 = pos
        self.pos3 = pos
        self.pos4 = pos
        self.pos5 = pos
        self.rect.topleft = self.pos
        self.rect2.topleft = self.pos2
        self.rect2.y = self.rect.y+self.rect.h-2
        self.rect3.topleft = self.pos3
        self.rect3.y = self.rect.y+(self.rect.h*2)
        self.rect4.topleft = self.pos4
        self.rect4.y = self.rect.y+(self.rect.h*3)
        self.rect5.topleft = self.pos5
        self.rect5.y = self.rect.y+(self.rect.h*4)


    def event(self, event):
        pass

    def update(self,dt):
        self.rect.y += 150*(dt/1000)
        self.rect2.y += 150*(dt/1000)
        self.rect3.y += 150*(dt/1000)
        self.rect4.y += 150*(dt/1000)
        if self.rect.y+self.rect.h>=1000:
            self.rect.y = 0
        if self.rect2.y+self.rect.h>=1000:
            self.rect2.y = 0
        if self.rect3.y+self.rect.h>=1000:
            self.rect3.y = 0
        if self.rect4.y+self.rect.h>=1000:
            self.rect4.y = 0


    def render(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.image2, self.rect2)
        # screen.blit(self.image3, self.rect3)
        # screen.blit(self.image4, self.rect4)
        # screen.blit(self.image5, self.rect5)




FPS = 40
clock = pygame.time.Clock()
pygame.init()
display = pygame.display.set_mode((1000,1000))
screen = pygame.display.get_surface()


test = Road((200,0))

done = False
while not done:
    # i = 0
    for e in pygame.event.get():

        if e.type == pygame.QUIT :
            done = True

        if e.type == pygame.KEYDOWN:
            if e.key == K_ESCAPE:
                done = True

        test.event(e) #Передаем все события объекту

    dt = clock.tick(FPS)
    test.update(dt)            #обновляем состояние объекта
    screen.fill((0,0,0))
    test.render(screen)      #отрисовываем объект
    pygame.display.flip()
