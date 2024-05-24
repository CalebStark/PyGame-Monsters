import pygame
from settings import *

class Level:
    def __init__(self):

        # Getting the Display Surface
        self.display_surface = pygame.display.get_surface()
        # Creating Sprite Groups
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        self.create_map()
    def create_map(self):
        for row in WORLD_MAP:
            print(row)

    def run(self):
        # Update and Draw the game
        pass
    