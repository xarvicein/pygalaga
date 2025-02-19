import os
from functools import cache
import pygame
from pygame.mixer import SoundType
from PIL import Image


@cache
def load_asset(asset: str, size: tuple[int, int]):
    asset_img = pygame.image.load(get_asset_path(asset))
    return pygame.transform.scale(asset_img, size)


@cache
def load_sound(asset: str) -> SoundType:
    return pygame.mixer.Sound(get_sound_path(asset))


@cache
def load_gif_asset(asset: str, size: tuple[int, int]):
    explosion_gif = Image.open(get_asset_path(asset))
    frames = []
    for frame in range(explosion_gif.n_frames):
        explosion_gif.seek(frame)
        frame_image = explosion_gif.convert("RGBA")
        mode = frame_image.mode
        frame_size = frame_image.size
        data = frame_image.tobytes()
        pygame_image = pygame.image.fromstring(data, frame_size, mode)
        frames.append(pygame.transform.scale(pygame_image, size))
    return frames


def get_asset_path(filename):
    return os.path.join(os.path.dirname(__file__), "assets", filename)


def get_sound_path(filename):
    return os.path.join(os.path.dirname(__file__), "assets/sounds", filename)
