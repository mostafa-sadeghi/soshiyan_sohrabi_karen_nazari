import pygame
from config import WINDOW_WIDTH, WINDOW_HEIGHT
from player import Player

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


FPS = 60
clock = pygame.time.Clock()
player_group = pygame.sprite.Group()
player = Player("player.png")
player_group.add(player)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player_group.draw(display_surface)

    pygame.display.update()

pygame.quit()
