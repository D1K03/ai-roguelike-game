import pygame
from backend.input_handler import InputHandler
from entities.characters import Player

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.input_handle = InputHandler()
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(position=(100, 100))
        self.all_sprites.add(self.player)
        self.projectiles = []
        self.isRunning = True
    
    def process_input(self, dt):
        movement, mouseDirection, shoot = self.input_handle.update(self.player.position)
        self.player.move(movement, dt)
        if shoot:
            self.player.shoot(mouseDirection)

    def update(self, dt):
        self.all_sprites.update(dt)

    def render(self):
        self.screen.fill((100, 25, 0))
        self.all_sprites.draw(self.screen) 
    

