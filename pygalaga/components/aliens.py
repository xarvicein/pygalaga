from pygalaga.utils import load_asset, load_gif_asset


class AlienRed:
    def __init__(self, x, y) -> None:
        self.image = load_asset("space_invader_red.png", (40, 40))
        self.explosion = load_gif_asset("explosion.gif", (80, 80))
        self.x = x
        self.y = y
        self.speed = 2
        self.__exploding = False
        self.explosion_time = 0
        self.explosion_index = 0

    @property
    def exploding(self):
        return self.__exploding

    @exploding.setter
    def exploding(self, val):
        self.explosion_time = 0
        self.explosion_index = 0
        self.__exploding = val

    def move(self) -> None:
        if not self.exploding:
            self.y += self.speed

    def draw(self, screen) -> None:
        if self.exploding:
            if self.explosion_index < len(self.explosion):
                screen.blit(
                    self.explosion[self.explosion_index], (self.x - 20, self.y - 20)
                )
                self.explosion_index += 1
            else:
                self.exploding = False
                self.explosion_index = 0
        else:
            screen.blit(self.image, (self.x, self.y))
