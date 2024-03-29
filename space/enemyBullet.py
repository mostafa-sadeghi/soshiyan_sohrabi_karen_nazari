from pygame.sprite import Sprite
import pygame
from constants import *

class EnemyBullet(Sprite):
    def __init__(self, x, y, bullet_group):
        super().__init__()
        self.image = pygame.image.load("assets/red_laser.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        bullet_group.add(self)

    def update(self):
        self.rect.y += 5
        if self.rect.top >= SCREEN_HEIGHT:
            self.kill()