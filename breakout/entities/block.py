import pygame
import random
from . import ENTITY_COLOR


class Block(pygame.sprite.Sprite):
    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        color: pygame.Color | str | tuple[int, int, int],
        *groups
    ):
        super().__init__(*groups)

        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_frect(topleft=(x, y))
        self.color = color

        self.image.fill(self.color)

    @staticmethod
    def generate(
        blocks_area: pygame.Rect,
        bound_rect: pygame.Rect,
        gap: int,
        rows: int,
        cols: int,
    ) -> pygame.sprite.Group:
        block_width = (blocks_area.width - (cols - 1) * gap) // cols
        block_height = (blocks_area.height - (rows - 1) * gap) // rows

        total_width = block_width * cols + (cols - 1) * gap
        total_height = block_height * rows + (rows - 1) * gap

        blocks_area.width = total_width
        blocks_area.height = total_height
        blocks_area.centerx = bound_rect.centerx
        blocks_area.centery = bound_rect.centery // 2

        blocks = pygame.sprite.Group()
        colors = list(pygame.colordict.THECOLORS.values())

        for r in range(rows):
            for c in range(cols):
                block = Block(
                    blocks_area.left + c * (block_width + gap),
                    blocks_area.top + r * (block_height + gap),
                    block_width,
                    block_height,
                    random.choice(colors),
                )
                blocks.add(block)

        return blocks
