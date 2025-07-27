import pygame
import game_config as gc

class ScoreScreen:
  def __init__(self, game, assets):
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
    if not pygame.time.get_ticks() - self.timer >= 3000:
      return
    
    if len(self.p1_kill_list) > 0:
      if pygame.time.get_ticks() - self.timer >= 100:
        score = self.p1_kill_list.pop(0)
        self.update_score(score, 'player1')
        self.score_timer = pygame.time.get_ticks()
        return
    
    if len(self.p2_kill_list) > 0:
      if pygame.time.get_ticks() - self.timer >= 100:
        score = self.p2_kill_list.pop(0)
        self.update_score(score, 'player2')
        self.score_timer = pygame.time.get_ticks()
        return
      
    if pygame.time.get_ticks() - self.score_timer >= 3000:
      self.active = False
      self.game.change_level(self.p1_score, self.p2_score)
      self.clear_for_new_stage()

  def draw(self, window):
    window.fill(gc.BLACK)
    window.blit(self.scoresheet, (0, 0))
    window.blit(self.hi_score_nums_total, self.hi_score_nums_rect)
    window.blit(self.stage_num, self.stage_num_rect)

  def generate_scoresheet_screen(self):
    pass

  def number_image(self, score, number_colour):
    num = str(score)
    length = len(num)
    score_surface = pygame.Surface(gc.imageSize // 2 * length, gc.imageSize // 2)
    for index, number in enumerate(num):
      score_surface.blit(number_colour[int(number)], (gc.imageSize // 2 * index, 0))
    return score_surface

  def update_player_score_images(self):
    self.pl1_score = self.number_image(self.pl1_score, self.orange_nums)
    self.pl1_score_rect = self.pl_1_score.get_rect(topleft=(gc.imageSize // 2 * 11 - self.pl_1_score.get_width(), gc.imageSize // 2 * 10))
    self.pl2_score = self.number_image(self.pl2_score, self.orange_nums)
    self.pl2_score_rect = self.pl_2_score.get_rect(topleft=(gc.imageSize // 2 * 29 - self.pl_2_score.get_width(), gc.imageSize // 2 * 10))

  def _create_top_score_and_stage_number_images(self):
    self.hi_score_nums_total = self.number_image(self.top_score, self.orange_nums)
    self.hi_score_nums_rect = self.hi_score_nums_total.get_rect(topleft=(gc.imageSize // 2 * 19, gc.imageSize // 2 * 4))

    self.stage_num = self.number_image(self.stage, self.white_nums)
    self.stage_num_rect = self.stage_num.get_rect(topleft=(gc.imageSize // 2 * 19, gc.imageSize // 2 * 6))

  def update_basic_info(self, top_score, stage_number):
    self.top_score = top_score
    self.stage = stage_number
    self._create_top_score_and_stage_number_images()

  def generate_tank_kill_images(self, x1, x2, pl_dict):
    pass

  def update_score(self, score, player):
    score_dict = {100: 'line1', 200: 'line2', 300: 'line3', 400: 'line4'}

    if player == 'player1':
      self.pl1_score_values[score_dict[score]][0] += 1
      self.pl1_score_values[score_dict[score]][1] += score
      self.pl1_score_values['total'] += 1
      self.p1_score += score
      self.p1_tank_num_imgs, self.p1_tank_score_imgs = self.generate_tank_kill_images(14, 7, self.pl1_score_values)
    else:
      self.pl2_score_values[score_dict[score]][0] += 1
      self.pl2_score_values[score_dict[score]][1] += score
      self.pl2_score_values['total'] += 1
      self.p2_score += score
      self.p2_tank_num_imgs, self.p2_tank_score_imgs = self.generate_tank_kill_images(20, 25, self.pl2_score_values)
    self.update_player_score_images()

  def clear_for_new_stage(self):
    self.p1_kill_list = []
    self.p2_kill_list = []

    self.pl1_score_values = {'line1': [0, 0], 'line2': [0, 0], 'line3': [0, 0], 'line4': [0, 0], 'total': 0}
    self.pl2_score_values = {'line1': [0, 0], 'line2': [0, 0], 'line3': [0, 0], 'line4': [0, 0], 'total': 0}

    self.pl_tank_num_imgs, self.p1_tank_score_imgs = self.generate_tank_kill_images(14, 7, self. pl1_score_values)
    self.p2_tank_num_imgs, self.p2_tank_score_imgs = self.generate_tank_kill_images(20, 25, self. pl2_score_values)

  

