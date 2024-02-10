import pygame
import time
from sprites import import_flag

class Tile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

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
        elif tile_type == 'flag':
            self.import_flag()  # Importeer de vlaganimatie

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

        tile_image = self.load_image(image, size)  # Gebruik het juiste image-pad
        self.image = tile_image
        self.rect = self.image.get_rect(topleft=self.rect.topleft)

    def update(self, x_shift):
        self.animatie()
        self.rect.x += x_shift