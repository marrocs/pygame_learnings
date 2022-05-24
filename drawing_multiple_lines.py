import pygame
from pygame.locals import *
from sys import exit
from random import *

pygame.init()
screen = pygame.display.set_mode((800, 600), 0, 32)

points = []

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == MOUSEMOTION:
            points.append(event.pos)
            if len(points)>100:
                del points[0]

    screen.fill((255, 255, 255))

    if len(points)>1:
        pygame.draw.lines(screen, (randint(0, 255), randint(0, 255), randint(0, 255)), False, points, 3)

    pygame.display.update()

