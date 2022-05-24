import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 600), 0, 32)

points = []

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == MOUSEBUTTONDOWN:
            points.append(event.pos)
    
    screen.fill((255, 255, 255))

    if len(points) >= 3:
        pygame.draw.polygon(screen, (0, 0, 255), points)
    for point in points:
        pygame.draw.circle(screen, (255, 0, 0), point, 3)
    
    pygame.display.update()