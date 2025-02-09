import pygame

from pygalaga.utils import get_asset_path


class AlienRed:
    enemy_img = pygame.image.load(get_asset_path("space_invader_red.png"))
    ALIEN_RED = pygame.transform.scale(enemy_img, (40, 40))
    def __init__(self, x, y):
        self.image = AlienRed.ALIEN_RED
        self.x = x
        self.y = y
        self.speed = 2

    def move(self):
        self.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
