import pygame
import game_config as gc
from characters import Tank, PlayerTank
from game_hud import GameHud
from random import choice, shuffle

class Game:
  def __init__(self, main, assets, player1=True, player2=False):
    self.main = main
    self.assets = assets

    self.groups = {'Player_Tanks': pygame.sprite.Group(),
                   'All_Tanks': pygame.sprite.Group(), 
                   'Bullets': pygame.sprite.Group()}
    self.player1_active = player1
    self.player2_active = player2

    self.hud = GameHud(self, self.assets)
    self.level_num = 1
    self.data = self.main_levels
    
    if self.player1_active: 
      self.player1 = PlayerTank(self, self.assets, self.groups, gc.Pl1_position, 'Up', 'Gold', 0)
    if self.player2_active: 
      self.player2 = PlayerTank(self, self.assets, self.groups, gc.Pl2_position, 'Up', 'Green', 1)

    self.enemies = 20
    self.enemy_tank_spawn_timer = gc.TANK_SPAWNING_TIME
    self.enemy_spawn_positions = [gc.Pc1_position, gc.Pc2_position, gc.Pc3_position]

    self.create_new_stage()
    self.end_game = False

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
    for dictKey in self.groups.keys():
      for item in self.groups[dictKey]:
        item.update()

  def draw(self, window):
      self.hud.draw(window)
      for dictKey in self.groups.keys():
        for item in self.groups[dictKey]:
          item.draw(window)

  def create_new_stage(self):
    for key, value in self.groups.items():
      if key == 'Player_Tanks':
        continue
      value.empty()
      

  def load_level_data(self, level):
    pass

  def generate_spawn_queue(self):
    pass

  def spawn_enemy_tanks(self):
    pass