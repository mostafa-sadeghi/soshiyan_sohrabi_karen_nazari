import pygame
pygame.init()


WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

dispaly_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Game one!!!")

dragon_left_image = pygame.image.load("dragon_left.png")
dragon_left_rect = dragon_left_image.get_rect()
dragon_left_rect.topleft = (0, 0)


dragon_right_image = pygame.image.load("dragon_right.png")
dragon_right_rect = dragon_right_image.get_rect()
dragon_right_rect.topright = (WINDOW_WIDTH, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dispaly_surface.blit(dragon_left_image, dragon_left_rect)
    dispaly_surface.blit(dragon_right_image, dragon_right_rect)
    pygame.display.update()

pygame.quit()
