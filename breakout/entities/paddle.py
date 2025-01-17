import pygame
from . import ENTITY_COLOR


class Paddle(pygame.sprite.Sprite):
    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        speed: int,
        life: int = 3,
        *groups,
    ):
        super().__init__(*groups)

    def lose_life(self):
        pass

    def change_dir(self, dir_x: int):
        pass

    def move(self, dt: float):
        pass

    def update(self, dt: float, bounds: pygame.Rect):
        pass
