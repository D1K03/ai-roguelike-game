import pygame
import sys
from backend.engine import Game

class Main():
    def __init__(self):
        pygame.init()
        self.isRunning = True
        self.screenWidth, self.screenHeight = 1024,768
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Roguelike")
        self.game = Game(self.screen)

    def run(self):
        while self.isRunning:
            self.dt = self.clock.tick(60)/1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isRunning = False
            
            self.screen.fill((100, 25, 0))
            self.game.process_input(self.dt)
            self.game.update(self.dt)
            self.game.render()
            pygame.display.flip()

        pygame.quit()
        sys.exit()



if __name__ == "__main__":
    game = Main()
    game.run()


