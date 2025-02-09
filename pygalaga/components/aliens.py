from pygalaga.utils import load_asset


class AlienRed:
    def __init__(self, x, y) -> None:
        self.image = load_asset("space_invader_red.png", (40, 40))
        self.x = x
        self.y = y
        self.speed = 2

    def move(self) -> None:
        self.y += self.speed

    def draw(self, screen) -> None:
        screen.blit(self.image, (self.x, self.y))
