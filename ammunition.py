import pygame
import gameconfig as gc

class Bullet(pygame.sprite.Sprite):
    def __init__(self, groups, owner, pos, dir, assets):
        super().__init__()
        self.assets = assets
        self.groups = groups
        self.tanks = self.groups['All_Tanks']
        self.bullet_group = self.groups['Bullets']
        self.xPos, self.yPos = pos
        self.direction = dir
        self.owner = owner
        self.images = self.assets.bullet_images
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect(center = (self.xPos, self.yPos))
        self.bullet_group.add(self)

    def update(self):
        self.move()

    def draw(self, window):
        window.blit(self.image, self.rect)
        pygame.draw.rect(window, gc.GREEN, self.rect, 1)

    def move(self):
        speed = gc.TANK_SPEED * 3
        if self.direction == 'Up':
            self.yPos -= speed
        elif self.direction == 'Down':
            self.yPos += speed
        elif self.direction == 'Left':
            self.xPos -= speed
        elif self.direction == 'Right':
            self.xPos += speed
        self.rect.center = (self.xPos, self.yPos)