import pygame
from config import *
from game import Game
from player import Player
pygame.init()


display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

clock = pygame.time.Clock()
player = Player()
monster_group = pygame.sprite.Group()

game = Game(player, monster_group)
game.start_new_round()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.warp()

    display_surface.fill((0, 0, 0))
    player.draw(display_surface)
    game.draw(display_surface)
    game.check_collisions()
    monster_group.update()
    monster_group.draw(display_surface)
    player.update()
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
