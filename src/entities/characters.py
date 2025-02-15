import pygame
import os
from entities.weapons import Pistol

ASSETS_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "assets")

class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.position = pygame.Vector2(position)
        self.weapon = Pistol(owner=self)
        self.sprite_sheet = self.load_asset("chars", "char001.png")
        self.animations = {
            "down": {"walk": [], "idle": []},
            "left": {"walk": [], "idle": []},
            "right": {"walk": [], "idle": []},
            "up": {"walk": [], "idle": []},
        }
        self.load_animation_frames()

        self.current_direction = "down"
        self.current_state = "idle"
        self.frame_index = 0 
        self.frame_timer = 0.0 
        self.frame_duration = 0.2 
        self.speed = 200

        self.image = self.animations[self.current_direction][self.current_state][self.frame_index]
        self.rect = self.image.get_rect(center=position)
    

    def load_asset(self, folder, data):
        assetPath = os.path.join(ASSETS_DIR, folder, data)
        return pygame.image.load(assetPath).convert_alpha()
    
    
    def update(self, dt):
        self.update_direction_from_mouse()
        self.animate(dt)



    def load_animation_frames(self):
        directions = ["down", "left", "right", "up"]
        frame_width = 48
        frame_height = 48
        num_cols = 4
        
        for row, direction in enumerate(directions):
            for col in range(num_cols):
                x = col * frame_width
                y = row * frame_height
                frame = self.get_image(x, y, frame_width, frame_height)
                if col % 2 == 0:
                    self.animations[direction]["walk"].append(frame)
                else:
                    self.animations[direction]["idle"].append(frame)
    

    def get_image(self, x, y, width, height):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        
        return image


    def animate(self, dt):
        self.frame_timer += dt
        if self.frame_timer >= self.frame_duration:
            self.frame_timer = 0.0
            frames = self.animations[self.current_direction][self.current_state]
            self.frame_index = (self.frame_index + 1) % len(frames)
            self.image = frames[self.frame_index]
    

    def update_direction_from_mouse(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dx = mouse_x - self.position.x
        dy = mouse_y - self.position.y

        if abs(dx) > abs(dy):
            self.current_direction = "right" if dx > 0 else "left"
        else:
            self.current_direction = "down" if dy > 0 else "up"


    def move(self, direction, dt):
        dx, dy = direction

        if dx != 0 or dy != 0:
            self.current_state = "walk"
        else:
            self.current_state = "idle"
            self.frame_index = 0

        self.position.x += dx * self.speed * dt
        self.position.y += dy * self.speed * dt
        self.rect.center = self.position
