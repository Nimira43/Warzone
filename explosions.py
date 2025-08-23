import pygame
from scores import ScoreBanner

class Explosion(pygame.sprite.Sprite):
  def __init__(self, assets, group, pos, explode_type=1, score=100):
    super().__init__()
    self.assets = assets
    self.group = group
    self.explosion_group = self.group['Explosion']
    self.explosion_group.add(self)
    self.score = score
    self.pos = pos
    self.explode_type = explode_type
    

  def update(self):
    pass

  def draw(self, window):
    pass