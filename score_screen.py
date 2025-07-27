import pygame
import game_config as gc

class ScoreScreen:
  def __init(self, game, assets):
    self.game = game
    self.assets = assets
    self.white_nums = self.assets.number_black_white
    self.orange_nums = self.assets.number_black_orange
    self.active = False
    self.timer = pygame.time.get_ticks()
    self.score_timer = 100
    self.images = self.assets.score_sheet_images
    self.p1_score = 0
    self.p1_kill_list = []
    self.p2_score = 0
    self.p2_kill_list = []
    self.top_score = 0
    self.stage = 0
    self.scoresheet = self.generate_scoresheet_screen()
    self._create_top_score_and_stage_number_images()
    self.update_player_score_images()
    self.pl1_score_values = {'line1': [0, 0], 'line2': [0, 0], 'line3': [0, 0], 'line4': [0, 0], 'total': 0}
    self.pl2_score_values = {'line1': [0, 0], 'line2': [0, 0], 'line3': [0, 0], 'line4': [0, 0], 'total': 0}
    self.p1_tank_num_imgs, self.p1_tank_score_imgs = self.generate_tank_kill_images(14, 7, self.pl1_score_values)
    self.p2_tank_num_imgs, self.p2_tank_score_imgs = self.generate_tank_kill_images(20, 25, self.pl2_score_values)

  def update(self):
    pass

  def draw(self, window):
    pass

  def generate_scoresheet_screen(self):
    pass

  def number_image(self, score, number_colour):
    pass

  def update_player_score_images(self):
    pass

  def _create_top_score_and_stage_number_images(self):
    pass

  def update_basic_info(self, top_score, stage_number):
    pass

  def generate_tank_kill_images(self, x1, x2, pl_dict):
    pass

  def update_score(self, score, player):
    pass

  def clear_for_new_stage(self):
    pass

  

