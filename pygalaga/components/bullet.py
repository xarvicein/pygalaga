from pygalaga.utils import load_asset


class Bullet:
    def __init__(self, x, y) -> None:
        self.image = load_asset("missile.png", (10, 20))
        self.x = x
        self.y = y
        self.speed = 7

    def move(self) -> None:
        self.y -= self.speed

    def draw(self, screen) -> None:
        screen.blit(self.image, (self.x, self.y))
