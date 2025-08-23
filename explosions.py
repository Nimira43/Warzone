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
    self.frame_index = 1
    self.images = self.assets.explosions
    self.image = self.images['explode_1']
    self.rect = self.image.get_rect(center=self.pos)
    self.anim_timer = pygame.time.get_ticks()

  def update(self):
    if pygame.time.get_ticks() - self.anim_timer >= 100:
      self.frame_index += 1

  def draw(self, window):
    pass