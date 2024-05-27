from settings import *
from pytmx.util_pygame import load_pygame
from os.path import join

from sprites import Sprite
from entities import Player
from groups import AllSprites

class Game:
    # Initilizing Pygame
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        pygame.display.set_caption("Monster Collector")
        self.clock = pygame.time.Clock()
        
        # Groups
        self.all_sprites = AllSprites()

        # Map Setup
        self.import_assets()
        self.setup(self.tmx_maps['world'], 'house')
        #self.setup(self.tmx_maps['hospital'], 'world')

    # Importing the TMX Maps
    def import_assets(self):
        self.tmx_maps = {
                "world": load_pygame(join("data", "maps", "world.tmx")), 
                "hospital": load_pygame(join("data", "maps", "hospital.tmx"))
                }

    #Setting up the TMX map Tiles
    def setup(self, tmx_map, player_start_pos):
        # Terrain Tiles
        for layer in ["Terrain", "Terrain Top"]:
            for x, y, surf in tmx_map.get_layer_by_name(layer).tiles():
                Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)

        # Objects
        for obj in tmx_map.get_layer_by_name("Objects"):
            Sprite((obj.x, obj.y), obj.image, self.all_sprites)

        # Entities
        for obj in tmx_map.get_layer_by_name("Entities"):
            if obj.name == "Player" and obj.properties["pos"] == player_start_pos:
                    self.player = Player((obj.x, obj.y), self.all_sprites)

    # Running the game loop
    def run(self):
        while True:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            # Game Logic
            self.all_sprites.update(dt)
            self.display_surface.fill("black")
            self.all_sprites.draw(self.player.rect.center)
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()