import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

circle(screen, (225, 255, 0), (200, 200), 100)
circle(screen, (225, 0, 0), (160, 170), 30)
circle(screen, (0, 0, 0), (160, 170), 10)
circle(screen, (225, 0, 0), (240, 175), 20)
circle(screen, (0, 0, 0), (240, 175), 10)
polygon(screen, (0, 0, 0), [(130, 130), (190, 140), (185, 145), (125, 135)])
polygon(screen, (0, 0, 0), [(210, 160), (270, 150), (275, 145), (215, 155)])
polygon(screen, (0, 0, 0), [(160, 250), (240, 250), (240, 260), (160, 260)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
