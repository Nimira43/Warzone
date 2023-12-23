import pygame
import gameconfig as gc
from characters import Tank, PlayerTank
from game_hud import GameHud

class Game:
    def __init__(self, main, assets, player1=True, player2=False):
        self.main = main
        self.assets = assets

        self.groups = {'All_Tanks': pygame.sprite.Group()}
        self.player1_active = player1
        self.player2_active = player2

        self.hud = GameHud(self, self.assets)
        
        if self.player1_active:
            self.player1 = PlayerTank(self, self.assets, self.groups, (200, 200), 'Up', 'Gold', 0)
        if self.player2_active:
            self.player2 = PlayerTank(self, self.assets, self.groups, (400, 200), 'Up', 'Green', 1)

    def input(self):
        keypressed = pygame.key.get_pressed()
        if self.player1_active:
            self.player1.input(keypressed)
        if self.player2_active:
            self.player2.input(keypressed)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.main.run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.main.run = False

    def update(self):
        self.hud.update()
        if self.player1_active:
            self.player1.update()
        if self.player2_active:
            self.player2.update()

    def draw(self, window):
        self.hud.draw(window)
        if self.player1_active:
            self.player1.draw(window)
        if self.player2_active:
            self.player2.draw(window)