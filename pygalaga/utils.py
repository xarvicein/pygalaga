import os
import pygame
from functools import cache
from pygame.mixer import SoundType


@cache
def load_asset(asset: str, size: tuple[int,int]):
    asset_img = pygame.image.load(get_asset_path(asset))
    return pygame.transform.scale(asset_img, size)

def load_sound() -> SoundType:
    return pygame.mixer.Sound(get_sound_path("shoot.mp3"))

def get_asset_path(filename):
    return os.path.join(os.path.dirname(__file__), "assets", filename)

def get_sound_path(filename):
    return os.path.join(os.path.dirname(__file__), "assets/sounds", filename)