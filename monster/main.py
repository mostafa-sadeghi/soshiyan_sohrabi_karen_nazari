import pygame
from config import *
from player import Player
pygame.init()


display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

clock = pygame.time.Clock()
player = Player()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill((0, 0, 0))
    player.draw(display_surface)
    player.update()
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
