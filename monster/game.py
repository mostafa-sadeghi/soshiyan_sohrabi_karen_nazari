from random import randint
import pygame

from config import WINDOW_HEIGHT, WINDOW_WIDTH
from monster import Monster


class Game:
    def __init__(self, player, monster_group) -> None:
        self.score = 0
        self.round_number = 0
        self.font = pygame.font.Font("assets/Abrushow.ttf", 24)
        self.player = player
        self.monster_group = monster_group
        blue_monster = pygame.image.load("assets/blue_monster.png")
        green_monster = pygame.image.load("assets/green_monster.png")
        yellow_monster = pygame.image.load("assets/yellow_monster.png")
        purple_monster = pygame.image.load("assets/purple_monster.png")
        self.target_monster_images = [
            blue_monster, green_monster, yellow_monster, purple_monster]
        self.target_monster_type = randint(0, 3)
        self.target_monster_image = self.target_monster_images[self.target_monster_type]
        self.target_monster_rect = self.target_monster_image.get_rect()
        self.target_monster_rect.bottom = 100
        self.target_monster_rect.centerx = WINDOW_WIDTH/2

    def draw(self, display_surface):
        COLORS = [
            (31, 193, 241),
            (74, 202, 61),
            (245, 176, 18),
            (240, 97, 254),
        ]
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
        display_surface.blit(self.target_monster_image,
                             self.target_monster_rect)
        pygame.draw.rect(display_surface, COLORS[self.target_monster_type],
                         (0, 100, WINDOW_WIDTH, WINDOW_HEIGHT - 200), 5)

    def start_new_round(self):
        self.round_number += 1
        for i in range(self.round_number):
            self.monster_group.add(
                Monster
                (
                    randint(0, WINDOW_WIDTH - 64),
                    randint(100, WINDOW_HEIGHT - 100),
                    self.target_monster_images[0],
                    0
                )
            )
            self.monster_group.add(Monster(randint(0, WINDOW_WIDTH - 64),
                                           randint(100, WINDOW_HEIGHT - 164), self.target_monster_images[1], 1))
            self.monster_group.add(
                Monster(randint(0, WINDOW_WIDTH - 64),
                        randint(100, WINDOW_HEIGHT - 164),
                        self.target_monster_images[2], 2
                        )
            )
            self.monster_group.add(
                Monster(randint(0, WINDOW_WIDTH - 64),
                        randint(100, WINDOW_HEIGHT - 164),
                        self.target_monster_images[3], 3
                        )
            )

    def check_collisions(self):
        collided_monster = pygame.sprite.spritecollideany(
            self.player, self.monster_group)
        if collided_monster:
            print("collides", collided_monster.type)
            # TODO"""
            # در صورت برخورد بازیکن به مانستر صحیح صدای مناسبی پلی شود و نیز امتیاز داده شود

            # در غیر اینصورت از جان بازیکن کم شود و صدای دیگری اجرا شود
            # """
