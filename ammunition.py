import pygame
import gameconfig as gc

class Bullet(pygame.sprite.Sprite):
    def __init__(self, groups, owner, pos, dir, assets):
        super().__init__()
        self.assets = assets
        self.groups = groups
        self.tanks = self.groups['All_Tanks']
        self.bullet_group = self.group['Bullets']