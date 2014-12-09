import pygame, sys, random, os
from pygame.locals import *
def load_image(name,alpha_cannel):
    fullname = os.path.join('Images', name) # Указываем путь к папке с картинками

    try:
        image = pygame.image.load(fullname) # Загружаем картинку и сохраняем поверхность (Surface)
    except (pygame.error): # Если картинки нет на месте
        print("Cannot load image:", name)
        return 0
    if(alpha_cannel):
        image = image.convert_alpha()
    else:
        image = image.convert()

    return image

class Block:
    def __init__(self, coords, height, width, color ):
        self.color = color
        self.select_color = (255,0,0)
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = coords
        self.rectResize = pygame.Rect(self.rect.w-10, self.rect.h-10,10,10 )
        self.drag = False
        self.dragpinkarea = False
        self.draw()


    def update(self, mcoords):
        pass

    def moveON(self, rel):
        self.rect.x += rel[0]
        self.rect.y += rel[1]


    def event(self, event):
        """
        Обрабатываем события
        """
        if event.type == MOUSEBUTTONDOWN: #Click

           if self.rect.collidepoint(event.pos):
                self.color, self.select_color = self.select_color, self.color
                self.draw()

                if self.rectResize.move(self.rect.topleft).collidepoint(event.pos):
                    self.dragpinkarea = True
                else:
                    self.drag = True

                return self

        if event.type == MOUSEBUTTONUP:
            self.drag = False
            self.dragpinkarea = False

        if event.type == pygame.MOUSEMOTION:
            if self.dragpinkarea == True :
                self.resize(event.rel)
                self.image = pygame.Surface((self.rect.w, self.rect.h))
                self.draw()
                print(True)


            elif self.drag == True and self.dragpinkarea!= True:
                self.moveON((event.rel[0], event.rel[1]))
                print(event.pos[0], event.pos[1])
                print(self.rectResize.x, self.rectResize.y)
                print(False)

    def resize(self, rel):
        self.rect.w = self.rect.w + rel[0]
        self.rect.h = self.rect.h + rel[1]
        if self.rect.w < 10:
            self.rect.w = 10


        elif self.rect.h <10:
            self.rect.h = 10

        else:
            self.rectResize = self.rectResize.move(rel)

        # if self.rect.w > 10 and self.rect.h > 10:
        #     self.rectResize = self.rectResize.move(rel)
        # elif self.rect.w == 10:
        #     print(" w <= 10")
        #     # self.rectResize = self.rectResize.move((0,rel[1]))
        # elif self.rect.h == 10:
        #     pass
        #     # self.rectResize = self.rectResize.move((rel[0],0))


        self.draw()


    def draw(self): #Рисует объект
        pygame.draw.rect(self.image, self.color, (0, 0, self.rect.w, self.rect.h))
        pygame.draw.rect(self.image, (200,0,80), self.rectResize)


    def render(self, screen): #Отображает объект на эакран
        screen.blit(self.image, self.rect)

class Buttom:
    def __init__(self, coords):
        self.image = load_image("button_hover.png",  1)
        self.startimage = load_image("button_hover.png",  1)
        self.image2 = load_image("button_off.png",  1)
        self.image3 = load_image("button_click.png",  1)
        self.lst = [self.image, self.image2, self.image3]
        self.rect = self.image.get_rect()
        self.rect.topleft = coords

    def render(self, screen): #Отображает объект на эакран
        screen.blit(self.lst[0], self.rect)

    def event(self, event):
        if event.type == MOUSEMOTION:
            if self.rect.collidepoint(event.pos) and self.lst[0]==self.image:
                self.lst[0], self.lst[1] = self.lst[1], self.lst[0]
            if self.rect.collidepoint(event.pos)==False and self.lst[0]!=self.image:
                self.lst[1],self.lst[0] = self.lst[0], self.lst[1]
        if event.type == MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos) and self.lst[0] == self.image2:
                self.lst[0], self.lst[2] = self.lst[2], self.lst[0]
                if event.type == MOUSEBUTTONUP:
                    self.lst[0], self.lst[2] = self.lst[2], self.lst[0]




        # if event.type == MOUSEBUTTONDOWN(event.pos):
        #     if self.rect.collidepoint:
        #         self.image2, self.image3 = self.image3, self.image2









pygame.init()
display = pygame.display.set_mode((700,700))
screen = pygame.display.get_surface()


test = Buttom((50,50))
x = 10
y = 10
w = 50
h = 50
i = 0
l = 0
blocks = []
while i<10:
    a = Block((x+70*i,y), w, h,(random.randint(0,255),random.randint(0,255),random.randint(0,255)) )
    if i>=5:
        a = Block((x+70*l,y+200), w, h,(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        l+=1
    blocks.append(a)
    i+=1
i = 0
done = False
for block in blocks:
    print(block.rect)
while not done:
    i = 0
    for e in pygame.event.get():

        if e.type == pygame.QUIT :
            done = True

        if e.type == pygame.KEYDOWN:
            if e.key == K_ESCAPE:
                done = True
        test.event(e)


        # for block in blocks:
        #     if block.event(e):
        #         if blocks.index(block)!=len(blocks)-1:
        #             blocks.remove(block)
        #             blocks.append(block)

    screen.fill((0,0,0))
    # for block in blocks:
    #     block.render(screen)
    test.render(screen)
    pygame.display.flip()
