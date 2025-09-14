import pygame
import game_config as gc

class StartScreen:
  def __init__(self, main, assets):
    self.main = main
    self.assets = assets
    self.start_y = gc.SCREENHEIGHT
    self.end_y = 0
    self.image = self.assets.start_screen
    self.rect = self.image.get_rect(topleft=(0, self.start_y))
    self.x, self.y = self.rect.topleft
    self.speed = gc.SCREEN_SCROLL_SPEED

    self.options_positions = [
      (4 * gc.imageSize, 7.75 * gc.imageSize),
      (4 * gc.imageSize, 8.75 * gc.imageSize),
      (4 * gc.imageSize, 9.75 * gc.imageSize),
    ]

    self.token_index = 0
    self.token_image = self.assets.start_screen_token
    self.token_rect = self.token_image.get_rect(topleft=self.option_positions[self.token_index])
    self.start_screen_active = False

  def input(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.main.run = False
        return False
      
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          self.main.run = False
          return False
        
        if self.start_screen_active == False:
          self._complete_screen_position()
          return True
        
        if event.key == pygame.K_UP or event.key == pygame.K_w:
          self._switch_options_main_menu(-1)
        
        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
          self._switch_options_main_menu(+1)
        
        if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
          self._selected_option_action()
          return False
        
    return True
  
  def update(self):
    if self._animate_screen_into_position() == False:
      return
    self.start_screen_active = True

  def draw(self, window):
    window.blit(self.image, self.rect)
    if self.start_screen_active:
      window.blit(self.token_image, self.token_rect)

  def _switch_options_main_menu(self, num):
    self.token_index += num
    self.token_index = self.token_index % len(self.option_positions)
    self.token_rect.topleft = self.option_positions[self.token_index]

  def _selected_option_action(self):
    if self.token_index == 0:
      self.main.start_new_game(player1=True, player2=False)
    elif self.token_index == 1:
      self.main.start_new_game(player1=True, player2=True)
    elif self.token_index == 2:
      self.main.start_level_creator()

  def _animate_screen_into_position(self):
    if self.y == self.end_y: 
      return True

    self.y -= self.speed
    if self.y < self.end_y:
      self.y = self.end_y
    self.rect.topleft = (0, self.y)
    return False

  def _complete_screen_position(self):
    self.y = self.end_y
    self.rect.topleft = (0, self.y)