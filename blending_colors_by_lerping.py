from random import randint, random
import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800, 600), 0, 32)

num1 = randint(0, 255)
num2 = randint(0, 255)
num3 = randint(0, 255)

color1 = (num2, num1, num3)
color2 = (num3, num2, num1)
factor = 0

def blend_color(color1, color2, blend_factor):
    red1, green1, blue1 = color1
    red2, green2, blue2 = color2
    red = red1+(red2-red1)*blend_factor
    green = green1+(green2-green1)*blend_factor
    blue = blue1+(blue2-blue1)*blend_factor
    return int(red), int(green), int(blue)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.fill((255, 255, 255))

    tri = [(0, 120), (799, 100), (799, 140)]
    pygame.draw.polygon(screen, (255, 0, 0), tri)
    pygame.draw.circle(screen, (0, 0, 255), (int(factor*799), 120), 10)

    x, y = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        factor = x/799
        pygame.display.set_caption('Pygame color blend test - %.3f' %factor)

    color = blend_color(color1, color2, factor)
    pygame.draw.rect(screen, color, (0, 300, 800, 300))

    pygame.display.update()

