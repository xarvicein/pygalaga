import pygame
from pygame import SurfaceType

from pygalaga.utils import load_asset
from pygalaga.config import WIDTH, HEIGHT
from .sounds import Sounds
from .bullet import Bullet


class Ship:
    def __init__(self):
        self.image = load_asset("ship.png", (50, 50))
        self.x = WIDTH // 2
        self.y = HEIGHT - 70
        self.speed = 5
        self.bullets = []
        self.last_shot_time = 0
        self.shoot_delay = 500
        self.sounds = Sounds()

    def move(self, direction) -> None:
        if direction == "left" and self.x > 0:
            self.x -= self.speed
        if direction == "right" and self.x < WIDTH - 50:
            self.x += self.speed

    def shoot(self) -> None:
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= self.shoot_delay:
            self.bullets.append(Bullet(self.x + 20, self.y))
            self.last_shot_time = current_time
            self.sounds.shoot.play()

    def draw(self, screen: SurfaceType) -> None:
        screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullets:
            bullet.draw(screen)
