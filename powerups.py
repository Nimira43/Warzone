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

    self.power_up = self.randomly_select_power_up()

  def randomly_select_power_up(self):
    powerups = list(gc.POWER_UPS.keys())
    selected_powerup = random.choice(powerups)
    return selected_powerup

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