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

    self.options_positions = [
      (4 * gc.imageSize, 7.75 * gc.imageSize),
      (4 * gc.imageSize, 8.75 * gc.imageSize),
      (4 * gc.imageSize, 9.75 * gc.imageSize),
    ]

    self.token_index = 0
    self.token_image = self.assets.start_screen_token
    self.token_rect = self.token_image.get_rect(topleft=self.options_positions[self.token_index])
    self.start_screen_active = False

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