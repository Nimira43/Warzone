spriteSize = 16
spriteScale = 4
imageSize = spriteSize * spriteScale

SCREENWIDTH = 16 * imageSize
SCREENHEIGHT = 14 * imageSize

GAME_SCREEN = (imageSize, imageSize // 2, imageSize * 13, imageSize * 13)
INFO_PANEL_X, INFO_PANEL_Y = SCREENWIDTH - (imageSize * 2), imageSize // 2
STD_ENEMIES = 20

SCREEN_BORDER_LEFT = GAME_SCREEN[0]
SCREEN_BORDER_TOP = GAME_SCREEN[1]
SCREEN_BORDER_RIGHT = GAME_SCREEN[2] + SCREEN_BORDER_LEFT
SCREEN_BORDER_BOTTOM = GAME_SCREEN[3] + SCREEN_BORDER_TOP

FPS = 60
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREY = (99, 99, 99)
GREEN = (0, 255, 0)

TANK_SPEED = imageSize // spriteSize

SPAWN_STAR = {'star_0': [(spriteSize * 16), (spriteSize * 6), spriteSize, spriteSize],
              'star_1': [(spriteSize * 17), (spriteSize * 6), spriteSize, spriteSize],
              'star_2': [(spriteSize * 18), (spriteSize * 6), spriteSize, spriteSize],
              'star_3': [(spriteSize * 19), (spriteSize * 6), spriteSize, spriteSize]}

SHIELD = {'shield_1': [(spriteSize * 16), (spriteSize * 9), 16, 16],
          'shield_2': [(spriteSize * 16), (spriteSize * 9), 16, 16]}

POWER_UPS = {'shield':          [(16 * 16), (16 * 7), 16, 16],
            'freeze':           [(16 * 17), (16 * 7), 16, 16],
            'fortify':          [(16 * 18), (16 * 7), 16, 16],
            'power':            [(16 * 19), (16 * 7), 16, 16],
            'explosion':        [(16 * 20), (16 * 7), 16, 16],
            'extra_life':       [(16 * 21), (16 * 7), 16, 16],
            'special':          [(16 * 22), (16 * 7), 16, 16]}

SCORE = {'100': [(spriteSize * 18), (spriteSize * 10), 16, 16],
         '200': [(spriteSize * 19), (spriteSize * 10), 16, 16],
         '300': [(spriteSize * 20), (spriteSize * 10), 16, 16],
         '400': [(spriteSize * 21), (spriteSize * 10), 16, 16],
         '500': [(spriteSize * 22), (spriteSize * 10), 16, 16]}
            
FLAG = {'Phoenix_Alive':        [(16 * 19), (16 * 2), 16, 16],           
        'Phoenix_Destroyed':    [(16 * 19), (16 * 2), 16, 16]}

EXPLOSIONS = {'explode_1': [(spriteSize * 16), (spriteSize * 8), 16, 16],
              'explode_2': [(spriteSize * 17), (spriteSize * 8), 16, 16],
              'explode_3': [(spriteSize * 18), (spriteSize * 8), 16, 16],
              'explode_4': [(spriteSize * 19), (spriteSize * 8), 32, 32],
              'explode_5': [(spriteSize * 21), (spriteSize * 8), 32, 32]}
           
BULLETS = {'Up': [(spriteSize * 20), (spriteSize * 6) + 4, 8, 8],
           'Left': [(spriteSize * 20) + 8, (spriteSize * 6) + 4, 8, 8],
           'Down': [(spriteSize * 21), (spriteSize * 6) + 4, 8, 8],
           'Right': [(spriteSize * 21) + 8, (spriteSize * 6) + 4, 8, 8]}

MAP_TILES = {
    432: {'small': [spriteSize * 16, spriteSize * 4, 8, 8],
          'small_right': [(spriteSize * 16) + 12, spriteSize * 4, 4, 8],
          'small_bot': [spriteSize * 17, (spriteSize * 4) + 4, 8, 4],
          'small_left': [(spriteSize * 17) + 8, spriteSize * 4, 4, 8],
          'small_top': [(spriteSize * 18), spriteSize * 4, 8, 4]},    
    482: {'small': [(spriteSize * 16), (spriteSize * 4) + 8, 8, 8]},
    483: {'small': [(spriteSize * 16) + 8, (spriteSize * 4) + 8, 8, 8]},
    484: {'small': [(spriteSize * 17), (spriteSize * 4) + 8, 8, 8]},
    533: {'small_1': [(spriteSize * 16) + 8, (spriteSize * 5), 8, 8],
          'small_2': [(spriteSize * 17), (spriteSize * 5), 8, 8]}
}

HUD_INFO = {'stage': [(16 * 20) + 8, (16 * 11), 40, 8],
            'num_0': [(16 * 20) + 8, (16 * 11) + 8, 8, 8],
            'num_1': [(16 * 21), (16 * 11) + 8, 8, 8],
            'num_2': [(16 * 21) + 8, (16 * 11) + 8, 8, 8],
            'num_3': [(16 * 22), (16 * 11) + 8, 8, 8],
            'num_4': [(16 * 22) + 8, (16 * 11) + 8, 8, 8],
            'num_5': [(16 * 20) + 8, (16 * 12), 8, 8],
            'num_6': [(16 * 21), (16 * 12), 8, 8],
            'num_7': [(16 * 21) + 8, (16 * 12), 8, 8],
            'num_8': [(16 * 22), (16 * 12), 8, 8],
            'num_9': [(16 * 22) + 8, (16 * 12), 8, 8],
            'life': [(16 * 20), (16 * 12), 8, 8],
            'info_panel': [(16 * 23), (16 * 0), 32, (16 * 15)],
            'grey_square': [(16 * 23), (16 * 0), 8, 8]}

NUMS = {
    0: [0, 0, 8, 8], 1: [8, 0, 8, 8], 2: [16, 0, 8, 8], 3: [24, 0, 8, 8], 4: [32, 0, 8, 8],
    5: [0, 8, 8, 8], 6: [8, 8, 8, 8], 7: [16, 8, 8, 8], 3: [24, 8, 8, 8], 4: [32, 8, 8, 8]}

CONTEXT = {'pause': [(16 * 18), (16 * 11), 40, 8],
           'game_over': [(16 * 18), (16 * 11) + 8, 32, 16]}


            