from pygame.mixer import SoundType
from pygalaga.utils import load_sound


class Sounds:
    def __init__(self):
        self.shoot: SoundType = load_sound("shoot.mp3")
        self.explosion: SoundType = load_sound("explosion.mp3")
