import sys
import pygame
import functions as fs
from snake import Snake
import game_settings
from score import Score

def run_game():
    pygame.init()
    
    pygame.mouse.set_visible(False)

    if len(sys.argv) == 2 :
        if sys.argv[1] == '1080p':
            screen = pygame.display.set_mode((1920, 1080))            
        elif sys.argv[1] == '720p':
            screen = pygame.display.set_mode((1280, 720))            
    else:
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            
    pygame.display.set_caption("SNAKE")
    settings = game_settings.Settings()
    snake = Snake(screen, settings)
    score = Score(settings, screen)
    blocks = fs.create_blocks(settings.block_number, screen, settings)
    game_pause = [False]
    while True:
        fs.check_events(snake, score, game_pause)
        if not game_pause[0]:
            snake.move()
            if snake.check_block_collisions(blocks):
                score.update()
            if snake.bad_collision():
                blocks = []
                score.reset()
            if not blocks:
                blocks = fs.create_blocks(settings.block_number, 
                    screen, settings)
        fs.update_screen(settings, screen, snake, blocks, score)
        


##########################################################################
run_game()
