import pygame
import time
import math

from entities import *
from util import *

pygame.init()

# Set up
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout")

counter = 0

# Entities
player_speed = 400
player_y = HEIGHT - 50
player1 = spawn_player(WIDTH / 2 + 150, player_y, player_speed)
player2 = spawn_player(WIDTH / 2 - 150, player_y, player_speed)
player_group = pygame.sprite.Group(player1, player2)

ball = None
ball_group = pygame.sprite.GroupSingle()

blocks_margin = 10
blocks_area = pygame.Rect(
    blocks_margin,
    blocks_margin,
    WIDTH - blocks_margin * 2,
    HEIGHT / 2 - blocks_margin * 2,
)

blocks = generate_blocks(blocks_area, screen.get_rect())

# Font
font = pygame.font.Font(None, 24)

p1_surf = font.render("Player 1", True, ENTITY_COLOR)
p2_surf = font.render("Player 2", True, ENTITY_COLOR)
press_space_surf = font.render("Press Space to Start", True, ENTITY_COLOR)

font.set_point_size(64)
game_over_surf = font.render("Game Over", True, ENTITY_COLOR)

# Main loop
dt = 0
t1 = time.perf_counter()
playing = False
game_over = False
running = True
while running:

    t2 = time.perf_counter()
    dt = t2 - t1
    t1 = t2

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player1.change_dir(-1)
            elif event.key == pygame.K_RIGHT:
                player1.change_dir(1)
            elif event.key == pygame.K_a:
                player2.change_dir(-1)
            elif event.key == pygame.K_d:
                player2.change_dir(1)
            elif event.key == pygame.K_SPACE:
                if not playing:
                    ball = Ball(WIDTH / 2, HEIGHT / 2 + 50, 10, 500)
                    ball_group.add(ball)
                    playing = True
                if game_over:
                    counter = 0
                    player_group.empty()
                    player1 = spawn_player(WIDTH / 2 + 150, player_y, player_speed)
                    player2 = spawn_player(WIDTH / 2 - 150, player_y, player_speed)
                    player_group.add(player1, player2)
                    playing = False
                    game_over = False
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                player1.change_dir(0)
            if event.key in (pygame.K_a, pygame.K_d):
                player2.change_dir(0)

    if playing:
        # Update
        counter += dt

        player_group.update(dt, screen.get_rect())
        ball_group.update(dt, screen.get_rect())

        # Check if the ball collides with the blocks
        block_collisions = pygame.sprite.groupcollide(ball_group, blocks, False, True)
        if block_collisions:
            ball.change_dir(ball.dirx, -ball.diry)

        # Check if the ball collides with the players
        player_collisions = pygame.sprite.groupcollide(
            ball_group, player_group, False, False
        )
        if player_collisions:
            player = player_collisions[ball].pop()
            offset = ball.rect.centerx - player.rect.centerx
            max_offset = player.rect.width / 2
            ball.change_dir((offset / max_offset), -ball.diry)

        # Checks if the ball misses the paddle
        if ball.rect.bottom >= HEIGHT:
            ball.kill()
            ball = Ball(WIDTH / 2, HEIGHT / 2 + 50, 10, 500)
            ball_group.add(ball)

            p1_offset = abs(ball.rect.centerx - player1.rect.centerx)
            p2_offset = abs(ball.rect.centerx - player2.rect.centerx)

            if not player1.alive():
                player2.lose_life()
            elif not player2.alive():
                player1.lose_life()
            else:
                if p1_offset < p2_offset:
                    player1.lose_life()
                elif p2_offset < p1_offset:
                    player2.lose_life()
                else:
                    player1.lose_life()
                    player2.lose_life()

            playing = False

        for player in player_group:
            if player.life == 0:
                player.kill()

        if player1.life == 0 and player2.life == 0:
            playing = False
            game_over = True

        if len(blocks) == 0:
            blocks = generate_blocks(blocks_area, screen.get_rect())

    # Draw
    screen.fill("#16161d")

    if not game_over:
        player_group.draw(screen)
        blocks.draw(screen)
        ball_group.draw(screen)

        if playing:
            font.set_point_size(52)
            counter_surf = font.render(str(math.floor(counter)), True, ENTITY_COLOR)
            counter_surf_rect = counter_surf.get_rect(
                center=(WIDTH / 2, HEIGHT - HEIGHT / 3)
            )
            screen.blit(counter_surf, counter_surf_rect)
        else:
            press_space_surf_rect = press_space_surf.get_rect(
                center=(WIDTH / 2, HEIGHT - HEIGHT / 3)
            )
            screen.blit(press_space_surf, press_space_surf_rect)

        font.set_point_size(18)

        if player1.alive():
            p1_life_surf = font.render(str(player1.life), True, "#16161d")
            screen.blit(p1_life_surf, p1_life_surf.get_rect(center=player1.rect.center))

            # Player 1 name
            p1_surf_rect = p1_surf.get_rect(
                center=(player1.rect.centerx, player1.rect.centery + 30)
            )
            screen.blit(p1_surf, p1_surf_rect)

        if player2.alive():
            p2_life_surf = font.render(str(player2.life), True, "#16161d")
            screen.blit(p2_life_surf, p2_life_surf.get_rect(center=player2.rect.center))

            # Player 2 name
            p2_surf_rect = p2_surf.get_rect(
                center=(player2.rect.centerx, player2.rect.centery + 30)
            )
            screen.blit(p2_surf, p2_surf_rect)
    else:
        # Game over
        game_over_surf_rect = game_over_surf.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        screen.blit(game_over_surf, game_over_surf_rect)

    pygame.display.flip()

pygame.quit()
