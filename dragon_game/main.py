from random import randint
import pygame
pygame.init()


WINDOW_WIDTH = 600
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
bg_music = pygame.mixer.Sound("Bad Piggies Theme.mp3")
bg_music.play(-1)

# TODO   لود کردن صداهای موفقیت و از دست دادن  -  فقط لود کردن

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

    # TODO   اضافه کردن جهت پایین

    if dragon_food_rect.x < 0:
        # TODO  پلی کردن صدای از دست دادن
        dragon_food_rect.center = (
            WINDOW_WIDTH + 50, randint(150,
                                       WINDOW_HEIGHT
                                       - 30))

    dragon_food_rect.x -= dragon_food_velocity

    display_surface.blit(title_text, title_rect)
    display_surface.blit(score_text, score_text_rect)
    display_surface.blit(lives_text, lives_text_rect)

    display_surface.blit(player, player_rect)
    display_surface.blit(dragon_food, dragon_food_rect)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
