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
        else:
            raise ValueError("Ongeldig tegeltype")

        tile_image = self.load_image(image_path, size)
        self.image = tile_image
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift


# --------------------------------------------------------------- + --------------------------------------------------------------- #

coin_gold_1 = pygame.image.load("C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/coins/gold/01.png").convert_alpha()
coin_gold_2 = pygame.image.load("C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/coins/gold/02.png").convert_alpha()
coin_gold_3 = pygame.image.load("C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/coins/gold/03.png").convert_alpha()
coin_gold_4 = pygame.image.load("C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/coins/gold/04.png").convert_alpha()

coin_silver_1 = pygame.image.load("C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/coins/silver/01.png").convert_alpha()
coin_silver_2 = pygame.image.load("C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/coins/silver/02.png").convert_alpha()
coin_silver_3 = pygame.image.load("C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/coins/silver/03.png").convert_alpha()
coin_silver_4 = pygame.image.load("C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/coins/silver/04.png").convert_alpha()


class Coin:
    def __init__(self, coin_images, animation_speed):
        self.coin_images = coin_images
        self.animation_speed = animation_speed
        self.index = 0
        self.last_update_time = 0

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update_time > self.animation_speed * 1000:
            self.index = (self.index + 1) % len(self.coin_images)
            self.last_update_time = current_time

    def get_current_image(self):
        return self.coin_images[self.index]
    
coin_images = [coin_gold_1, coin_gold_2, coin_gold_3, coin_gold_4]