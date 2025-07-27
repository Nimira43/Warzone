import pygame
from ammunition import Bullet
import game_config as gc

class Tank(pygame.sprite.Sprite):

  def __init__(self, game, assets, groups, position, direction, enemy = True, colour='Silver', tank_level=0):
    super().__init__()
    self.game = game
    self.assets = assets
    self.groups = groups

    self.tank_group = self.groups['All_Tanks']
    self.player_group = self.groups['Player_Tanks']
    self.tank_group.add(self)
    self.tank_images = self.assets.tank_images
    
    self.spawn_images = self.assets.spawn_star_images
    self.spawn_pos = position
    self.xPos, self.yPos = self.spawn_pos
    self.direction = direction

    self.spawning = True
    self.active = False
            
    self.tank_level = tank_level
    self.colour = colour
    self.tank_speed = gc.TANK_SPEED
    self.enemy = enemy
    self.tank_health = 1

    self.frame_index = 0
    self.image = self.tank_images[f'Tank_{self.tank_level}'][self.colour][self.direction][self.frame_index]
    self.rect = self.image.get_rect(topleft=(self.spawn_pos))
    self.width, self.height = self.image.get_size()

    self.bullet_limit = 1
    self.bullet_sum = 0

    self.paralyzed = False
    self.paralysis = gc.TANK_PARALYSIS
    self.paralysis_timer = pygame.time.get_ticks()

    self.spawn_image = self.spawn_images[f'star_{self.frame_index}']
    self.spawn_timer = pygame.time.get_ticks()
    self.spawn_anim_timer = pygame.time.get_ticks()

    self.mask_dict = self.get_various_masks()
    self.mask = self.mask_dict[self.direction]
    # self.mask_image = self.mask.to_surface()
    self.mask_direction = self.direction

  def input(self):
    pass

  def update(self):
    if self.spawning:
      if pygame.time.get_ticks() - self.spawn_anim_timer >= 50:
        self.spawn_animation()
      if pygame.time.get_ticks() - self.spawn_timer > 2000:
        self.frame_index = 0
        self.spawning = False
        self.active = True
      return
    if self.paralyzed:
      if pygame.time.get_ticks() - self.paralysis_timer >= self.paralysis:
        self.paralyzed = False

  def draw(self, window):
    if self.spawning:
      window.blit(self.spawn_image, self.rect)

    if self.active:
      window.blit(self.image, self.rect)
      # window.blit(self.mask_image, self.rect)
      pygame.draw.rect(window, gc.RED, self.rect, 1)

  def move_tank(self, direction):
    if self.spawning:
      return
    self.direction = direction        
    if self.paralyzed:
      self.image = self.tank_images[f'Tank_{self.tank_level}'][self.colour][self.direction][self.frame_index]
      return
    if direction == 'Up':
      self.yPos -= self.tank_speed
      if self.yPos < gc.SCREEN_BORDER_TOP:
        self.yPos = gc.SCREEN_BORDER_TOP
    elif direction == 'Down':
      self.yPos += self.tank_speed
      if self.yPos + self.height > gc.SCREEN_BORDER_BOTTOM:
        self.yPos = gc.SCREEN_BORDER_BOTTOM - self.height
    elif direction == 'Left':
      self.xPos -= self.tank_speed
      if self.xPos < gc.SCREEN_BORDER_LEFT:
        self.xPos = gc.SCREEN_BORDER_LEFT
    elif direction == 'Right':
      self.xPos += self.tank_speed
      if self.xPos + self.width > gc.SCREEN_BORDER_RIGHT:
        self.xPos = gc.SCREEN_BORDER_RIGHT - self.width
    
    self.rect.topleft = (self.xPos, self.yPos)
    self.tank_movement_animation()
    self.tank_on_tank_collisions()

  def tank_movement_animation(self):
    self.frame_index += 1
    imagelistlength = len(self.tank_images[f'Tank_{self.tank_level}'][self.colour][self.direction])
    self.frame_index = self.frame_index % imagelistlength
    self.image = self.tank_images[f'Tank_{self.tank_level}'][self.colour][self.direction][self.frame_index]
    if self.mask_direction != self.direction:
      self.mask_direction = self.direction
      self.mask = self.mask_dict[self.mask_direction]
      # self.mask_image = self.mask.to_surface()  

  def spawn_animation(self): 
    self.frame_index += 1
    self.frame_index = self.frame_index % len(self.spawn_images)
    self.spawn_image = self.spawn_images[f'star_{self.frame_index}']
    self.spawn_anim_timer = pygame.time.get_ticks()

  def get_various_masks(self):
    images = {}
    for direction in ['Up', 'Down', 'Left', 'Right']:
      image_to_mask = self.tank_images[f'Tank_{self.tank_level}'][self.colour][direction][0]
      images.setdefault(direction, pygame.mask.from_surface(image_to_mask))
    return images

  def tank_on_tank_collisions(self):
    tank_collision = pygame.sprite.spritecollide(self, self.tank_group, False)
    if len(tank_collision) == 1:
      return
    for tank in tank_collision:
      if tank == self:
        continue
      
      if self.direction == 'Right':
        if self.rect.right >= tank.rect.left and \
          self.rect.bottom > tank.rect.top and self.rect.top < tank.rect.bottom:
          self.rect.right = tank.rect.left
          self.xPos = self.rect.x
      
      elif self.direction == 'Left':
        if self.rect.left <= tank.rect.right and \
          self.rect.bottom > tank.rect.top and self.rect.top < tank.rect.bottom:
          self.rect.left = tank.rect.right
          self.xPos = self.rect.x
      
      elif self.direction == 'Up':
        if self.rect.top <= tank.rect.bottom and \
          self.rect.left < tank.rect.right and self.rect.right > tank.rect.left:
          self.rect.top = tank.rect.bottom
          self.yPos = self.rect.y
      
      elif self.direction == 'Down':
        if self.rect.bottom >= tank.rect.top and \
          self.rect.left < tank.rect.right and self.rect.right > tank.rect.left:
          self.rect.bottom = tank.rect.top
          self.yPos = self.rect.y

  def shoot(self):
    if self.bullet_sum >= self.bullet_limit:
      return
    bullet = Bullet(self.groups, self, self.rect.center, self.direction, self.assets)
    self.bullet_sum += 1

  def paralyze_tank(self, paralysis_time):
    self.paralysis = paralysis_time
    self.paralyzed = True
    self.paralysis_timer = pygame.time.get_ticks()

  def destroy_tank(self):
    self.tank_health -= 1
    if self.tank_health <= 0:
      self.kill()
      return

