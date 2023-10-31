import pygame
from pygame.sprite import Sprite


class Enemy(Sprite):
    def __init__(self, x, y, bullet_group):
        super().__init__()
        self.image = pygame.image.load("assets/alien.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = 1
        self.speed = 3

    def update(self):
        self.rect.x += self.direction * self.speed

    def fire(self):
        pass
