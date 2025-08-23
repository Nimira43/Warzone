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
    self.rect.y -= 1
    if pygame.time.get_ticks() - self.timer >= 1000:
      self.kill()

  def draw(self, window):
    window.blit(self.image, self.rect)