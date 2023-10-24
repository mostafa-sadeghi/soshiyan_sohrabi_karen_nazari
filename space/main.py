import pygame
from constants import *
from player import Player

pygame.init()
main_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player_bullet_group = pygame.sprite.Group()
my_player = Player(player_bullet_group)

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                my_player.fire()
    main_screen.fill((0, 0, 0))
    my_player.draw(main_screen)
    player_bullet_group.draw(main_screen)
    player_bullet_group.update()
    pygame.display.update()
    clock.tick(FPS)
