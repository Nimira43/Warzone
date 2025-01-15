import pygame
import gameconfig as gc
from game_assets import GameAssets
from game import Game
from leveleditor import LevelEditor

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((gc.SCREENWIDTH, gc.SCREENHEIGHT))
        pygame.display.set_caption('Warzone')
        self.Clock = pygame.time.Clock()
        self.run = True
        self.assets = GameAssets()

        self.game_on = False
        self.game = Game(self, self.assets, True, True)

        self.level_editor_on = True
        self.level_creator = LevelEditor(self, self.assets)

    def run_game(self):
        while self.run:
            self.input()
            self.update()
            self.draw()

    def input(self):
        if self.game_on:
            self.game.input()
        if self.level_editor_on:
            self.level_creator.input()
        if not self.game_on and not self.level_editor_on:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

    def update(self):
        self.Clock.tick(gc.FPS)
        if self.game_on:
            self.game.update()
        if self.level_editor_on:
            self.level_creator.update()

    def draw(self):
        self.screen.fill(gc.BLACK)
        if self.game_on:
            self.game.draw(self.screen)
        if self.level_editor_on:
            self.level_creator.draw(self.screen)
        pygame.display.update()

if __name__== '__main__':
    warzone = Main()
    warzone.run_game()
    pygame.quit()


