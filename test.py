import pygame, sys, os

def draw(surf):
    pygame.draw.rect(surf, (200,0,0), (30,30, 100, 70))
    pygame.draw.lines(surf, (0,0,200), False, [(80,65), (200,65)] )

pygame.init()
display = pygame.display.set_mode((700,700))
screen = pygame.display.get_surface()
drawing_surf = pygame.Surface((700,700))

draw(drawing_surf)
while True: #главный цикл программы
    for e in pygame.event.get(): #цикл обработки очереди событий окна
        if e.type == pygame.QUIT:
            sys.exit() #Закрытие окна программы
         #Устанавливаем FPS
    screen.fill((0,0,0))   #Очищаем экран
    screen.blit(drawing_surf, (0,0))
    pygame.display.flip()
