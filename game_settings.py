import pygame

class Settings(object):
    def __init__(self):
        info = pygame.display.Info()
        self.screen_res = [info.current_h, info.current_w]
        self.bg_color = 141, 141, 141
        self.snake_color = (51, 102, 255), (255, 43, 43), (154, 255, 43), \
            (223, 43, 255), (43, 255, 240), (255, 157, 49)
        self.score_color = 0, 0, 0
        self.bg_score_color = 255, 255, 255
        if self.screen_res > [1080, 1920]:
            self.block_number = 15
            self.snake_size = 60
            self.score_bar_height = 240
            self.score_fontsize = 125
        elif self.screen_res == [1080, 1920]:
            self.block_number = 10
            self.snake_size = 40
            self.score_fontsize = 75
            self.score_bar_height = 120
        elif self.screen_res == [720, 1280]:
            self.block_number = 10
            self.snake_size = 20
            self.score_fontsize = 40
            self.score_bar_height = 60
        else:
            self.block_number = 10
            self.snake_size = 40
            self.score_fontsize = 45
            self.score_bar_height = 60