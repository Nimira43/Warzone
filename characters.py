import pygame
from ammunition import Bullet
from explosions import Explosion
from powerups import PowerUps
import random
import game_config as gc

class MyRect(pygame.sprite.Sprite):
  def __init__(self, x, y, width, height):
    super().__init__()
    self.image = None
    self.rect = pygame.Rect(x, y, width, height)

class Tank(pygame.sprite.Sprite):
  def __init__(self, game, assets, groups, position, direction, enemy = True, colour='Silver', tank_level=0):
    super().__init__()
    self.game = game
    self.assets = assets
    self.groups = groups

    self.tank_group = self.groups['All_Tanks']
    self.player_group = self.groups['Player_Tanks']
    self.tank_group.add(self)

    levels = {0: None, 4: 'level_0', 5: 'level_1', 6: 'level_2', 7: 'level_3'}
    self.level = levels[tank_level]

    self.tank_images = self.assets.tank_images
    self.spawn_images = self.assets.spawn_star_images
    self.spawn_pos = position
    self.xPos, self.yPos = self.spawn_pos
    self.direction = direction

    self.spawning = True
    self.active = False
            
    self.tank_level = tank_level
    self.colour = colour
    self.tank_speed = gc.TANK_SPEED if not self.level else gc.TANK_SPEED * gc.Tank_Critrea[self.level]['speed']
    self.power = 1 if not self.level else gc.Tank_Critrea[self.level]['power']
    self.bullet_speed_modifier = 1
    self.bullet_speed = gc.TANK_SPEED * (3 * self.bullet_speed_modifier)
    self.score = 100 if not self.level else gc.Tank_Critrea[self.level]['score']
    self.enemy = enemy
    self.tank_health = 1 if not self.level else gc.Tank_Critrea[self.level]['health']

    self.frame_index = 0
    self.image = self.tank_images[f'Tank_{self.tank_level}'][self.colour][self.direction][self.frame_index]
    self.rect = self.image.get_rect(topleft=(self.spawn_pos))
    self.width, self.height = self.image.get_size()

    self.bullet_limit = 1
    self.bullet_sum = 0
    self.shot_cooldown_time = 500
    self.shot_cooldown = pygame.time.get_ticks()

    self.paralyzed = False
    self.paralysis = gc.TANK_PARALYSIS
    self.paralysis_timer = pygame.time.get_ticks()

    self.amphibious = False

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
        colliding_sprites = pygame.sprite.spritecollide(self, self.tank_group, False)
        if len(colliding_sprites) == 1:
          self.frame_index = 0
          self.spawning = False
          self.active = True
        else:
          self.spawn_star_collection(colliding_sprites)
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

  def grid_alignment_movement(self, pos):
    if pos % (gc.imageSize // 2) != 0:
      if pos % (gc.imageSize // 2) < gc.imageSize // 4:
        pos -= (pos % (gc.imageSize // 4))
      elif pos % (gc.imageSize // 2) > gc.imageSize // 4:
        pos += (gc.imageSize // 4) - (pos % (gc.imageSize // 4))
      else:
        return pos
    return pos
  
  def move_tank(self, direction):
    if self.spawning:
      return
    self.direction = direction        
    if self.paralyzed:
      self.image = self.tank_images[f'Tank_{self.tank_level}'][self.colour][self.direction][self.frame_index]
      return
    if direction == 'Up':
      self.yPos -= self.tank_speed
      self.xPos = self.grid_alignment_movement(self.xPos)
      if self.yPos < gc.SCREEN_BORDER_TOP:
        self.yPos = gc.SCREEN_BORDER_TOP
    elif direction == 'Down':
      self.yPos += self.tank_speed
      self.xPos = self.grid_alignment_movement(self.xPos)
      if self.yPos + self.height > gc.SCREEN_BORDER_BOTTOM:
        self.yPos = gc.SCREEN_BORDER_BOTTOM - self.height
    elif direction == 'Left':
      self.xPos -= self.tank_speed
      self.yPos = self.grid_alignment_movement(self.yPos)
      if self.xPos < gc.SCREEN_BORDER_LEFT:
        self.xPos = gc.SCREEN_BORDER_LEFT
    elif direction == 'Right':
      self.xPos += self.tank_speed
      self.yPos = self.grid_alignment_movement(self.yPos)
      if self.xPos + self.width > gc.SCREEN_BORDER_RIGHT:
        self.xPos = gc.SCREEN_BORDER_RIGHT - self.width
    
    self.rect.topleft = (self.xPos, self.yPos)
    self.tank_movement_animation()
    self.tank_on_tank_collisions()
    self.tank_collisions_with_obstacles()
    self.base_collision()

  def tank_movement_animation(self):
    self.frame_index += 1
    imagelistlength = len(self.tank_images[f'Tank_{self.tank_level}'][self.colour][self.direction])
    self.frame_index = self.frame_index % imagelistlength
    self.image = self.tank_images[f'Tank_{self.tank_level}'][self.colour][self.direction][self.frame_index]
    if self.mask_direction != self.direction:
      self.mask_direction = self.direction
      self.mask = self.mask_dict[self.mask_direction]  

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
      if tank == self or tank.spawning == True:
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

  def tank_collisions_with_obstacles (self):
    wall_collision = pygame.sprite.spritecollide(self, self.groups['Impassable_Tiles'], False)
    for obstacle in wall_collision:
      if obstacle in self.groups['Water_Tiles'] and self.amphibious == True:
        continue
      if self.direction == 'Right':
        if self.rect.right >= obstacle.rect.left:
          self.rect.right = obstacle.rect.left
          self.xPos = self.rect.x
      
      elif self.direction == 'Left':
        if self.rect.left <= obstacle.rect.right:
          self.rect.left = obstacle.rect.right
          self.xPos = self.rect.x
           
      elif self.direction == 'Up':
        if self.rect.top <= obstacle.rect.bottom:
          self.rect.top = obstacle.rect.bottom
          self.yPos = self.rect.y
      
      elif self.direction == 'Down':
        if self.rect.bottom >= obstacle.rect.top:
          self.rect.bottom = obstacle.rect.top
          self.yPos = self.rect.y

  def spawn_star_collision(self, colliding_sprites):
    for tank in colliding_sprites:
      if tank.active:
        return
    for tank in colliding_sprites:
      if tank == self:
        continue  
      if self.spawning and tank.spawning:
        self.frame_index = 0
        self.spawning = False
        self.active = True    

  def base_collision(self):
    if not self.groups['Eagle'].sprite.active:
      return
    if self.rect.colliderect(self.groups['Eagle'].sprite.rect):
      self.groups['Eagle'].sprite.destroy_base()
      
  def shoot(self):
    if self.bullet_sum >= self.bullet_limit:
      return
    bullet = Bullet(self.groups, self, self.rect.center, self.direction, self.assets)
    self.assets.channel_fire_sound.play(self.assets.fire_sound)
    self.bullet_sum += 1

  def paralyze_tank(self, paralysis_time):
    self.paralysis = paralysis_time
    self.paralyzed = True
    self.paralysis_timer = pygame.time.get_ticks()

  def destroy_tank(self):
    self.tank_health -= 1
    if self.tank_health <= 0:
      self.kill()
      Explosion(self.assets, self.groups, self.rect.center, 5, self.score)
      self.assets.channel_explosion_sound.play(self.assets.explosion_sound)
      self.game.enemies_killed -= 1
      return
    
    if self.tank_health == 3:
      self.colour = 'Green'
    elif self.tank_health == 2:
      self.colour = 'Gold'
    elif self.tank_health == 1:
      self.colour = 'Silver'


class PlayerTank(Tank):
  def __init__(self, game, assets, groups, position, direction, colour, tank_level):
    super().__init__(game, assets, groups, position, direction, False, colour, tank_level)
    self.player_group.add(self)
    self.lives = 1
    self.dead = False
    self.game_over = False
    self.score_list = []
    self.shield_start = True
    self.shield = False
    self.shield_time_limit = 5000
    self.shield_timer = pygame.time.get_ticks()
    self.shield_images = self.assets.shield_images
    self.shield_img_index = 0
    self.shield_anim_timer = pygame.time.get_ticks()
    self.shield_image = self.shield_images[f'shield_{self.shield_img_index + 1}']
    self.shield_image_rect = self.shield_image.get_rect(topleft=(self.rect.topleft))

    self.movement_sound = self.assets.movement_sound
    self.player_movement_channel = pygame.mixer.Channel(0)


  def input(self, keypressed):
    if self.game_over or self.dead:
      return
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
  
  def draw():
    pass

  def move_tank():
    pass

  def shoot():
    pass

  def destroy_tank(self):
    pass

  def new_stage_spawn(self, spawn_pos):
    self.tank_group.add(self)
    self.spwaning = True
    self.active = False
    self.direction = 'Up'
    self.xPos, self.yPos = spawn_pos
    self.image = self.tank_images[f'Tank_{self.tank_level}'][self.colour][self.direction][self.frame_index]
    self.rect.topleft = (self.xPos, self.yPos)
    self.score_list.clear()

  def respawn_tank():
    pass

class EnemyTank(Tank):
  def __init__():
    pass

  def ai_shooting():
    pass

  def ai_move():
    pass

  def ai_move_direction():
    pass

  def update():
    pass

  def draw():
    pass