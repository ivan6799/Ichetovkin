import pygame, sys, random, os
from pygame.locals import *
from Util.loads import load_image


def testf1():
    return None


class Button:
    """
    Кнопка, получает координаты, изображения, функцию, надпись
    """
    def __init__(self, coords=(0, 0), images=("button_hover.png", "button_off.png", "button_click.png"), func=testf1,
                 note="Hello world"):
        self.image = load_image(images[0], alpha_cannel=True, path='../Images/Buttons')
        self.image2 = load_image(images[1], alpha_cannel=True, path='../Images/Buttons')
        self.image3 = load_image(images[2], alpha_cannel=True, path='../Images/Buttons')
        self.lst = [self.image, self.image2, self.image3]
        self.rect = self.image.get_rect()
        self.func = func
        self.note = note
        self.rect.topleft = coords
        self.font = pygame.font.Font(None, 30)
        self.text = self.font.render(self.note, True, (255, 255, 255), None)
        self.textRect = self.text.get_rect()
        self.textRect.center = self.rect.center

    def render(self, screen):  # Отображает объект на эакран
        screen.blit(self.lst[0], self.rect)
        screen.blit(self.text, self.textRect)

    def event(self, event):  # Получает и обрабатывает события
        if event.type == MOUSEMOTION:
            if self.rect.collidepoint(event.pos) and self.lst[0] == self.image:
                self.lst[0], self.lst[1] = self.lst[1], self.lst[0]
            if self.rect.collidepoint(event.pos) == False and self.lst[0] != self.image:
                self.lst[1], self.lst[0] = self.lst[0], self.lst[1]

        elif event.type == MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos) and self.lst[0] != self.image:
                self.lst[0], self.lst[2] = self.lst[2], self.lst[0]

        elif event.type == MOUSEBUTTONUP and self.lst[0] != self.image:
            self.lst[0], self.lst[2] = self.lst[2], self.lst[0]
            print(True)
            return True

if __name__ == '__main__':

    pygame.init()
    display = pygame.display.set_mode((700, 700))
    screen = pygame.display.get_surface()
    MainBut = Button((350 - 186 / 2, 150), ["button_hover.png", "button_off.png", "button_click.png"], testf1, "Start")
    MainBut2 = Button((350 - 186 / 2, 250), ["button_hover.png", "button_off.png", "button_click.png"], testf1,
                      "Best score")
    MainBut3 = Button((350 - 186 / 2, 350), ["button_hover.png", "button_off.png", "button_click.png"], testf1, "Exit")

    done2 = False
    i = 0
    while not done2:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                done2 = True
            if e.type == pygame.KEYDOWN:
                if e.key == K_ESCAPE:
                    done2 = True
            MainBut.event(e)
            MainBut2.event(e)
            MainBut3.event(e)
            if MainBut3.event(e):
                done2 = True
            if MainBut.event(e):
                from Project_Cars.Car import *
                done2 = True
        screen.fill((0, 0, 0))
        MainBut.render(screen)
        MainBut2.render(screen)
        MainBut3.render(screen)
        pygame.display.flip()