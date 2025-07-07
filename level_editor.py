import pygame
import game_config as gc
from levels import LevelData

class LevelEditor:
  def __init__(self, main, assets):
    self.main = main
    self.assets = assets
    self.active = True
    self.level_data = LevelData()
    self.all_levels = []

    for stage in self.level_data.level_data:
      self.all_levels.append(stage)

    self.overlay_screen = self.draw_screen()
    self.matrix = self.create_level_matrix()
   
    self.tile_type = {
      432: self.assets.brick_tiles['small'],
      482: self.assets.steel_tiles['small'],
      483: self.assets.forest_tiles['small'],
      484: self.assets.ice_tiles['small'],
      533: self.assets.water_tiles['small_1'],
      999: self.assets.flag['Phoenix_Alive']
    }

    self.inserts = [
      [-1, -1, -1, -1],
      [-1, 432, -1, 432],
      [-1, -1, 432, 432],
      [432, -1, 432, -1],
      [432, 432, -1, -1],
      [432, 432, 432, 432],
      [-1, 482, -1, 482],
      [-1, -1, 482, 482],
      [482, -1, 482, -1],
      [482, 482, -1, -1],
      [482, 482, 482, 482],
      [483, 483, 483, 483],
      [484, 484, 484, 484],
      [533, 533, 533, 533],
    ]

    self.index = 0
    self.insert_file = self.inserts[self.index]
    
    self.icon_image = self.assets.tank_images['Tank_4']['Gold']['Up'][0]
    self.icon_rect = self.icon_image.get_rect(topleft = (gc.SCREEN_BORDER_LEFT, gc.SCREEN_BORDER_TOP))

  def input(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:  
        self.main.run = False
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          self.main.run = False

  def update(self):
    pass

  def draw(self, window):
    window.blit(self.overlay_screen, (0, 0))
    self.draw_grid_to_screen(window)
    window.blit(self.icon_image, self.icon_rect)
    pygame.draw.rect(window, gc.GREEN, self.icon_rect, 1)

  def draw_screen(self):
    overlay_screen = pygame.Surface((gc.SCREENWIDTH, gc.SCREENHEIGHT))
    overlay_screen.fill(gc.GREY)
    pygame.draw.rect(overlay_screen, gc.BLACK, (gc.GAME_SCREEN))
    return overlay_screen
  
  def draw_grid_to_screen(self, window):
    vert_lines = (gc.SCREEN_BORDER_RIGHT - gc.SCREEN_BORDER_LEFT) // (gc.imageSize)
    hor_lines = (gc.SCREEN_BORDER_BOTTOM - gc.SCREEN_BORDER_TOP) // (gc.imageSize)
    for i in range(vert_lines):
      pygame.draw.line(window, gc.RED, (gc.SCREEN_BORDER_LEFT + (i * gc.imageSize), gc.SCREEN_BORDER_TOP), (gc.SCREEN_BORDER_LEFT + (i * gc.imageSize), gc.SCREEN_BORDER_BOTTOM))
    for i in range(hor_lines):
      pygame.draw.line(window, gc.RED, (gc.SCREEN_BORDER_LEFT, gc.SCREEN_BORDER_TOP + (i * gc.imageSize)), (gc.SCREEN_BORDER_RIGHT, gc.SCREEN_BORDER_TOP + (i * gc.imageSize))) 
          
  def create_level_matrix(self):
      rows = (gc.SCREEN_BORDER_BOTTOM - gc.SCREEN_BORDER_TOP) // (gc.imageSize // 2)
      columns = (gc.SCREEN_BORDER_RIGHT - gc.SCREEN_BORDER_LEFT) // (gc.imageSize // 2)
      matrix = []
      for row in range(rows):
        line = []
        for col in range(columns):
            line.append(-1)
        matrix.append(line)
      return matrix