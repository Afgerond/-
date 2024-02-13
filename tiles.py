import pygame
import random

class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type):
        super().__init__()
        self.tile_type = tile_type

    def load_image(self, image_path, size):
        image = pygame.image.load(image_path)
        image = pygame.transform.scale(image, (size, size))
        return image

    def create_tile(self, pos, size, tile_type):
        if tile_type == 'grass':
            image_path = "C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/Grass.png"
        elif tile_type == 'dirt':
            image_path = "C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/Dirt.png"
        elif tile_type == 'border':
            image_path = "C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/transparant.png"
        elif tile_type == 'killingborder':
            image_path = "C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/transparant.png"          
        elif tile_type == 'wheel':
            image_path = "C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/wheel/Ship Helm Turn 01.png"
        elif tile_type == 'spikes':
            image_path = "C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/spikes/Spikes.png"
        elif tile_type == 'flag':
            image_path = "C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/flag/1.png"   
        elif tile_type == 'coin':
            image_path = random.choice(["C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/coins/gold/01.png", "C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/coins/silver/01.png"])
        else:
            raise ValueError("Ongeldig tegeltype")

        tile_image = self.load_image(image_path, size)
        self.image = tile_image
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift