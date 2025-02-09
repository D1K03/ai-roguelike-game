import pygame
import sys

class Main():
    def __init__(self):
        self.isRunning, self.isPlaying = True, True
        self.screenWidth, self.screenHeight = 1024,768
        self.display = pygame.Surface((self.screenWidth, self.screenHeight))
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        self.clock = pygame.time.Clock()

    def run(self):
        while self.isRunning:
            self.dt = self.clock.tick(60)/1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isRunning = False
            
            self.display.fill((100, 25, 0))
            self.screen.blit(self.display, (0, 0))
            pygame.display.flip()



if __name__ == "__main__":
    pygame.init()
    game = Main()
    game.run()
    pygame.quit()
    sys.exit()

