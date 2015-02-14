import pygame, sys, random, os, math
from pygame.locals import *
from Classes.Vector import Vector
from Util.loads import load_image

MOVE = 0
TURN_LEFT = 1
TURN_RIGHT = 2
MOVE_UP = 3
MOVE_DOWN = 4



class Car:
    def __init__(self, pos):
        self.image = load_image('racecar.png', alpha_cannel=True, path='../Images')
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect()
        self.pos = Vector(pos)
        self.rect.topleft = pos
        self.acsel = Vector((0,0))
        # self.d_acsel = 0
        self.speed = Vector((10,0))
        self.angle_speed = 40
        self.status = MOVE

    def event(self, event):
        """
        Обрабатываем события
        """
        if event.type == KEYDOWN:
            if event.key == K_UP:
                self.acsel = self.speed.normalize()* 2
            elif event.key == K_DOWN:
                 self.acsel = self.speed.normalize()* -2
            elif event.key == K_LEFT:
                self.status = TURN_LEFT
            elif event.key == K_RIGHT:
                self.status = TURN_RIGHT
        elif event.type == KEYUP:
            self.acsel = Vector((0,0))
            self.status = MOVE



    def aclerate(self):
        self.speed = self.speed + self.acsel


    def move(self, dt):
        """
        Передвигаем объект
        """
        self.aclerate()
        print("rect.x before =",self.rect.x)
        self.rect.y = self.rect.y + (self.speed.y*(dt/1000))
        self.rect.x = self.rect.x + (self.speed.x*(dt/1000))
        print(self.speed, self.rect.topleft)


    def update(self, dt):
        """
        Обновляем состояние(местоположение, угол поворота и т.п.) объекта
        Этот метод должен вызываться перед отрисовкой каждого кадра
        Как правило, из данного метода вызываются другие методы, которые изменяют нужное состояние объекта

        """
        # if self.status == TURN_RIGHT:
        #     self.speed.rotate(self.angle_speed/1000*dt)
        # elif self.status == TURN_LEFT:
        #     self.speed.rotate(-self.angle_speed/1000*dt)
        self.move(dt)



    def render(self, screen):
        """
        Отрисовываем объект на поверхность screen
        """
        angle_of_rotate = math.degrees(math.acos(self.speed.normalize().x))
        if self.speed.y>0:
            angle_of_rotate = 360-angle_of_rotate

        rotated_img = pygame.transform.rotate(self.image, angle_of_rotate)
        rect_img = rotated_img.get_rect()
        rect_img.center = self.rect.center
        screen.blit(rotated_img, rect_img)
        pygame.draw.lines(screen, (255,0,0), False, [self.rect.center,  (self.rect.centerx+self.speed.x, self.rect.centery+self.speed.y)])



FPS = 40
clock = pygame.time.Clock()
pygame.init()
display = pygame.display.set_mode((1000,1000))
screen = pygame.display.get_surface()
test = Car((100,100))



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