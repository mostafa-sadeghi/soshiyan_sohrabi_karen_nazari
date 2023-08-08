from random import randint
import pygame
pygame.init()


WINDOW_WIDTH = 967
WINDOW_HEIGHT = 655
main_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

FPS = 60
YELLOW = (248, 231, 28)
BLUE = (1, 175, 209)


clock = pygame.time.Clock()

bg_image = pygame.image.load("background.png")
bg_rect = bg_image.get_rect()
bg_rect.topleft = (0, 0)

clown_image = pygame.transform.scale(pygame.image.load("Clown.png"), (80, 80))
clown_rect = clown_image.get_rect()
clown_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # TODO   حرکت دادن دلقک در جهت های رندوم
    # همسنطور دلقک نباید از صفحه خارج و در صورت خروج از صفحه برگردد

    main_surface.blit(bg_image, bg_rect)
    main_surface.blit(clown_image, clown_rect)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
