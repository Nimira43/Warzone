import pygame
import game_config as gc
from characters import Tank, PlayerTank

class Game:
    def __init__(self, main, assets):
        self.main = main
        self.assets = assets

        self.groups = {'All_Tanks': pygame.sprite.Group()}
        self.player1 = PlayerTank(self, self.assets, self.groups, (200, 200), 'Up', 'Gold', 0)
        self.player2 = PlayerTank(self, self.assets, self.groups, (400, 200), 'Up', 'Green', 1)

    def input(self):
        keypressed = pygame.key.get_pressed()
        self.player1.input(keypressed)
        self.player2.input(keypressed)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.main.run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.main.run = False

    def update(self):
        self.player1.update()
        self.player2.update()

    def draw(self, window):
        self.player1.draw(window)
        self.player2.draw(window)