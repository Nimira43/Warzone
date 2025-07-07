import pygame
import game_config as gc

class StartScreen:
  def __init__(self, main, assets):
    self.main = main
    self.assets = assets
    self.start_y = gc.SCREENHEIGHT
    self.end_y = 0
    self.image = self.assets.start_screen
    self.rect = self.image.get_rect(topleft=(0, self.start_y))
    self.x, self.y = self.rect.topleft
    self.speed = gc.SCREEN_SCROLL_SPEED

  def input(self):
    pass

  def update(self):
    pass

  def draw(self, window):
    pass

  def _switch_options_main_menu(self, num):
    pass

  def _selected_option_action(self):
    pass

  def _animate_screen_into_position(self):
    pass

  def _complete_screen_position(self):
    pass