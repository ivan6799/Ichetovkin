import pygame, sys, random, os, math
from pygame.locals import *
from Classes.Vector import Vector
from Util.loads import load_image
from  Project_Cars.road import Road

MOVE = 0
TURN_LEFT = 1
TURN_RIGHT = 2
STOP = 3
ACSEL_UP = 4
ACSEL_DOWN = 5





class Car:
    def __init__(self, pos):
        self.image = load_image('racecar.png', alpha_cannel=True, path='../Images')
        self.image = pygame.transform.rotate(self.image, -90)
        self.image = pygame.transform.scale(self.image, (75,50))
        self.rect = self.image.get_rect()
        self.pos = Vector(pos)
        self.rect.topleft = pos
        self.acsel = Vector((0,0))
        self.rect_img = self.image.get_rect()
        # self.d_acsel = 0
        self.speed = Vector((0,-10))
        self.angle_speed = 40
        self.status = MOVE

    def event(self, event):
        """
        Обрабатываем события
        """
        if event.type == KEYDOWN:
            if event.key == K_UP:

                self.acsel = self.speed.normalize()* +24
                self.status = ACSEL_UP
            elif event.key == K_DOWN:
                 self.acsel = self.speed.normalize()* -12
                 self.status = ACSEL_DOWN
            elif event.key == K_LEFT:
                self.status = TURN_LEFT
            elif event.key == K_RIGHT:
                self.status = TURN_RIGHT
        elif event.type == KEYUP:
            if event.key == K_LEFT:
                self.status = MOVE
            elif event.key == K_RIGHT:
                self.status = MOVE
            elif event.key == K_UP or event.key == K_DOWN:
                self.acsel = Vector((0,0))



    def aclerate(self,dt):

        a = math.sqrt(self.speed.x**2+self.speed.y**2)
        b = math.sqrt((self.acsel*(dt/1000)).x**2 + (self.acsel*(dt/1000)).y**2 )
        if a<b:
            if self.status == ACSEL_UP:
                self.speed = self.speed + self.acsel*(dt/100)
            if self.status == ACSEL_DOWN:
                self.acsel = Vector((0,0))

        else:
            self.speed = self.speed + self.acsel*(dt/1000)
            print(self.speed.y)
            print(self.speed.x)
            if self.speed.y <= -80 :
                    self.speed.y = -80
            if self.speed.x <= -80 :
                    self.speed.x = -80
            if self.speed.x >= 80 :
                    self.speed.x = 80




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
    if testRoad.get_static_rect().colliderect(testCar.rect_img) == True or testRoad.get_static_rect2().colliderect(testCar.rect_img) :
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