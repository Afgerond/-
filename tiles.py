import pygame
import time
from sprites import import_flag

class Tile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.animations = []  # Initial animations as an empty list
        self.image_path = ""  # Initial image_path as an empty string

    def load_image(self, image_path, size):
        image = pygame.image.load(image_path)
        image = pygame.transform.scale(image, (size, size))
        return image

    def create_tile(self, pos, tile_type, size):
        if tile_type == 'grass':
            self.image_path = "C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/Grass.png"
        elif tile_type == 'dirt':
            self.image_path = "C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/Dirt.png"
        elif tile_type == 'border':
            self.image_path = "C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/transparant.png"
        elif tile_type == 'flag':
            self.import_flag()  # Correctly call the import_flag method

        self.size = size  # Store the size as an attribute

        tile_image = self.load_image(self.image_path, self.size)  # Use the stored image_path and size
        self.image = tile_image
        self.rect = self.image.get_rect(topleft=pos)

    def import_flag(self):
        full_path = 'C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/flag/'
        self.animations = import_flag(full_path)

    def animatie(self):
        self.index = 0
        self.animation_speed = 0.15
        animation = self.animations

        self.index += self.animation_speed

        if self.index >= len(animation):
            self.index = 0

        image = animation[int(self.index)]

        tile_image = self.load_image(image, self.size)  # Use the stored size attribute
        self.image = tile_image
        self.rect = self.image.get_rect(topleft=self.rect.topleft)

    def update(self, x_shift):
        self.animatie()
        self.rect.x += x_shift