import pygame
import random
from py.utils import get_asset_path

# Game Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# Player Class
class Player:
    player_img = pygame.image.load(get_asset_path("ship.png"))
    SHIP = pygame.transform.scale(player_img, (50, 50))
    def __init__(self):
        self.image = Player.SHIP
        self.x = WIDTH // 2
        self.y = HEIGHT - 70
        self.speed = 5
        self.bullets = []

    def move(self, direction):
        if direction == "left" and self.x > 0:
            self.x -= self.speed
        if direction == "right" and self.x < WIDTH - 50:
            self.x += self.speed

    def shoot(self):
        bullet = Bullet(self.x + 20, self.y)
        self.bullets.append(bullet)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullets:
            bullet.draw(screen)


# Enemy Class
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


# Bullet Class
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

def main():
    # Initialize Pygame
    pygame.init()
    # Create Game Window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Galaga")

    player = Player()
    enemies = [AlienRed(random.randint(0, WIDTH - 40), random.randint(-100, -40)) for _ in range(6)]
    running = True
    clock = pygame.time.Clock()

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
        if keys[pygame.K_SPACE]:
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
