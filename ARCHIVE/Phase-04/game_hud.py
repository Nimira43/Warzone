import pygame
import gameconfig as gc

class GameHud:
    def __init__(self, game, assets):
        self.game = game
        self.assets = assets
        self.images = self.assets.hud_images
        self.hud_overlay = self.generate_hud_overlay_screen()
        self.player1_active = False
        self.player1_lives = 0
        self.player1_lives_image = self.display_player_lives(self.player1_lives, self.player1_active)
        self.player2_active = False
        self.player2_lives = 0
        self.player2_lives_image = self.display_player_lives(self.player2_lives, self.player2_active)

    def generate_hud_overlay_screen(self):
        overlay_screen = pygame.Surface((gc.SCREENWIDTH, gc.SCREENHEIGHT))
        overlay_screen.fill(gc.GREY)
        pygame.draw.rect(overlay_screen, gc.BLACK, (gc.GAME_SCREEN))
        overlay_screen.blit(self.images['info_panel'], (gc.INFO_PANEL_X, gc.INFO_PANEL_Y))
        overlay_screen.set_colorkey(gc.BLACK)
        return overlay_screen
    
    def display_player_lives(self, playerlives, player_active):
        width, height = gc.imageSize, gc.imageSize // 2
        surface = pygame.Surface((width, height))
        surface.fill(gc.BLACK)
        if playerlives > 99:
            playerlives = 99
        if not player_active:
            surface.blit(self.images['grey_square'], (0, 0))
            surface.blit(self.images['grey_square'], (gc.imageSize // 2, 0))
            return surface
        if playerlives < 10:
            image = pygame.transform.rotate(self.images['life'], 180)
        else:
            num = str(playerlives)[0]
            image = self.images[f'num_{num}']
        surface.blit(image, (0, 0))
        num = str(playerlives)[-1]
        image_2 = self.images[f'num_{num}']
        surface.blit(image_2, (gc.imageSize // 2, 0))
        return surface

    def update(self):
        self.player1_active = self.game.player1_active
        if self.player1_active:
            if self.player1_lives != self.game.player1.lives:
                self.player1_lives = self.game.player1.lives
                self.player1_lives_image = self.display_player_lives(self.player1_lives, self.player1_active)
        self.player2_active = self.game.player2_active
        if self.player2_active:
            if self.player2_lives != self.game.player2.lives:
                self.player2_lives = self.game.player2.lives
                self.player2_lives_image = self.display_player_lives(self.player2_lives, self.player2_active)
    
    def draw(self, window):
        window.blit(self.hud_overlay, (0, 0))
        window.blit(self.player1_lives_image, (14.5 * gc.imageSize, 9.5 * gc.imageSize))
        window.blit(self.player2_lives_image, (14.5 * gc.imageSize, 11 * gc.imageSize))
        