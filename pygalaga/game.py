import random
import pygame
from pygame import SurfaceType

from pygalaga.config import WIDTH, HEIGHT
from pygalaga.components import Ship, AlienRed, Sounds


class GamePlay:
    def __init__(self, screen):
        self.screen = screen
        self.player = Ship()
        self.enemies = [
            AlienRed(random.randint(0, WIDTH - 40), random.randint(-100, -40))
            for _ in range(2)
        ]

        self.clock = pygame.time.Clock()
        self.sounds = Sounds()
        self.running = True

    def handle_key_pad_controls(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move("left")
        if keys[pygame.K_RIGHT]:
            self.player.move("right")
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            self.player.shoot()

    def draw_bullets(self):
        for bullet in self.player.bullets[:]:
            bullet.move()
            if bullet.y < 0:
                self.player.bullets.remove(bullet)

    def draw_enemies(self):
        for enemy in self.enemies[:]:
            enemy.move()
            if enemy.y > HEIGHT:
                self.enemies.remove(enemy)
                self.enemies.append(
                    AlienRed(random.randint(0, WIDTH - 40), random.randint(-100, -40))
                )

    def detect_bullet_enemy_collision(self):
        for bullet in self.player.bullets[:]:
            for enemy in self.enemies[:]:
                if (
                    enemy.x < bullet.x < enemy.x + 40
                    and enemy.y < bullet.y < enemy.y + 40
                ):
                    self.player.bullets.remove(bullet)
                    enemy.exploding = True
                    enemy.explosion_time = pygame.time.get_ticks()
                    self.sounds.explosion.play()

    def destroy_enemies_after_collision(self):
        for enemy in self.enemies[:]:
            if enemy.exploding and pygame.time.get_ticks() - enemy.explosion_time > 500:
                self.enemies.remove(enemy)
                self.enemies.append(
                    AlienRed(random.randint(0, WIDTH - 40), random.randint(-100, -40))
                )

    def start_game_loop(self):
        while self.running:
            self.screen.fill((0, 0, 0))  # Clear screen
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.handle_key_pad_controls()
            self.draw_bullets()
            self.draw_enemies()
            self.detect_bullet_enemy_collision()
            self.destroy_enemies_after_collision()

            self.player.draw(self.screen)
            for enemy in self.enemies:
                enemy.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(30)


def main():
    pygame.init()

    screen: SurfaceType = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Galaga")

    game_play = GamePlay(screen)
    game_play.start_game_loop()

    pygame.quit()


if __name__ == "__main__":
    main()
