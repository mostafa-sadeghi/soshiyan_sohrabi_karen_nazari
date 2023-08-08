from random import randint
import pygame
pygame.init()


WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
BLACK = (0, 0, 0)

PLAYER_STARTING_LIVES = 5
PLAYER_VELOCITY = 10
DRAGON_FOOD_VELOCITY = 10
DRAGON_ACCELERATION = 0.5

FPS = 60
clock = pygame.time.Clock()

score = 0
player_lives = PLAYER_STARTING_LIVES
dragon_food_velocity = DRAGON_FOOD_VELOCITY

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Game one!!!")

dragon_left_image = pygame.image.load("dragon_left.png")
dragon_left_rect = dragon_left_image.get_rect()
dragon_left_rect.topleft = (0, 0)


dragon_right_image = pygame.image.load("dragon_right.png")
dragon_right_rect = dragon_right_image.get_rect()
dragon_right_rect.topright = (WINDOW_WIDTH, 0)


my_font = pygame.font.Font("DragonHunter.otf", 32)
title_text = my_font.render("Feed the dragon", True, GREEN,
                            DARKGREEN)
title_rect = title_text.get_rect()
title_rect.midtop = (WINDOW_WIDTH/2, 0)


score_text = my_font.render(f"Score: {score}", False, DARKGREEN, GREEN)
score_text_rect = score_text.get_rect()
score_text_rect.centery = 64
score_text_rect.left = 128

lives_text = my_font.render(f"Lives: {player_lives}", False, GREEN, DARKGREEN)
lives_text_rect = lives_text.get_rect()
lives_text_rect.centery = 64
lives_text_rect.right = WINDOW_WIDTH - 128


gameover_text = my_font.render("gameover", False, GREEN, DARKGREEN)
gameover_text_rect = gameover_text.get_rect()
gameover_text_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)

continue_text = my_font.render(
    "Press any key to continue...", False, GREEN, DARKGREEN)
continue_text_rect = continue_text.get_rect()
continue_text_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + 50)


player = pygame.transform.flip(pygame.image.load(
    "player.png"), True, False)
player_rect = player.get_rect()
player_rect.midleft = (32, WINDOW_HEIGHT/2)


dragon_food = pygame.image.load("egg.png")
dragon_food_rect = dragon_food.get_rect()
dragon_food_rect.center = (WINDOW_WIDTH + 50,
                           randint(150,
                                   WINDOW_HEIGHT
                                   - 30))
pygame.mixer.music.load("Bad Piggies Theme.mp3")
pygame.mixer.music.play()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill(BLACK)
    display_surface.blit(dragon_left_image, dragon_left_rect)
    display_surface.blit(dragon_right_image, dragon_right_rect)

    pygame.draw.line(display_surface, WHITE, (0, 128), (WINDOW_WIDTH, 128), 4)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_rect.top > 128:
        player_rect.y -= PLAYER_VELOCITY
    if keys[pygame.K_DOWN] and player_rect.bottom < WINDOW_HEIGHT:
        player_rect.y += PLAYER_VELOCITY

    if dragon_food_rect.x < 0:
        player_lives -= 1

        dragon_food_rect.center = (
            WINDOW_WIDTH + 50, randint(150,
                                       WINDOW_HEIGHT
                                       - 30))

    dragon_food_rect.x -= dragon_food_velocity

    if player_rect.colliderect(dragon_food_rect):
        score += 1
        dragon_food_velocity += DRAGON_ACCELERATION
        dragon_food_rect.center = (
            WINDOW_WIDTH + 50, randint(150,
                                       WINDOW_HEIGHT
                                       - 30))
    score_text = my_font.render(f"Score: {score}", False, DARKGREEN, GREEN)
    lives_text = my_font.render(
        f"Lives: {player_lives}", False, GREEN, DARKGREEN)

    if player_lives == 0:
        display_surface.blit(gameover_text, gameover_text_rect)
        display_surface.blit(continue_text, continue_text_rect)
        pygame.display.update()
        pygame.mixer.music.stop()

        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

                if event.type == pygame.KEYDOWN:
                    score = 0
                    player_lives = PLAYER_STARTING_LIVES
                    player_rect.y = WINDOW_HEIGHT/2
                    dragon_food_velocity = DRAGON_FOOD_VELOCITY
                    pygame.mixer.music.play(-1)
                    is_paused = False

    display_surface.blit(title_text, title_rect)
    display_surface.blit(score_text, score_text_rect)
    display_surface.blit(lives_text, lives_text_rect)

    display_surface.blit(player, player_rect)
    display_surface.blit(dragon_food, dragon_food_rect)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
