#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, os

class Animation:
    def __init__(self, sprites=None, time=100):
        self.sprites = sprites
        self.time = time
        self.work_time = 0
        self.skip_frame = 0
        self.frame = 0

    def update(self, dt):
        self.work_time += dt
        #print("work_time = ",self.work_time)
        # Считаем сколько кадров надо перелистнуть
        self.skip_frame = self.work_time / self.time
        #print("skip_frame = ",self.skip_frame)
        if self.skip_frame > 0:
            # Не забываем, что у нас, при смене кадров с частотой в
            # 100 мс, вполне могло уже пройти 133 мс, и важно не
            # забыть про эти 33 мс.
            self.work_time = self.work_time % self.time
            self.frame += self.skip_frame
            if self.frame >= len(self.sprites):
                #print("self.frame - ",self.frame)
                #print("len(self.sprites) = ", len(self.sprites))
                self.frame = 0

    def get_sprite(self):
        #print("frame = ", self.frame)
        return self.sprites[self.frame]

if __name__ == '__main__':
    pygame.init()

    display = pygame.display.set_mode((400,200))

    screen = pygame.Surface((200,200))

    time = 180
    sprite = pygame.image.load('footman.png').convert_alpha()

    # Создание анимации.
    anim = list()
    dx = 4
    dy = 1
    for x in range(4):
        y = 70*x+2*x
        anim.append(sprite.subsurface((0+70*dx+4, y+70*dy,70,70)))

    robot = Animation(anim, time)

    clock = pygame.time.Clock()

    done = False
    dt = 0
    while not done:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                done = True

        # Обновление каждого объекта анимации
        robot.update(dt)

        screen.fill((255,255,255))

        # Рисуем анимацию.
        screen.blit(robot.get_sprite(), (0, 0))

        display.blit(screen,(0,0))
        pygame.display.flip()
        dt = clock.tick(20)
        #print("clock = ",clock)
