import pygame
from pygame.sprite import Sprite
from constants import *
from playerBullet import PlayerBullet
class Player(Sprite):
    def __init__(self, bullet_group):
        super().__init__()
        self.image = pygame.image.load('assets/player_ship.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = SCREEN_HEIGHT
        self.rect.centerx = SCREEN_WIDTH/2
        self.bullet_group = bullet_group
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        pass

    def fire(self):
        PlayerBullet(self.rect.centerx, self.rect.top, self.bullet_group)
