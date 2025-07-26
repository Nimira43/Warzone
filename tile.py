import pygame
import game_config as gc

class TileType(pygame.sprite.Sprite):
  def __init__(self, pos, group, map_tile):
    pass

  def update(self):
    pass

  def _get_rect_and_size(self, position):
    pass

  def hit_by_bullet(self, bullet):
    pass

  def draw(self, window):
    pass

class BrickTile(TileType):
  pass

class SteelTile(TileType):
  pass

class ForestTile(TileType):
  pass

class IceTile(TileType):
  pass

class WaterTile(TileType):
  pass
