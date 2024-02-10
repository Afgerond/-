import pygame
import time

class Tile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def load_image(self, image_path, size):
        image = pygame.image.load(image_path)
        image = pygame.transform.scale(image, (size, size))
        return image

    def create_tile(self, pos, size, tile_type):
        if tile_type == 'grass':
            image_path = "D:/Animations/graphics/map/Grass.png"
        elif tile_type == 'dirt':
            image_path = "D:/Animations/graphics/map/Dirt.png"

        tile_image = self.load_image(image_path, size)
        self.image = tile_image
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift