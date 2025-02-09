import pygame

from pygalaga.utils import get_asset_path


class Bullet:
    bullet_img = pygame.image.load(get_asset_path("missile.png"))
    BULLET = pygame.transform.scale(bullet_img, (10, 20))
    def __init__(self, x, y):
        self.image = Bullet.BULLET
        self.x = x
        self.y = y
        self.speed = 7

    def move(self):
        self.y -= self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
