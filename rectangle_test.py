from time import sleep
import pygame
from pygame.locals import *
from sys import exit

from random import *

pygame.init()
screen = pygame.display.set_mode((800, 600), 0, 32)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.lock()

    for count in range(1):
        random_color = (randint(0, 255),randint(0, 255), randint(0, 255))
        random_pos = (randint(0, 799), randint(0, 599))
        random_size = (799-randint(random_pos[0], 799), 599-randint(random_pos[1],599))
        pygame.draw.rect(screen, random_color, Rect(random_pos, random_size))
    
    screen.unlock()
    sleep(0.5)

    pygame.display.update()
    