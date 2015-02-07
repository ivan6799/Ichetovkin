import pygame, sys, random, os
from pygame.locals import *
from Classes import Vector
from Util.loads import load_image

MOVE = 0
MOVE_LEFT = 1
MOVE_RIGHT = 2
MOVE_UP = 3
MOVE_DOWN = 4



class Car:
    def __init__(self, pos):
        self.image = load_image('racecar.png', alpha_cannel=True, path='../Images')
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect()
        self.pos = [pos[0],pos[1]] #Позиция/кординаты объекта на экране
        self.rect.topleft = pos
        self.acsel = 0
        self.d_acsel = 0
        self.speed = (50,0)
        self.status = MOVE

    def event(self, event):
        """
        Обрабатываем события
        """
        if event.type == KEYDOWN:
            if event.key == K_UP:
                self.status = MOVE_UP
                self.d_acsel += 12
            elif event.key == K_DOWN:
                self.status = MOVE_DOWN
                self.d_acsel += -6
        elif event.type == KEYUP:
            self.d_acsel = 0

    def move(self, dt):
        """
        Передвигаем объект
        """

        self.rect.y = self.rect.y + (self.speed[1]*(dt/1000))
        self.rect.x = self.rect.x + (self.speed[0]*(dt/1000)) + (self.acsel*(dt/1000))

    def change_acsel_and_speed(self):
        self.acsel += self.d_acsel
        self.speed[0]+=self.acsel



    def update(self, dt):
        """
        Обновляем состояние(местоположение, угол поворота и т.п.) объекта
        Этот метод должен вызываться перед отрисовкой каждого кадра
        Как правило, из данного метода вызываются другие методы, которые изменяют нужное состояние объекта
        """
        self.move(dt)



    def render(self, screen):
        """
        Отрисовываем объект на поверхность screen
        """

        # pygame.draw.line(screen, (255,0,0), False, [self.rect.center, (self.rect.centerx+self.speed[0], self.rect.centery+self.speed[1])])
        screen.blit( self.image, self.rect)
        pygame.draw.lines(screen, (255,0,0), False, [self.rect.center,  (self.rect.centerx+self.speed[0], self.rect.centery+self.speed[1])])



FPS = 40
clock = pygame.time.Clock()
pygame.init()
display = pygame.display.set_mode((1000,1000))
screen = pygame.display.get_surface()
test = Car((100,100))



done = False
while not done:
    i = 0
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