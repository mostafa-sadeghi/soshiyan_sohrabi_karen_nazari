import pygame
import random
from enemyBullet import EnemyBullet
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
        self.bullet_group = bullet_group

    def update(self):
        self.rect.x += self.direction * self.speed
        self.fire()

    def fire(self):
        if random.randint(1,1000) > 999 and len(self.bullet_group) < 3:
            EnemyBullet(self.rect.centerx, self.rect.bottom, self.bullet_group)

