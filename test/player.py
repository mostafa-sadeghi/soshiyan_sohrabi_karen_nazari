import pygame
from pygame.sprite import Sprite
from config import WINDOW_WIDTH, WINDOW_HEIGHT


class Player(Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(
            bottom=WINDOW_HEIGHT, centerx=WINDOW_WIDTH/2)

        self.velocity = 5
        self.lives = 3
