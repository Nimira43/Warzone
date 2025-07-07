import pygame
import os
import csv

class LevelData:
  def __init__(self):
    self.leveldata = self.load_level_data()

  def load_level_data(self):
    gameStages = []
    for stage in os.listdir('levels'):
      level_data = [[] for i in range(27)]
      with open(f'levels/{stage}', newline='') as csvFile:
        reader = csv.reader(csvFile, delimiter=',')
        for i, row in enumerate(reader):
          for j, tile in enumerate(row):
            level_data[i].append(int(tile))
      gameStages.append(level_data)
    return

  def save_level_data(self, level_data):
    pass

