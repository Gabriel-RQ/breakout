import pygame
import random

from entities import Block, Paddle


def generate_blocks(
    blocks_area: pygame.Rect, bounding_area: pygame.Rect
) -> list[Block]:
    return Block.generate(
        blocks_area,
        bounding_area,
        random.randrange(2, 10),
        random.randrange(5, 20),
        random.randrange(10, 35),
    )


def spawn_player(x: int, y: int, speed: int) -> Paddle:
    return Paddle(x, y, 100, 20, speed)
