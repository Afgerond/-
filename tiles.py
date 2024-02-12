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
        elif tile_type == 'spikes':
            image_path = "C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/spikes/Spikes.png"
        elif tile_type == 'flag':
            image_path = "C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/flag/1.png"
        elif tile_type == 'coin':
            image_path = "C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/coins/gold/01.png"
        else:
            raise ValueError("Ongeldig tegeltype")

        tile_image = self.load_image(image_path, size)
        self.image = tile_image
        self.rect = self.image.get_rect(topleft=pos)

    def animate_coin(self):
        if self.tile_type == 'coin':
            self.coin_images = []
            for i in range(1, 4):
                image_path = f"C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/coins/gold/0{i}.png"
                self.coin_images.append(self.load_image(image_path, self.rect.width))
            self.index = 0
            self.animation_speed = 0.15
            self.last_update_time = 0

            self.index += 0.1
            if self.index >= len(self.coin_images):
                self.index = 0

            self.image = self.coin_images[int(self.index)]

    def update(self, x_shift):
        self.rect.x += x_shift
        self.animate_coin()