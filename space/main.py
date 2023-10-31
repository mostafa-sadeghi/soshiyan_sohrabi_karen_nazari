import pygame
from constants import *
from enemy import Enemy
from player import Player

pygame.init()

player_bullet_group = pygame.sprite.Group()
my_player = Player(player_bullet_group)

level_number = 0

enemy_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()


def start_new_level():
    global level_number
    level_number += 1
    for row in range(4):
        for col in range(15):
            enemy = Enemy(col * 64 + 300, row*64, enemy_bullet_group)
            enemy_group.add(enemy)


def shift_enemies():
    pass


def check_collisions():
    if pygame.sprite.groupcollide(player_bullet_group, enemy_group, True, True):
        pass


start_new_level()
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                my_player.fire()
    main_screen.fill((0, 0, 0))
    check_collisions()
    my_player.move()
    my_player.draw(main_screen)
    player_bullet_group.draw(main_screen)
    player_bullet_group.update()
    enemy_group.update()
    enemy_group.draw(main_screen)
    pygame.display.update()
    clock.tick(FPS)
