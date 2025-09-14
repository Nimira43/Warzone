import pygame
import game_config as gc
from game_assets import GameAssets
from game import Game
from leveleditor import LevelEditor
from levels import LevelData
from startscreen import StartScreen

class Main:
  def __init__(self):
    pygame.init()
    pygame.mixer.init()
    self.screen = pygame.display.set_mode((gc.SCREENWIDTH, gc.SCREENHEIGHT))
    pygame.display.set_caption('Warzone')
    
    self.Clock = pygame.time.Clock()
    self.run = True
    self.assets = GameAssets()
    self.levels = LevelData()

    self.start_screen = StartScreen(self, self.assets)
    self.start_screen_active = True
 
    self.game_on = False
    # self.game = Game(self, self.assets, True, True)
    self.game = None

    self.level_editor_on = False
    # self.level_creator = LevelEditor(self, self.assets)
    self.level_creator = None

  def run_game(self):
    while self.run:
      self.input()
      self.update()
      self.draw()

  def input(self):
    if self.game_on:
      self.game.input()
    if self.start_screen_active:
      self.start_screen_active = self.start_screen.input()
    if self.level_editor_on:
      self.level_creator.input()
    if not self.game_on and not self.level_editor_on and not self.start_screen_active:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.run = False

  def update(self):
    self.Clock.tick(gc.FPS)
    if self.start_screen_active:
      self.start_screen.update()

    if self.game_on:
      self.game.update()

    if self.game:
      if self.game.end_game == True:
        self.start_screen = StartScreen(self, self.assets)
        self.start_screen_active = True
        self.game_on = False
        self.game = None
    
    if self.level_editor_on:
      self.level_creator.update()

    if self.level_creator:
      if self.level_creator.active == False:
        self.start_screen = StartScreen(self, self.assets)
        self.start_screen_active = True
        self.level_editor_on = False
        self.level_creator = None

  def draw(self):
    self.screen.fill(gc.BLACK)
    if self.start_screen_active:
      self.start_screen.draw(self.screen)
    if self.game_on:
      self.game.draw(self.screen)
    if self.level_editor_on:
      self.level_creator.draw(self.screen)
    pygame.display.update()

  def start_new_game(self, player1, player2):
    self.game_on = True
    self.game = Game(self, self.assets, player1, player2)
    self.start_screen_active = False
    return

  def start_level_creator(self):
    self.level_editor_on = True
    self.level_creator = LevelEditor(self, self.assets)
    self.start_screen_active = False

if __name__== '__main__':
  warzone = Main()
  warzone.run_game()
  pygame.quit()
