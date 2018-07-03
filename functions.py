from random import sample
import sys
import pygame
from snake import Block

def check_events(snake, score, game_pause):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                score.save_best()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    if game_pause[0]:
                        game_pause[0] = False
                    else:
                        game_pause[0] = True
                if event.key == pygame.K_ESCAPE:
                    score.save_best()
                    sys.exit()
                if event.key == pygame.K_UP and not snake.direction == 'down' \
                    and snake.moved:
                    snake.direction = 'up'
                    snake.moved = False
                if event.key == pygame.K_DOWN and not snake.direction == 'up' \
                    and snake.moved:
                    snake.direction = 'down'
                    snake.moved = False
                if event.key == pygame.K_RIGHT and not snake.direction == 'left' \
                    and snake.moved:
                    snake.direction = 'right'
                    snake.moved = False
                if event.key == pygame.K_LEFT and not snake.direction == 'right' \
                    and snake.moved:
                    snake.direction = 'left'
                    snake.moved = False                    


def create_blocks(n, screen, game_settings):
    blocks = []
    heigth, width = game_settings.screen_res
    bar_height = game_settings.score_bar_height
    size = game_settings.snake_size
    xx = sample(range(size // 2, width, size), n)
    yy = sample(range(size // 2 + bar_height, heigth, size), n)
    for x, y in zip(xx, yy):
        blocks.append(Block([x, y], screen, game_settings))
    return blocks


def update_screen(game_settings, screen, snake, blocks, score):
    pygame.time.Clock().tick(8 + score.current // 600)
    screen.fill(game_settings.bg_color)
    for block in blocks:
        block.draw()
    snake.draw()
    score.draw()
    pygame.display.flip()