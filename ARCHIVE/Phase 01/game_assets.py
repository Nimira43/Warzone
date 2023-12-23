import pygame
import gameconfig as gc

class GameAssets:
    def __init__(self):
        self.start_screen = self.load_ind_img('start_screen', True, (gc.SCREENWIDTH, gc.SCREENHEIGHT))
        self.start_screen_token = self.load_ind_img('token', True, (gc.imageSize, gc.imageSize))        
        self.spritesheet = self.load_ind_img('BattleCity')        
        self.number_image_black_white = self.load_ind_img('numbers_black_white')        
        self.number_image_black_orange = self.load_ind_img('numbers_black_orange')        
        self.tank_images = self._load_all_tank_images()        
        # self. = self.load_ind_img('', True, gc.imageSize, gc.imageSize)        
        # self. = self.load_ind_img('', True, gc.imageSize, gc.imageSize)        
        # self. = self.load_ind_img('', True, gc.imageSize, gc.imageSize)        
        # self. = self.load_ind_img('', True, gc.imageSize, gc.imageSize)        
        # self. = self.load_ind_img('', True, gc.imageSize, gc.imageSize)        
        # self. = self.load_ind_img('', True, gc.imageSize, gc.imageSize)        
        # self. = self.load_ind_img('', True, gc.imageSize, gc.imageSize)  
        
        self.score_sheet_images = {}
        for image in ['hiScore', 'arrow', 'player1', 'player2', 'pts', 'stage', 'total']:
            self.score_sheet_images[image] = self.load_ind_img(image)

    def _load_all_tank_images(self):
        tank_image_dict = {}
        for tank in range(8):
            tank_image_dict[f'Tank_{tank}'] = {}
            for group in ['Gold', 'Silver', 'Green', 'Special']:
                tank_image_dict[f'Tank_{tank}'][group] = {}
                for direction in ['Up', 'Down', 'Left', 'Right']:
                    tank_image_dict[f'Tank_{tank}'][group][direction] = []
        
        for row in range(16):
            for col in range(16):
                surface = pygame.Surface((gc.spriteSize, gc.spriteSize))
                surface.fill(gc.BLACK)
                surface.blit(self.spritesheet, (0, 0), (col * gc.spriteSize, row * gc.spriteSize, 
                                                        gc.spriteSize, gc.spriteSize))
                surface.set_colorkey(gc.BLACK)
                surface = self.scale_image(surface, gc.imageSize)
                tank_level = self._sort_tanks_into_levels(row)
                tank_group = self._sort_tanks_into_groups(row, col)
                tank_direction = self._sort_tanks_by_direction(col)
                tank_image_dict[tank_level][tank_group][tank_direction].append(surface)
        return tank_image_dict
        
    def scale_image(self, image, scale):
        image = pygame.transform.scale(image, (scale, scale))
        return image
    
    def _sort_tanks_into_levels(self, row):
        tank_levels = {0: 'Tank_0', 1: 'Tank_1', 2: 'Tank_2', 3: 'Tank_3',
                       4: 'Tank_4', 5: 'Tank_5', 6: 'Tank_6', 7: 'Tank_7'}
        return tank_levels[row % 8]
    
    def _sort_tanks_into_groups(self, row, col):
        if 0 <= row <= 7 and 0 <= col <= 7:
            return 'Gold'
        elif 8 <= row <= 16 and 0 <= col <= 7:
            return 'Green'
        elif 0 <= row <= 7 and 8 <= col <= 16:
            return 'Silver'
        else:
            return 'Special'
        
    def _sort_tanks_by_direction(self, col):
        if col % 7 <= 1: return 'Up'
        elif col % 7 <= 3: return 'Left'
        elif col % 7 <= 5: return 'Down'
        else:
            return 'Right'
    
    def load_ind_img(self, path, scale=False, size=(0,  0)):
        image = pygame.image.load(f'assets/{path}.png').convert_alpha()
        if scale:
            image = pygame.transform.scale(image, size)
        return image