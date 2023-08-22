from random import choice
import pygame
pygame.init()


WINDOW_WIDTH = 967
WINDOW_HEIGHT = 655
main_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

FPS = 60
YELLOW = (248, 231, 28)
BLUE = (1, 175, 209)


clock = pygame.time.Clock()

bg_image = pygame.image.load("catch_the_clown\\background.png")
bg_rect = bg_image.get_rect()
bg_rect.topleft = (0, 0)

clown_image = pygame.transform.scale(
    pygame.image.load("catch_the_clown\\Clown.png"), (80, 80))
clown_rect = clown_image.get_rect()
clown_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)

dx = choice([-1, 1])
dy = choice([-1, 1])
clown_v = 5
score = 0

font = pygame.font.SysFont("Arial", 32)
score_text = font.render(f'Score: {score}', False, (255, 0, 0))
score_rect = score_text.get_rect()
score_rect.topleft = (32, 10)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if clown_rect.collidepoint(event.pos):
                clown_v += .5
                score += 1

    clown_rect.x += dx * clown_v
    clown_rect.y += dy * clown_v

    if clown_rect.left <= 0 or clown_rect.right >= WINDOW_WIDTH:
        dx *= -1

    if clown_rect.top <= 0 or clown_rect.bottom >= WINDOW_HEIGHT:
        dy *= -1

    score_text = font.render(f'Score: {score}', False, (255, 0, 0))


    main_surface.blit(bg_image, bg_rect)
    main_surface.blit(clown_image, clown_rect)
    main_surface.blit(score_text, score_rect)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
