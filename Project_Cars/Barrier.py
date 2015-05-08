import pygame
from pygame.locals import *

from Util.loads import load_image


class Barrel:
    image = None

    def __init__(self, coords):
        if not self.image:
            self.image = load_image("images.png", alpha_cannel=True, path='../Images')
        self.image = pygame.transform.scale(self.image, (50,50))
        self.pos = coords
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        self.equal = True

    def update(self, speed=0):
        self.rect.y += speed

    def test_equal(self, other):
        if self.equal == True:
            if self.rect.y>=other:
                self.equal = False
                return 1
            else:
                return 0
        else:
            return 0

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