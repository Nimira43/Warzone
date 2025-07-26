import pygame
import game_config as gc

class TileType(pygame.sprite.Sprite):
  def __init__(self, pos, group, map_tile):
    super().__init__(group)
    self.group = group
    self.images = map_tile
    self.xPos = pos[0]
    self.yPos = pos[1]

  def update(self):
    pass

  def _get_rect_and_size(self, position):
    self.rect = self.image.get_rect(topleft = position)
    self.width, self.height = self.image.get_size()

  def hit_by_bullet(self, bullet):
    pass

  def draw(self, window):
    pass

class BrickTile(TileType):
  def __init__(self, pos, group, map_tile):
    pass

  def hit_by_bullet(self, bullet):
    pass

class SteelTile(TileType):
  def __init__(self, pos, group, map_tile):
    pass

  def hit_by_bullet(self, bullet):
    pass

class ForestTile(TileType):
  def __init__(self, pos, group, map_tile):
    pass

class IceTile(TileType):
  def __init__(self, pos, group, map_tile):
    pass

class WaterTile(TileType):
  def __init__(self, pos, group, map_tile):
    pass

  def update(self):
    pass
