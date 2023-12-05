import pygame
from pygame.sprite import Sprite

class Player(Sprite):
    def __init__(self, x,y):
        super().__init__()
        img = pygame.image.load("assets/boy/Idle (1).png")
        self.image = pygame.transform.scale(img, (img.get_width() * 0.2, img.get_height() * 0.2))
        self.rect = self.image.get_rect(topleft=(x,y))
        self.vel_y = 0
        self.speed = 5

    def update(self):
        dx = 0
        dy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            dx -= self.speed
        if keys[pygame.K_RIGHT]:
            dx += self.speed


