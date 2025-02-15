import pygame
import math

class InputHandler:
    def __init__(self):
        self.shoot = False
        self.movement = [0, 0]
        self.mouseDirection = (0, 0)

    def update(self, player_position):
        self.movement = [0, 0]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.movement[1] -= 1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.movement[1] += 1
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.movement[0] -= 1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.movement[0] += 1
        
        moveVal = math.hypot(self.movement[0], self.movement[1])
        if moveVal > 0:
            self.movement[0] /= moveVal
            self.movement[1] /= moveVal
        
        mouseX, mouseY = pygame.mouse.get_pos()
        dx = mouseX - player_position[0]
        dy = mouseY - player_position[1]
        
        length = math.hypot(dx, dy)
        if length > 0:
            self.mouseDirection = (dx / length, dy / length)
        else:
            self.mouseDirection = (0, 0)
        
        return self.movement, self.mouseDirection, self.shoot
