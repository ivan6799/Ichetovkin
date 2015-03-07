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
        self.Srect = self.image.get_rect()
        self.Srect2 = self.image.get_rect()
        self.Srect3 = self.image.get_rect()
        self.Srect4 = self.image.get_rect()
        self.pos = pos
        self.rect.topleft = self.pos
        self.rect2.bottomleft = self.rect.topleft
        self.rect3.bottomleft = self.rect2.topleft
        self.rect4.bottomleft = self.rect3.topleft
        self.rect5.bottomleft = self.rect4.topleft
        self.Srect.topleft = self.pos
        self.Srect2.topleft = self.Srect.bottomleft
        self.Srect3.topleft = self.Srect2.bottomleft
        self.Srect4.topleft = self.Srect.bottomleft
        self.pos5 = self.rect2.topleft


    def event(self, event):
        pass

    def get_static_rect(self):
        self.staticrect = pygame.Rect((0,0), (self.rect.x, self.rect.h*5))
        return self.staticrect

    def get_static_rect2(self):
        self.staticrect2 = pygame.Rect((self.Srect.topright), (self.rect.x, self.rect.h*5))
        return self.staticrect2

    def update(self,speed):
        if speed<1:
            speed=0
        self.rect.y += speed/3
        self.rect2.y += speed/3
        self.rect3.y += speed/3
        self.rect4.y += speed/3
        self.rect5.y += speed/3
        self.Srect3.y += speed/3
        self.Srect4.y += speed/3
        if self.rect.y+self.rect.h>=self.rect.h*4:
            self.rect.topleft = self.pos5
        if self.rect2.y+self.rect.h>=self.rect.h*4:
            self.rect2.bottomleft = self.rect.topleft
        if self.rect3.y+self.rect.h>=self.rect.h*4:
            self.rect3.bottomleft = self.rect2.topleft
        if self.rect4.y+self.rect.h>=self.rect.h*4:
            self.rect4.bottomleft = self.rect3.topleft
        if self.rect5.y+self.rect.h>=self.rect.h*4:
            self.rect5.bottomleft = self.rect4.topleft


    def render(self, screen):
        # screen.blit(self.image, self.Srect)
        # screen.blit(self.image, self.Srect2)
        screen.blit(self.image, self.Srect3)
        screen.blit(self.image, self.Srect4)
        screen.blit(self.image, self.rect)
        screen.blit(self.image, self.rect2)
        screen.blit(self.image, self.rect3)
        screen.blit(self.image, self.rect4)
        screen.blit(self.image, self.rect5)
        # pygame.draw.lines(screen, (255,0,0), True, [self.rect.bottomleft, self.rect.topleft, self.rect.topright, self.rect.bottomright])
        # pygame.draw.lines(screen, (255,0,0), True, [self.rect2.bottomleft, self.rect2.topleft, self.rect2.topright, self.rect2.bottomright])
        # pygame.draw.lines(screen, (255,0,0), True, [self.rect3.bottomleft, self.rect3.topleft, self.rect3.topright, self.rect3.bottomright])
        # pygame.draw.lines(screen, (255,0,0), True, [self.rect4.bottomleft, self.rect4.topleft, self.rect4.topright, self.rect4.bottomright])
        # pygame.draw.lines(screen, (255,0,0), True, [self.rect5.bottomleft, self.rect5.topleft, self.rect5.topright, self.rect5.bottomright])
        # pygame.draw.rect(screen, (0,0,255), self.get_static_rect())
        # pygame.draw.rect(screen, (0,0,255), self.get_static_rect2())




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
