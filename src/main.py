import pygame
import sys

def main():
    pygame.init()
    screenResolution = pygame.display.set_mode((800, 800))
    clock = pygame.time.Clock()

    isRunning = True
    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
        

        screenResolution.fill((0, 0, 0))
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
