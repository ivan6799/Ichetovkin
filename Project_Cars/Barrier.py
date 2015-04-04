import pygame, sys, random, os
from pygame.locals import *
from Util.loads import load_image
# Hello world
class Barrel:
    def __init__(self, coords):
        self.image = load_image("images.jpg", alpha_cannel=True, path='../Images' )
        self.image = pygame.transform.scale(self.image, (50,50))
        self.pos = coords
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def update(self, speed=0):
        self.rect.y += speed

    def render(self, screen):
        """

        :type self: object
        """
        screen.blit(self.image, self.rect)



if __name__=='__main__':

    FPS = 40
    clock = pygame.time.Clock()
    pygame.init()
    display = pygame.display.set_mode((750,650))
    screen = pygame.display.get_surface()
    test = Barrel((200,200))

    done = False
    while not done:
        for e in pygame.event.get():

            if e.type == pygame.QUIT:
                done = True

            if e.type == pygame.KEYDOWN:
                if e.key == K_ESCAPE:
                    done = True

        dt = clock.tick(FPS)
        test.update()            #обновляем состояние объекта
        screen.fill((0,0,0))
        test.render(screen)
        pygame.display.flip()