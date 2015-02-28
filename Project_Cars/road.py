import pygame, sys, random, os, math
from pygame.locals import *
from Classes.Vector import Vector
from Util.loads import load_image

class Road:
    def __init__(self, pos):
        self.image = load_image('pdn_road_example.png', alpha_cannel=True, path='../Images/road parts')
        self.rect = self.image.get_rect()
        self.rect2 = self.image.get_rect()
        self.rect3 = self.image.get_rect()
        self.rect4 = self.image.get_rect()
        self.rect5 = self.image.get_rect()
        self.rect6 = self.image.get_rect()
        self.pos = pos
        self.rect.topleft = self.pos
        self.rect2.bottomleft = self.rect.topleft
        self.rect3.bottomleft = self.rect2.topleft
        self.rect4.bottomleft = self.rect3.topleft
        self.rect5.bottomleft = self.rect4.topleft
        self.rect6.bottomleft = self.rect5.topleft
        self.pos5 = self.rect2.topleft


    def event(self, event):
        pass

    def update(self,speed):
        self.rect.y += speed
        self.rect2.y += speed
        self.rect3.y += speed
        self.rect4.y += speed
        print(self.rect.topleft, 1 )
        print(self.rect2.bottomleft, 2)
        if self.rect.y+self.rect.h>=1000:
            self.rect.topleft = self.pos5
        if self.rect2.y+self.rect.h>=1000:
            self.rect2.bottomleft = self.rect.topleft
        if self.rect3.y+self.rect.h>=1000:
            self.rect3.bottomleft = self.rect2.topleft
        if self.rect4.y+self.rect.h>=1000:
            self.rect4.bottomleft = self.rect3.topleft
        if self.rect5.y+self.rect.h>=1000:
            self.rect5.bottomleft = self.rect4.topleft



    def render(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.image, self.rect2)
        screen.blit(self.image, self.rect3)
        screen.blit(self.image, self.rect4)
        screen.blit(self.image, self.rect5)



if __name__=='__main__':
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
