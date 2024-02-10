import pygame
import time

class Tile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        image_path = ""

    def load_image(self, image_path, size):
        image = pygame.image.load(image_path)
        image = pygame.transform.scale(image, (size, size))
        return image

    def create_tile(self, pos, tile_type, size):
        if tile_type == 'grass':
            image_path = "C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/Grass.png"
        elif tile_type == 'dirt':
            image_path = "C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/Dirt.png"
        elif tile_type == 'border':
            image_path = "C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/transparant.png"
        elif tile_type == 'flag':
            image_path = "C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/flag/1.png"

        tile_image = self.load_image(image_path, size)
        self.image = tile_image
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift