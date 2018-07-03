from collections import deque
from itertools import islice
from time import sleep
from random import choice
import pygame

class Block(object):
    def __init__(self, pos, screen, game_settings):
        self.pos = pos
        self.size = game_settings.snake_size
        self.color = choice(game_settings.snake_color)
        self.screen = screen
    
    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.pos, 
                self.size // 2, 0)


class Snake(object):
    def __init__(self, screen, game_settings):
        self.screen = screen
        self.settings = game_settings
        self.size_block = game_settings.snake_size
        self.body_color = game_settings.snake_color[0]
        self.game_settings = game_settings
        self.__get_starting_point()
        self.__initialize_block()
        self.moved = False
        self.direction = 'up'

    def __get_starting_point(self):
        h, w = self.settings.screen_res
        w -= self.size_block
        h -= self.size_block
        x = w // 2
        y = h // 2 + self.settings.score_bar_height
        x =  x // self.size_block
        y = y // self.size_block
        self.start_x = x * self.size_block + self.size_block // 2
        self.start_y = y * self.size_block + self.size_block // 2

    def __initialize_block(self):
        self.blocks = deque([
            Block([self.start_x, self.start_y], self.screen, self.settings)
        ])

    @property
    def head(self):
        return self.blocks[-1]

    @head.setter
    def head(self, block):
        self.head = block

    @property
    def length(self):
        return len(self.blocks)

    def move(self):
        pos = [0, 0]
        if self.direction == 'up':
            pos[0] = self.head.pos[0]
            pos[1] = self.head.pos[1] - self.size_block
        elif self.direction == 'down':
            pos[0] = self.head.pos[0]
            pos[1] = self.head.pos[1] + self.size_block
        elif self.direction == 'right':
            pos[0] = self.head.pos[0] + self.size_block
            pos[1] = self.head.pos[1]
        elif self.direction == 'left':
            pos[0] = self.head.pos[0] - self.size_block
            pos[1] = self.head.pos[1]
        self.blocks.append(Block(pos, self.screen, self.game_settings))
        self.blocks.popleft()
        self.moved = True

    def add_block(self, block):
        self.blocks.append(block)

    def check_block_collisions(self, blocks):
        for i, block in enumerate(blocks):
            if self.head.pos == block.pos:
                self.add_block(blocks.pop(i))
                return True
        return False

    def reset(self):
        sleep(0.5)
        self.__initialize_block()
        self.direction = 'up'

    def selfcollide(self):
        if self.length > 2:
            for block in islice(self.blocks, 0, len(self.blocks) -2):
                if block.pos == self.head.pos:
                    self.reset()
                    return True
        return False

    def bordercollide(self):
        if self.head.pos[0] <= 0 \
            or self.head.pos[0] >= self.settings.screen_res[1]:
            self.reset()
            return True
        if self.head.pos[1] <= self.settings.score_bar_height \
            or self.head.pos[1] >= self.settings.screen_res[0]:            
            self.reset()
            return True
        return False

    def bad_collision(self):
        return self.selfcollide() or self.bordercollide()

    def uniform_color(self):
        for block in self.blocks:
            block.color = self.body_color

    def draw(self):
        self.uniform_color()
        for block in self.blocks:
            block.draw()
