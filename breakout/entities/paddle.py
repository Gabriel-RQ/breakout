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

        self.speed = speed
        self.dir_x = 0

        self.life = life

        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_frect(center=(x, y))

        self.image.fill(ENTITY_COLOR)

    def lose_life(self):
        self.life -= 1

    def change_dir(self, dir_x: int):
        self.dir_x = dir_x

    def move(self, dt: float):
        self.rect.x += self.dir_x * self.speed * dt

    def update(self, dt: float, bounds: pygame.Rect):
        self.move(dt)
        self.rect.clamp_ip(bounds)