class PlayerTank(Tank):
  def __init__(self, game, assets, groups, position, direction, colour, tank_level):
    super().__init__(game, assets, groups, position, direction, False, colour, tank_level)
    self.player_group.add(self)
    self.lives = 3
    self.score_list = []
  
  def input(self, keypressed):
    if self.colour == 'Gold':
      if keypressed[pygame.K_q]:
        self.move_tank('Up')
      elif keypressed[pygame.K_a]:
        self.move_tank('Down')
      elif keypressed[pygame.K_z]:
        self.move_tank('Left')
      elif keypressed[pygame.K_x]:
        self.move_tank('Right')
      
    if self.colour == 'Green':
      if keypressed[pygame.K_p]:
        self.move_tank('Up')
      elif keypressed[pygame.K_l]:
        self.move_tank('Down')
      elif keypressed[pygame.K_j]:
        self.move_tank('Left')
      elif keypressed[pygame.K_k]:
        self.move_tank('Right')
  
  def new_stage_spawn(self, spawn_pos):
    self.tank_group.add(self)
    self.spwaning = True
    self.active = False
    self.direction = 'Up'
    self.xPos, self.yPos = spawn_pos
    self.image = self.tank_images[f'Tank_{self.tank_level}'][self.colour][self.direction][self.frame_index]
    self.rect.topleft = (self.xPos, self.yPos)
    self.score_list.clear()