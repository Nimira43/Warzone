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
    self.fade_in = True
    self.fade_out = False
    self.transition = False
    self.timer = pygame.time.get_ticks()
    self.top_rect = pygame.Rect(0, 0 - gc.SCREENHEIGHT // 2, gc. SCREENWIDTH, gc.SCREENHEIGHT // 2)
    self.top_rect_start_y = self.top_rect.bottom
    self.top_rect_end_y = gc.SCREENHEIGHT // 2
    self.top_y = self.top_rect.bottom
    self.bot_rect = pygame.Rect(0, gc.SCREENHEIGHT, gc. SCREENWIDTH, gc.SCREENHEIGHT // 2)
    self.bot_rect_start_y = self.bot_rect.top
    self.bot_rect_end_y = gc.SCREENHEIGHT // 2
    self.bot_y = self.bot_rect.top


  def update(self):
    pass

  def draw(self, window):
    pass

  def move_y_fade(self, ycoord, start_pos, end_pos, speed):
    pass

  def create_stage_image(self):
    pass

