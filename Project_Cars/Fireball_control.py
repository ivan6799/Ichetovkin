import pygame, sys, random, os
from pygame.locals import *
from Util.loads import load_image
from Project_Cars.Fireball import  Fireball

class Fireball_Controll:
    def __init__(self):
        self.fireballs = []
        self.scorer =35
        self.check = False

    def remove(self,i):
        self.fireballs.remove(i)

    def add_fireball(self, angle_of_rotate, pos):
        if self.scorer:
            fireball = Fireball((pos),angle_of_rotate)
            self.fireballs.append(fireball)
            self.scorer+=-1

    def event(self,event):
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                self.check = True

    def text_render(self, screen):
        font = pygame.font.Font(None, 20)
        text = font.render("Осталось выстрелов:", True, (200,200,0),None)
        i = 'x'+str(self.scorer)
        text2 = font.render(i, True, (200,200,0),None)
        textRect = text.get_rect()
        textRect2 = text2.get_rect()
        textRect.topleft = (20,100)
        textRect2.topleft = (170,100)
        screen.blit(text, textRect)
        screen.blit(text2, textRect2)


    def update(self,angle_of_rotate, pos):
            if self.check:
                self.add_fireball(angle_of_rotate, pos)
                self.check = False

            for i in self.fireballs:
                if i.rect.y<=-500:
                    self.remove(i)
            for i in self.fireballs:
                i.update()



    def render(self,screen):
        for i in self.fireballs:
            i.render(screen)
        self.text_render(screen)

if __name__=='__main__':

    FPS = 40
    clock = pygame.time.Clock()
    pygame.init()
    display = pygame.display.set_mode((750,650))
    screen = pygame.display.get_surface()
    test = Road_Control()

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
        test.update(50)            #обновляем состояние объекта
        screen.fill((0,0,0))
        test.render(screen)
        pygame.display.flip()

