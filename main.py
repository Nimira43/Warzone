import pygame
import game_config as gc
from game_assets import GameAssets

class Main:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((gc.SCREENWIDTH, gc.SCREENHEIGHT))
    pygame.display.set_caption('Warzone')
    self.Clock = pygame.time.Clock()
    self.run = True
    self.assets = GameAssets()

  def run_game(self):
    while self.run:
      self.input()
      self.update()
      self.draw()

  def input(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.run = False

  def update(self):
    self.Clock.tick(gc.FPS)

  def draw(self):
    self.screen.fill(gc.BLACK)
    # self.screen.blit(self.assets.tank_images['Tank_4']['Green']['Down'][0], (400, 400))
    pygame.display.update()

if __name__=='__main__':
  warzone = Main()
  warzone.run_game()
  pygame.quit()
