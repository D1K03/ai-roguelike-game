import time
import pygame
import os

ASSETS_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "assets")

class Weapon:
    def __init__(self, owner, cooldown):
        self.owner = owner
        self.lastShotTime = 0
        self.cooldown = cooldown
        self.base_weapon = self.load_asset("weapons", "Glock18.png")


    
    def shoot(self, direction):
        pass


    def load_asset(self, folder, data):
        assetPath = os.path.join(ASSETS_DIR, folder, data)
        return pygame.image.load(assetPath).convert_alpha()



class Pistol(Weapon):
    def __init__(self, owner):
        super().__init__(owner, cooldown=0.5)
        
