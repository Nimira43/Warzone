import pygame
import game_config as gc

class Fade:
  def __init__(self, game, assets, speed = 5):
    self.game = game
    self.level = self.game.level_num - 1
    self.assets = assets
    self.images = self.assets.hud_images
    self.speed = speed
    self.fade_active = False

  def update(self):
    pass

  def draw(self, window):
    pass

  def move_y_fade(self, ycoord, start_pos, end_pos, speed):
    pass

  def create_stage_image(self):
    pass

