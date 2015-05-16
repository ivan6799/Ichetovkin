import math

import pygame
from pygame.locals import *

from Classes.Vector import Vector
from Util.loads import load_image

class Fireball():
    image = None
    def __init__(self,pos, angle_of_rotate):
        if not self.image:
            Fireball.image = load_image("Flying_fireball.png", alpha_cannel=True,  path='../Images')
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.rect_img = self.rect
        self.pos = Vector(pos)
        self.AoR = angle_of_rotate-90
        self.speed = Vector((0,-10))
        self.speed.rotate(-self.AoR)

    def move(self):

        self.pos += self.speed

    def update(self):
        self.move()

    def render(self,screen):
        rotated_img = pygame.transform.rotate(self.image, self.AoR)
        self.rect_img = rotated_img.get_rect()
        self.rect_img.center = self.pos.as_point()
        screen.blit(rotated_img, self.rect_img)






if __name__ == '__main__':
    FPS = 40
    clock = pygame.time.Clock()
    pygame.init()
    display = pygame.display.set_mode((750,650))
    screen = pygame.display.get_surface()
    test = Fireball((200, 500),90)

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
        test.update()            #обновляем состояние объекта
        screen.fill((0,0,0))
        test.render(screen)
        pygame.display.flip()