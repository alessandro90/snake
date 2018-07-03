import pygame

class Score(object):
    def __init__(self, game_settings, screen):
        self.screen = screen
        self.screen_res = game_settings.screen_res
        self.height = game_settings.score_bar_height
        self.current = 0
        try:
            with open('.score', 'r') as f:
                try:
                    self.best = int(f.read())
                except ValueError:
                    self.best = 0
        except FileNotFoundError:
            self.best = 0
        self.previous_best = self.best
        self.color = game_settings.score_color
        self.bg_color = game_settings.bg_score_color
        self.font = pygame.font.SysFont(None, 
            game_settings.score_fontsize)

    def update(self):
        self.current += 10
        if self.current > self.best:
            self.best = self.current

    def reset(self):
        self.current = 0

    def save_best(self):
        if self.best > self.previous_best:
            with open('.score', 'w') as f:
                f.write(str(self.best))

    def render(self):
        self.printable_current = self.font.render(
            'SCORE: ' + '{:,}'.format(self.current), True, self.color, 
            self.bg_color)
        self.printable_current_rect = self.printable_current.get_rect()
        self.printable_current_rect.topleft = (50, self.height // 3)

        self.printable_best = self.font.render(
            'BEST: ' + '{:,}'.format(self.best), True, 
            self.color, self.bg_color)
        self.printable_best_rect = self.printable_best.get_rect()
        self.printable_best_rect.topright = (self.screen_res[1] - 50, 
            self.height // 3)

    def draw(self):
        self.render()
        self.screen.fill(self.bg_color, pygame.Rect(0, 0, self.screen_res[1], 
            self.height))
        self.screen.blit(self.printable_current, self.printable_current_rect)
        self.screen.blit(self.printable_best, self.printable_best_rect)

