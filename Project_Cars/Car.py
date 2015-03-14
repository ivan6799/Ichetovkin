import pygame
import sys
import random
import os
import math
from pygame.locals import *
from Classes.Vector import Vector
from Util.loads import load_image
from Project_Cars.road import Road

MOVE = 0
TURN_LEFT = 1
TURN_RIGHT = 2
STOP = 3
ACCEL_UP = 4
ACCEL_DOWN = 5


class Car:
    K_ACCELERATE = 24
    K_FRICTION = -5

    def __init__(self, pos):
        self.image = load_image('racecar.png', alpha_cannel=True, path='../Images')
        self.image = pygame.transform.rotate(self.image, -90)
        self.image = pygame.transform.scale(self.image, (75,50))
        self.rect = self.image.get_rect()
        self.pos = Vector(pos)
        self.rect.topleft = pos
        self.accel = Vector((0, 0))
        self.rect_img = self.image.get_rect()
        self.speed = Vector((0, -10))
        # self.friction = self.speed.normalize()*-5
        self.angle_speed = 40
        self.status = MOVE
        self.max_speed = 80

    def friction(self):
        return self.speed.normalize()* self.K_FRICTION


    def event(self, event):
        """
        Обрабатываем события
        """
        if event.type == KEYDOWN:
            if event.key == K_UP:
                self.accel = self.speed.normalize()*self.K_ACCELERATE + self.friction()
                self.status = ACCEL_UP
            if event.key == K_DOWN:
                self.accel = self.speed.normalize()*-self.K_ACCELERATE + self.friction()
                self.status = ACCEL_DOWN
            elif event.key == K_LEFT:
                self.accel = self.friction()
                self.status = TURN_LEFT
            elif event.key == K_RIGHT:
                self.accel = self.friction()
                self.status = TURN_RIGHT
        elif event.type == KEYUP:
            if event.key == K_LEFT:
                self.status = MOVE
            elif event.key == K_RIGHT:
                self.status = MOVE
            elif event.key == K_UP or event.key == K_DOWN:
                self.accel = self.friction()

    def aclerate(self, dt):

        if self.speed < (self.accel*(dt/1000)):
            if self.status == ACCEL_UP:
                self.speed = self.speed + self.accel*(dt/1000)
            if self.status == ACCEL_DOWN:
                self.accel = Vector((0, 0))
        else:
            speed_temp = self.speed
            self.speed = self.speed + self.accel*(dt/1000)
            if self.speed.len() > self.max_speed:
                self.speed = speed_temp

    def move(self, dt):
        """
        Передвигаем объект
        """
        self.aclerate(dt)
        self.pos.x += self.speed.x*(dt/1000)
        # print(self.speed.len())


    def update(self, dt):
        """
        Обновляем состояние(местоположение, угол поворота и т.п.) объекта
        Этот метод должен вызываться перед отрисовкой каждого кадра
        Как правило, из данного метода вызываются другие методы, которые изменяют нужное состояние объекта

        """

        if self.status == TURN_RIGHT:
            self.speed.rotate(self.angle_speed/1000*dt)
        elif self.status == TURN_LEFT:
            self.speed.rotate(-self.angle_speed/1000*dt)
        self.move(dt)



    def render(self, screen):
        """
        Отрисовываем объект на поверхность screen
        """
        angle_of_rotate = math.degrees(math.acos(self.speed.normalize().x))
        if self.speed.y>0:
            angle_of_rotate = 360-angle_of_rotate

        rotated_img = pygame.transform.rotate(self.image, angle_of_rotate)
        self.rect_img = rotated_img.get_rect()
        self.rect_img.center = self.pos.as_point()
        screen.blit(rotated_img, self.rect_img)
        pygame.draw.lines(screen, (255,0,0), False, [self.pos.as_point(),  (self.pos.x+self.speed.x, self.pos.y+self.speed.y)])
        # pygame.draw.rect(screen,(255,0,0), self.rect_img)
        # print()



FPS = 40
clock = pygame.time.Clock()
pygame.init()
display = pygame.display.set_mode((750,650))
screen = pygame.display.get_surface()
testRoad = Road((200,0))
testCar = Car((200+ testRoad.rect.w/2, 400))



done = False
while not done:
    # i = 0
    for e in pygame.event.get():

        if e.type == pygame.QUIT :
            done = True

        if e.type == pygame.KEYDOWN:
            if e.key == K_ESCAPE:
                done = True

        testCar.event(e) #Передаем все события объекту
    dt = clock.tick(FPS)
    if testRoad.get_static_rect().colliderect(testCar.rect_img) or testRoad.get_static_rect2().colliderect(testCar.rect_img):
        if testRoad.get_static_rect().colliderect(testCar.rect_img) == True:
            if testCar.speed.x>0:
                testCar.pos.x = testCar.pos.x + testCar.speed.x*dt/1000
            elif    testRoad.get_static_rect2().colliderect(testCar.rect_img) == True:
                if testCar.speed.x<0:
                    testCar.pos.x = testCar.pos.x + testCar.speed.x*dt/1000
        testCar.pos.x = testCar.pos.x - testCar.speed.x*dt/1000




    testCar.update(dt)            #обновляем состояние объекта
    testRoad.update(testCar.speed.len())
    screen.fill((0,0,0))
    testRoad.render(screen)
    testCar.render(screen)      #отрисовываем объект
    pygame.display.flip()