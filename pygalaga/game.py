import random
import pygame
from pygame import SurfaceType

from pygalaga.config import *
from pygalaga.components import Ship, AlienRed, Sounds


def main():
    pygame.init()

    screen: SurfaceType = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Galaga")

    player = Ship()
    enemies = [AlienRed(random.randint(0, WIDTH - 40), random.randint(-100, -40)) for _ in range(2)]
    running = True
    clock = pygame.time.Clock()
    sounds = Sounds()

    while running:
        screen.fill((0, 0, 0))  # Clear screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move("left")
        if keys[pygame.K_RIGHT]:
            player.move("right")
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            player.shoot()

        # Move and draw bullets
        for bullet in player.bullets[:]:
            bullet.move()
            if bullet.y < 0:
                player.bullets.remove(bullet)

        # Move and draw enemies
        for enemy in enemies[:]:
            enemy.move()
            if enemy.y > HEIGHT:
                enemies.remove(enemy)
                enemies.append(AlienRed(random.randint(0, WIDTH - 40), random.randint(-100, -40)))

        # Collision detection
        for bullet in player.bullets[:]:
            for enemy in enemies[:]:
                if enemy.x < bullet.x < enemy.x + 40 and enemy.y < bullet.y < enemy.y + 40:
                    player.bullets.remove(bullet)
                    enemy.exploding = True
                    enemy.explosion_time = pygame.time.get_ticks()
                    sounds.explosion.play()

        for enemy in enemies[:]:
            if enemy.exploding and pygame.time.get_ticks() - enemy.explosion_time > 500:
                enemies.remove(enemy)
                enemies.append(AlienRed(random.randint(0, WIDTH - 40), random.randint(-100, -40)))

        # Draw objects
        player.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
