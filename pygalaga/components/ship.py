import time

import pygame

from pygalaga.utils import get_asset_path
from .bullet import Bullet
from pygalaga.config import WIDTH, HEIGHT

class Ship:
    player_img = pygame.image.load(get_asset_path("ship.png"))
    SHIP = pygame.transform.scale(player_img, (50, 50))
    def __init__(self):
        self.image = Ship.SHIP
        self.x = WIDTH // 2
        self.y = HEIGHT - 70
        self.speed = 5
        self.bullets = []
        self.last_shot_time = 0
        self.shoot_delay = 500

    def move(self, direction):
        if direction == "left" and self.x > 0:
            self.x -= self.speed
        if direction == "right" and self.x < WIDTH - 50:
            self.x += self.speed

    def shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= self.shoot_delay:
            self.bullets.append(Bullet(self.x + 20, self.y))
            self.last_shot_time = current_time

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullets:
            bullet.draw(screen)

