import pygame
import random
import game_config as gc
from scores import ScoreBanner

class PowerUps(pygame.sprite.Sprite):
  def __init__(self, game, assets, groups):
    super().__init__()
    self.game = game
    self.assets = assets
    self.powerup_images = self.assets.power_up_images

    self.groups = groups
    self.groups['Power_Ups'].add(self)


  def randomly_select_power_up():
    pass

  def power_up_collected():
    pass

  def shield():
    pass

  def freeze():
    pass

  def explosion():
    pass

  def extra_life():
    pass

  def power():
    pass

  def special():
    pass

  def fortify():
    pass

  def update():
    pass

  def draw():
    pass