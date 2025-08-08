import pygame
import game_config as gc
from characters import Tank, PlayerTank
from game_hud import GameHud
from random import choice, shuffle
from tile import BrickTile, SteelTile, ForestTile, IceTile, WaterTile
from fade_animate import Fade
from score_screen import ScoreScreen

class Game:
  def __init__(self, main, assets, player1=True, player2=False):
    self.main = main
    self.assets = assets

    self.groups = {'Ice_Tiles': pygame.sprite.Group(),
                   'Water_Tiles': pygame.sprite.Group(),
                   'Player_Tanks': pygame.sprite.Group(),
                   'All_Tanks': pygame.sprite.Group(), 
                   'Bullets': pygame.sprite.Group(),
                   'Destructable_Tiles': pygame.sprite.Group(),
                   'Impassable_Tiles': pygame.sprite.Group(),
                   'Forest_Tiles': pygame.sprite.Group()}
    self.top_score = 20000
    self.player1_active = player1
    self.player1_score = 0
    self.player2_active = player2
    self.player2_score = 0

    self.hud = GameHud(self, self.assets)
    self.level_num = 15
    self.level_complete = False
    self.level_transition_timer = None
    self.data = self.main_levels

    self.fade = Fade(self, self.assets, 10)
    self.scoreScreen = ScoreScreen(self, self.assets)
    
    if self.player1_active: 
      self.player1 = PlayerTank(self, self.assets, self.groups, gc.Pl1_position, 'Up', 'Gold', 0)
    if self.player2_active: 
      self.player2 = PlayerTank(self, self.assets, self.groups, gc.Pl2_position, 'Up', 'Green', 1)

    self.enemies = 20
    self.enemy_tank_spawn_timer = gc.TANK_SPAWNING_TIME
    self.enemy_spawn_positions = [gc.Pc1_position, gc.Pc2_position, gc.Pc3_position]

    self.create_new_stage()
    self.end_game = False
    self.game_on = False

  def input(self):
    keypressed = pygame.key.get_pressed()
    if self.player1_active:
      self.player1.input(keypressed)
    if self.player2_active:
      self.player2.input(keypressed)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.main.run = False
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          self.main.run = False
        if event.key == pygame.K_SPACE:
          if self.player1_active:
            self.player1.shoot()
        if event.key == pygame.K_RCTRL:
          if self.player2_active:
            self.player2.shoot()

        if event.key == pygame.K_RETURN:
          Tank(self, self.assets, self.groups, (400, 400), 'Down')
          self.enemies -= 1

  def update(self):
    self.hud.update()

    if self.fade.fade_active:
      self.fade.update()
      if not self.fade.fade_active:
        for tank in self.groups['All_Tanks']:
          tank.spawn_timer = pygame.time.get_ticks()
      return

    for dictKey in self.groups.keys():
      if dictKey == 'Player_Tanks':
        continue
      for item in self.groups[dictKey]:
        item.update()
    
    self.spawn_enemy_tanks()

    if self.enemies_killed <= 0 and self.level_complete == False:
      self.level_complete = True
      self.level_transition_timer = pygame.time.get_ticks()

    if self.level_complete:
      if pygame.time.get_ticks() - self.level_transition_timer >= gc.TRANSITION_TIMER: 
        self.stage_transition()
        
  def draw(self, window):
      self.hud.draw(window)

      if self.scoreScreen.active:
        self.scoreScreen.draw(window)
        return
      
      for dictKey in self.groups.keys():
        if dictKey == 'Impassable_Tiles': 
          continue
        if self.fade.fade_active == True and (dictKey == 'All_tanks' or dictKey == 'Player_Tank'):
          continue
        for item in self.groups[dictKey]:
          item.draw(window)
      
      if self.fade.fade_active:
        self.fade.draw(window)

  def create_new_stage(self):
    for key, value in self.groups.items():
      if key == 'Player_Tanks':
        continue
      value.empty()

    self.current_level_data = self.data.level_data[self.level_num - 1]
    self.enemies = 3
    self.enemies_killed = self.enemies
    self.load_level_data(self.current_level_data)
    self.level_complete = False
    self.fade.level = self.level_num
    self.fade.stage_image = self.fade.create_stage_image()
    self.fade.fade_active = True

    self.generate_spawn_queue()
    self.spawn_pos_index = 0
    self.spawn_queue_index = 0
    print(self.spawn_queue)

    if self.player1_active:
      self.player1.new_stage_spawn(gc.Pl1_position)
    if self.player2_active:
      self.player2.new_stage_spawn(gc.Pl2_position)

  def load_level_data(self, level):
    self.grid = []
    for i, row in enumerate(level):
      line = []
      for j, tile in enumerate(row):
        pos = (gc.SCREEN_BORDER_LEFT + (j * gc.imageSize // 2), gc.SCREEN_BORDER_TOP + (i * gc.imageSize // 2))
      if int(tile) < 0:
        line.append('   ')
      elif int(tile) == 432:
        line.append(f'{tile}')
        map_tile = BrickTile(pos, self.groups['Destructable_Tiles'], self.assets.brick_tiles)
        self.groups['Impassable_Tiles'].add(map_tile)

  def generate_spawn_queue(self):
    pass

  def spawn_enemy_tanks(self):
    pass