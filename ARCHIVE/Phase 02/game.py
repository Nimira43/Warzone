import pygame
import game_config

class Game:
    def __init__(self, main, assets):
        self.main = main
        self.assets = assets

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.main.run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.main.run = False

    def update(self):
        print('game running')

    def draw(self, window):
        pass