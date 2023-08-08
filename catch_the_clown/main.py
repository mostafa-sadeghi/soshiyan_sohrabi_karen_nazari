from random import randint
import pygame
pygame.init()


WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

FPS = 60
clock = pygame.time.Clock()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
