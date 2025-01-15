import pygame


    def draw(self):
        self.screen.fill(gc.BLACK)
        self.screen.blit(self.assets.tank_images['Tank_4']['Green']['Down'][0], (400, 400))
        pygame.display.update()

if __name__=='__main__':
    warzone = Main()
    warzone.run_game()
    pygame.quit()


