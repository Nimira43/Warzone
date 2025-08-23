import pygame

class ScoreBanner(pygame.sprite.Sprite):
  def __init__(self, assets, group, pos, score):
    super().__init__()
    self.assets = assets
    self.group = group
    self.group['Score'].add(self)
    self.pos = pos
    self.score = str(score)

  def update(self):
    pass

  def draw(self, windows):
    pass