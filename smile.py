import pygame
from pygame.draw import *

pygame.init()
FPS = 30
screen = pygame.display.set_mode((400, 400))

yellow = (225, 225, 0)
red = (225, 0, 0)
black = (0, 0, 0)

circle(screen, yellow, (200, 200), 100)
circle(screen, red, (160, 170), 30)
circle(screen, black, (160, 170), 10)
circle(screen, red, (240, 175), 20)
circle(screen, black, (240, 175), 10)
polygon(screen, black, [(130, 130), (190, 140), (185, 145), (125, 135)])
polygon(screen, black, [(210, 160), (270, 150), (275, 145), (215, 155)])
polygon(screen, black, [(160, 250), (240, 250), (240, 260), (160, 260)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
