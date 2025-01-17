import pygame
from . import ENTITY_COLOR


class Ball(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, radius: int, speed: int, *groups):
        super().__init__(*groups)

    def change_dir(self, dirx: int, diry: int):
        pass

    def move(self, dt: float):
        pass

    def update(self, dt: float, bounds: pygame.Rect):
        pass
