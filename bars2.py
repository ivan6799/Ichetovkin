import pygame, sys
from pygame.locals import *

class Block:
    def __init__(self, coords, height, width, color ):
        self.x = coords[0]
        self.y = coords[1]

        self.height = height
        self.width = width
        self.color = color
        self.image = pygame.Surface((self.width, self.height))
        self.drag = False
        self.dragpinkarea = False
        self.draw()


    def update(self, mcoords):
        pass

    def moveON(self, rel):
        self.x = self.x + rel[0]
        self.y = self.y + rel[1]

    def testcolpo(self,lst):
        if lst[0].collidePoint == True:
            lst[0], lst[9] = lst[9], lst[0]
            print("lst[0]- True")
        if lst[1].collidePoint == True:
            lst[1], lst[9] = lst[9], lst[1]
            print("lst[1]- True")
        if lst[2].collidePoint == True:
            lst[2], lst[9] = lst[9], lst[2]
            print("lst[2]- True")
        if lst[3].collidePoint == True:
            lst[3], lst[9] = lst[9], lst[3]
            print("lst[3]- True")
        if lst[4].collidePoint == True:
            lst[4], lst[9] = lst[9], lst[4]
            print("lst[4]- True")
        if lst[5].collidePoint == True:
            lst[5], lst[9] = lst[9], lst[5]
            print("lst[5]- True")
        if lst[6].collidePoint == True:
            lst[6], lst[9] = lst[9], lst[6]
            print("lst[6]- True")
        if lst[7].collidePoint == True:
            lst[7], lst[9] = lst[9], lst[7]
            print("lst[7]- True")
        if lst[8].collidePoint == True:
            lst[8], lst[9] = lst[9], lst[8]
            print("lst[8]- True")
        return lst

    def event(self, event):
        """
        Обрабатываем события
        """
        if event.type == MOUSEBUTTONDOWN:

            if self.collidePoint(event.pos):
                if self.color == (10,50,70):
                    self.color = (100,50,70)
                else:
                    self.color = (10,50,70)
                self.draw()
                self.drag = True
                self.render(screen)


            if self.collidePoint2(event.pos):
                self.dragpinkarea = True

        if event.type == MOUSEBUTTONUP:
            self.drag = False
            self.dragpinkarea = False

        if event.type == pygame.MOUSEMOTION:
            if self.dragpinkarea == True :
                self.resize(event.rel)
            elif self.drag == True and self.dragpinkarea!= True:
                self.moveON(event.rel)

    def resize(self, rel):
        self.width = self.width+ rel[0]
        self.height = self.height + rel[1]
        if self.width < 10:
            self.width = 10
        if self.height <10:
            self.height = 10
        self.image = pygame.Surface((self.width, self.height))
        self.draw()

    def get_coords(self, coords):
        return coords[0], coords[1]

    def collidePoint(self, mcoords):
        if self.x <= mcoords[0] <= (self.x+self.width) and self.y <= mcoords[1] <= (self.y+self.height):
            return True
        else:
            return False

    def collidePoint2(self, mcoords): #для розовой области
        if self.width+ self.x-10 <= mcoords[0] <= (self.width+self.x) and self.height+self.y-10 <= mcoords[1] <= (self.height+self.y):
            return True
        else:

            return False

    def draw(self): #Рисует объект
        pygame.draw.rect(self.image, self.color, (0, 0, self.width, self.height))
        pygame.draw.rect(self.image, (200,0,80), (self.width-10,self.height-10 , 10, 10 ))

    def render(self, screen): #Отображает объект на эакран
        screen.blit(self.image, (self.x, self.y))







pygame.init()
display = pygame.display.set_mode((700,700))
screen = pygame.display.get_surface()



# block1 = Block((10,10), 50, 50, (10,50,70) )
# block2 = Block((100,10), 50, 50, (10,50,70) )
# block3 = Block((250,10), 50, 50, (10,50,70))
# block4 = Block((400,400), 100,100, (10,50,70))
x = 10
y = 10
w = 50
h = 50
i = 0
l = 0
lst = []
while i<10:
    a = Block((x+70*i,y), w, h,(10+i*20,50+i*20,70+i*20) )
    if i>=5:
        a = Block((x+70*l,y+200), w, h,(10+i*20,50+i*20,70+i*20))
        l+=1
    lst.append(a)
    i+=1
i = 0
# lst.append(block1)
# lst.append(block2)

done = False
while not done:
    i = 0
    for e in pygame.event.get():

        if e.type == pygame.QUIT :
            done = True

        if e.type == pygame.KEYDOWN:
            if e.key == K_ESCAPE:
                done = True

        while i<len(lst):
            lst[i].event(e)

            i+=1
        # block1.event(e)
        # block2.event(e)
        # block3.event(e)
        # block4.event(e)
        # if e.type == pygame.MOUSEMOTION:
        #     block1.event(e)
        #     print(e)
    screen.fill((0,0,0))
    # block1.render(screen)
    # block2.render(screen)
    # block3.render(screen)
    # block4.render(screen)
    k = 0
    while k < 10:
        lst[k].render(screen)
        k+=1
    pygame.display.flip()
