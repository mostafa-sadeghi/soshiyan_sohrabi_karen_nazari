import pygame
from constants import *
from enemy import Enemy
from player import Player

pygame.init()

font = pygame.font.Font("assets/Facon.ttf",22)
font32 = pygame.font.Font("assets/Facon.ttf",32)


player_bullet_group = pygame.sprite.Group()
my_player = Player(player_bullet_group)

level_number = 0
score = 0
enemy_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()
winning_status = False
winning_time = pygame.time.get_ticks()
def start_new_level():
    global level_number
    level_number += 1
    for row in range(5):
        for col in range(15):
            enemy = Enemy(col * 64 + 300, (row + 2)*64, enemy_bullet_group)
            enemy_group.add(enemy)

def reset():
    global level_number, score
    enemy_group.empty()
    level_number -= 1
    


def shift_enemies():

    shift = False
    for enemy in enemy_group:
        if enemy.rect.right >= SCREEN_WIDTH or enemy.rect.left <= 0:
            shift = True
    if shift:
        breach = False
        for enemy in enemy_group:
            enemy.direction = -1 * enemy.direction
            enemy.rect.y += level_number * 30
            if enemy.rect.bottom >= SCREEN_HEIGHT - 100:
                breach = True
        if breach:
            my_player.lives -= 1
            reset()



def draw_text():
    level_text = font.render(f'Level {level_number}', True, (255,10,220))
    level_rect = level_text.get_rect(topright = (SCREEN_WIDTH, 0))
    main_screen.blit(level_text, level_rect)

def check_collisions():
    global score, level_number, winning_status, winning_time
    if pygame.sprite.groupcollide(player_bullet_group, enemy_group, True, True):
        score += 1
    if len(enemy_group) == 0:
        if not winning_status:
            winning_time = pygame.time.get_ticks()
            winning_status = True

        if pygame.time.get_ticks() - winning_time < 4000:        
            level_text = font32.render(f'Level {level_number+1}', True, (255,10,220))
            
            level_rect = level_text.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
            main_screen.blit(level_text, level_rect)
            
        elif winning_status:
            start_new_level()
            
            winning_status = False
        

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
    shift_enemies()
    draw_text()
    my_player.move()
    my_player.draw(main_screen)
    player_bullet_group.update()
    player_bullet_group.draw(main_screen)
    enemy_bullet_group.update()
    enemy_bullet_group.draw(main_screen)
    enemy_group.update()
    enemy_group.draw(main_screen)
    pygame.display.update()
    clock.tick(FPS)
