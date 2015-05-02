import pygame, sys, random, os
from pygame.locals import *
from Util.loads import load_image
def testf1():
    print(3.14 * (5**2))

"""
Кнопка, получает координаты, изображения, функцию, надпись
"""
class Button:
    def __init__(self, coords = (0,0), images = ("button_hover.png","button_off.png","button_click.png"), func = testf1, note = "Hello world"):
        self.image = load_image(images[0], alpha_cannel=True, path='../Images')
        self.image2 = load_image(images[1], alpha_cannel=True, path='../Images')
        self.image3 = load_image(images[2], alpha_cannel=True, path='../Images')
        self.lst = [self.image, self.image2, self.image3]
        self.rect = self.image.get_rect()
        self.func = func
        self.rect.topleft = coords
        self.font = pygame.font.Font(None, 30)
        self.text = self.font.render( note, True, (255,255,255),None)
        self.textRect = self.text.get_rect()
        self.textRect.center = self.rect.center


    def render(self, screen): #Отображает объект на эакран
        screen.blit(self.lst[0], self.rect)
        screen.blit(self.text, self.textRect)


    def event(self, event):#Получает и обрабатывает события
        if event.type == MOUSEMOTION:
            if self.rect.collidepoint(event.pos) and self.lst[0]==self.image:
                self.lst[0], self.lst[1] = self.lst[1], self.lst[0]
            if self.rect.collidepoint(event.pos)==False and self.lst[0]!=self.image:
                self.lst[1],self.lst[0] = self.lst[0], self.lst[1]
        elif event.type == MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos) and self.lst[0]!= self.image:
                self.lst[0], self.lst[2] = self.lst[2], self.lst[0]
                self.func()

        elif event.type == MOUSEBUTTONUP and self.lst[0]!= self.image:
                self.lst[0], self.lst[2] = self.lst[2], self.lst[0]
"""
, но в дополнении получает еще 1 надпись и еще 1 изоюражание.
"""
class OffB(Button):
    def __init__(self, coords = (0,0), images = ("button_hover.png","button_on.png","button_click.png", "button_off.png"), func = testf1, note = "Hello world", note2 = "Well done"):
        super().__init__(coords, images, func, note)
        self.image4 = load_image(images[3])
        self.lst.append(self.image4)
        self.text2  = self.font.render( note2, True, (255,255,255),None)

    def event(self, event):
        super().event(event)
        if event.type == MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.changeText()
                if self.image!= self.image4:
                    self.image = self.image4
                    self.lst[0] = self.image4

    def changeText(self):#Меняет текст на кнопке
        self.text, self.text2 = self.text2, self.text


if __name__ == '__main__':
    pygame.init()
    display = pygame.display.set_mode((700,700))
    screen = pygame.display.get_surface()
    MainBut = Button()
    ModBut1 = OffB((400,50),["button_hover.png","button_on.png","button_click.png","button_off.png"], testf1, "Hello world", "Well done")
    ModBut2 = OffB((200,200),["button_hover.png","button_on.png","button_click.png","button_off.png"], testf1, "Hello world", "Well done")


    done = False
    while not done:
        for e in pygame.event.get():

            if e.type == pygame.QUIT :
                done = True

            if e.type == pygame.KEYDOWN:
                if e.key == K_ESCAPE:
                    done = True
            if e.type == MOUSEBUTTONDOWN:
                if MainBut.rect.collidepoint(e.pos):
                    ModBut1.changeText()
                    ModBut2.changeText()

            MainBut.event(e)
            ModBut1.event(e)
            ModBut2.event(e)

        screen.fill((0,0,0))
        MainBut.render(screen)
        ModBut1.render(screen)
        ModBut2.render(screen)
        pygame.display.flip()
