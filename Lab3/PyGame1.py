import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1450, 900))

rect(screen, (254, 213, 162), (0, 0, 1450, 200), 0) # Higher sky
rect(screen, (254, 213, 196), (0, 200, 1450, 200), 0) # Middle sky
rect(screen, (254, 213, 148), (0, 400, 1450, 200), 0) # Lower sky

circle(screen, (252, 238, 33), (725, 200), 80) # Sun

polygon(screen, (252, 152, 49), [(0, 430), (1450, 280), (1350, 250), (1301, 277), (1206, 223), (1152, 237), (1091, 183),
                                (969, 200), (833, 291), (840, 318), (772, 305), (725, 355), (617, 352), (549, 366),
                                (379, 244), (359, 210), (298, 156), (298, 406), (14, 393), (0, 430)]) # Distant mountains

polygon(screen, (172, 67, 52), [(0, 644), (1450, 630), (1450, 346), (1399, 434), (1335, 427), (1304, 481), (1254, 434),
                            (1186, 515), (833, 515), (698, 542), (596, 468), (461, 440), (420, 562), (318, 508),
                            (251, 623), (20, 481), (0, 481), (0, 644)]) # Nearby mountains
ellipse(screen, (172, 67, 52), (27, 386, 230, 515), 0)                  # Nearby mountains

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
