import pygame
import game_config as gc
from game_assets import GameAssets
from game import Game

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((gc.SCREENWIDTH, gc.SCREENHEIGHT))
        pygame.display.set_caption('Warzone')
        self.Clock = pygame.time.Clock()
        self.run = True
        self.assets = GameAssets()

        self.game_on = True
        self.game = Game(self, self.assets)

    def run_game(self):
        while self.run:
            self.input()
            self.update()
            self.draw()

    def input(self):
        if self.game_on:
            self.game.input()

        if not self.game_on:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

    def update(self):
        self.Clock.tick(gc.FPS)
        if self.game_on:
            self.game.update()

    def draw(self):
        self.screen.fill(gc.BLACK)
        if self.game_on:
            self.game.draw(self.screen)

        pygame.display.update()

if __name__=='__main__':
    warzone = Main()
    warzone.run_game()
    pygame.quit()


