import pygame, sys, random, os
from pygame.locals import *
from Util.loads import load_image


class Road:
    image = None
    def __init__(self, coords):
        if not self.image:
            Road.image = load_image("pdn_road_example.png", alpha_cannel=True, path='../Images/road parts')
        self.pos = coords
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def update(self, speed):
        self.rect.y += speed

    def render(self, screen):
        if -500 <= self.rect.y <= 1000:
            screen.blit(self.image, self.rect)



if __name__ == '__main__':

    FPS = 40
    clock = pygame.time.Clock()
    pygame.init()
    display = pygame.display.set_mode((750, 650))
    screen = pygame.display.get_surface()
    test = Road((200, 0))

    done = False
    while not done:
        # i = 0
        for e in pygame.event.get():

            if e.type == pygame.QUIT:
                done = True

            if e.type == pygame.KEYDOWN:
                if e.key == K_ESCAPE:
                    done = True

        dt = clock.tick(FPS)
        test.update(50)  # обновляем состояние объекта
        screen.fill((0, 0, 0))
        test.render(screen)
        pygame.display.flip()