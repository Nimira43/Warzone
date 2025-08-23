import pygame
from explosions import Explosion
import game_config as gc

class Eagle(pygame.sprite.Sprite):
  def __init__(self, game, assets, groups):
    super().__init__()
    self.game = game
    self.assets = assets
    self.group = groups
    self.group['Eagle'].add(self)
    self.active = True
    self.timer = pygame.time.get_ticks()
    self.image = self.assets.flag['Phoenix_Alive']
    self.rect = self.image.get_rect(topleft=(gc.FLAG_POSITION))

  def update(self):
    pass

  def draw(self, window):
    pass

  def destroy_base(self):
    pass