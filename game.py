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
        elif int(tile) == 482:
          line.append(f'{tile}')
          map_tile = SteelTile(pos, self.groups['Destructable_Tiles'], self.assets.steel_tiles)
          self.groups['Impassable_Tiles'].add(map_tile)
        elif int(tile) == 483:
          line.append(f'{tile}')
          map_tile = ForestTile(pos, self.groups['Forest_Tiles'], self.assets.forest_tiles)
        elif int(tile) == 484:
          line.append(f'{tile}')
          map_tile = IceTile(pos, self.groups['Ice_Tiles'], self.assets.ice_tiles)
        elif int(tile) == 533:
          line.append(f'{tile}')
          map_tile = WaterTile(pos, self.groups['Water_Tiles'], self.assets.water_tiles)
          self.groups['Impassable_Tiles'].add(map_tile)
        else:
          line.append(f'{tile}')
      self.grid.append(line)

  def generate_spawn_queue(self):
    self.spawn_queues_ratios = gc.Tank_spawn_queue[f'queue_{str((self.level_num - 1 % 36) // 3)}']
    self.spawn_queue = []

    for lvl, ratio in enumerate(self.spawn_queues_ratios):
      for i in range(int(round(self.enemies * (ratio / 100)))):
        self.spawn_queue.append(f'level_{lvl}')
    shuffle(self.spawn_queue) 

  def spawn_enemy_tanks(self):
    if self.enemies == 0:
      return
    if pygame.time.get_ticks() - self.enemy_tank_spawn_timer >= gc.TANK_SPAWNING_TIME:
      position = self.enemy_spawn_positions[self.spawn_pos_timer % 3]
      tank_level = gc.Tank_Critrea[self.spawn_queue[self.spawn_queue_index % len(self.spawn_queue)]]['image']
      Tank(self, self.assets, self.groups, position, 'Down', True, 'Silver', tank_level)
      self.enemy_tank_spawn_timer = pygame.time.get_ticks()
      self.spawn_pos_index += 1
      self.spawn_queue_index += 1
      self.enemies -= 1

  def stage_transition(self):
    if not self.scoreScreen.active:
      self.scoreScreen.timer = pygame.time.get_ticks()
      if self.player1_active:
        self.scoreScreen.p1_score = self.player1_score
        self.scoreScreen.p1_kill_list = sorted(self.player1.score_list)

  def change_level(self, p1_score, p2_score):
    pass