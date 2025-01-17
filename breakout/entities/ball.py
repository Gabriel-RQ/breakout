import pygame
from . import ENTITY_COLOR


class Ball(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, radius: int, speed: int, *groups):
        super().__init__(*groups)

        self.speed = speed
        self.dirx = 0
        self.diry = 1

        self.radius = radius
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        self.rect = self.image.get_frect(center=(x, y))

        pygame.draw.circle(self.image, ENTITY_COLOR, (radius, radius), radius)

    def change_dir(self, dirx: int, diry: int):
        self.dirx = dirx
        self.diry = diry

    def move(self, dt: float):
        self.rect.x += self.dirx * self.speed * dt
        self.rect.y += self.diry * self.speed * dt

    def update(self, dt: float, bounds: pygame.Rect):
        self.move(dt)

        if self.rect.left < bounds.left:
            self.dirx = 1
        if self.rect.right > bounds.right:
            self.dirx = -1
        if self.rect.top < bounds.top:
            self.diry = 1
        if self.rect.bottom > bounds.bottom:
            self.diry = -1
