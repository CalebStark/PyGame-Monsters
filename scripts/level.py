import pygame
from settings import *
from tile import Tile
from player import Player

class Level:
    def __init__(self):

        # Getting the Display Surface
        self.display_surface = pygame.display.get_surface()
        # Creating Sprite Groups
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        self.create_map()
    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                if col == "w":
                    Tile(((row_index*64),(col_index*64)), [self.visible_sprites, self.obstacle_sprites])
                if col == "p":
                    Player(((row_index*64),(col_index*64)), self.visible_sprites)

    def run(self):
        # Update and Draw the game
        self.visible_sprites.draw(self.display_surface)
    