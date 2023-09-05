from random import choice, randint
from pygame.sprite import Sprite
import pygame


class Monster(Sprite):
    def __init__(self, x, y, image, monster_type):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft(x, y)
        self.type = monster_type

        self.dx = choice((-1, 1))
        self.dy = choice((-1, 1))

        self.velocity = randint(1, 5)
