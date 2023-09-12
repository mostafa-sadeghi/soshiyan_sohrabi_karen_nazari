from random import randint
import pygame

from config import WINDOW_HEIGHT, WINDOW_WIDTH
from monster import Monster


class Game:
    def __init__(self, player, monster_group) -> None:
        self.score = 0
        self.round_number = 0
        self.font = pygame.font.Font("assets/Abrushow.ttf", 24)
        self.moster_group = monster_group
        blue_monster = pygame.image.load("assets/blue_monster.png")
        green_monster = pygame.image.load("assets/green_monster.png")
        yellow_monster = pygame.image.load("assets/yellow_monster.png")
        purple_monster = pygame.image.load("assets/purple_monster.png")
        self.target_monster_images = [
            blue_monster, green_monster, yellow_monster, purple_monster]

    def draw(self, display_surface):
        score_text = self.font.render(
            f"Score: {self.score}", True, (255, 255, 255))
        score_rect = score_text.get_rect()
        score_rect.topleft = (10, 10)

        round_text = self.font.render(
            f"Round: {self.round_number}", True, (255, 255, 255))
        round_rect = round_text.get_rect()
        round_rect.topright = (WINDOW_WIDTH, 10)

        display_surface.blit(score_text, score_rect)
        display_surface.blit(round_text, round_rect)

    def start_new_round(self):
        self.round_number += 1
        for i in range(self.round_number):
            self.moster_group.add(Monster(randint(0, WINDOW_WIDTH - 64), randint(
                100, WINDOW_HEIGHT - 100), self.target_monster_images[0], "blue"))
            # self.moster_group.add(Monster())
            # self.moster_group.add(Monster())
            # self.moster_group.add(Monster())
