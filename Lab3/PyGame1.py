import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1450, 1000))

rect(screen, (254, 213, 162), (0, 0, 1450, 200), 0) # Higher sky
rect(screen, (254, 213, 196), (0, 200, 1450, 200), 0) # Middle sky
rect(screen, (254, 213, 148), (0, 400, 1450, 200), 0) # Lower sky

circle(screen, (252, 238, 33), (725, 200), 80) # Sun

polygon(screen, (252, 152, 49), [(0, 430), (1450, 280), (1350, 250), (1301, 277), (1206, 223), (1152, 237), (1091, 183),
                                (969, 200), (963, 226), (939, 269), (885, 302), (840, 318), (772, 305), (725, 355), (617, 352), (549, 366),
                                (379, 244), (359, 210), (298, 156), (266, 228), (228, 253), (209, 266), (158, 336), (108, 317), (65, 393), (14, 393), (0, 430)]) # Distant mountains
ellipse(screen, (252, 152, 49), (965, 149, 147, 130), 0) 

polygon(screen, (172, 67, 52), [(0, 644), (1450, 630), (1450, 346), (1399, 434), (1335, 427), (1304, 481), (1254, 434),
                            (1186, 515), (833, 515), (698, 542), (596, 468), (461, 440), (420, 562), (318, 508),
                            (251, 623), (20, 481), (0, 481), (0, 644)]) # Nearby mountains
ellipse(screen, (172, 67, 52), (35, 386, 230, 515), 0)                  # Nearby mountains
ellipse(screen, (172, 67, 52), (839, 403, 306, 242), 0)                 # Nearby mountains
ellipse(screen, (172, 67, 52), (1120, 448, 112, 168), 0)                # Nearby mountains

rect(screen, (188,125,145), (0, 600, 1450, 400), 0) # Ground level

polygon(screen, (57, 5, 42), [(0, 494), (171, 545), (304, 722), (431, 886), (475, 924), (678, 949), (918, 823), (988, 848), (1013, 880), (1082, 880), (1171, 829), (1298, 703), (1450, 583), (1450, 1000), (0, 1000)], 0) # Here you are

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
