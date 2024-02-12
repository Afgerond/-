import pygame
from settings import WIDTH, HEIGHT

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

coin_gold_1 = pygame.image.load("C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/coins/gold/01.png").convert_alpha()
coin_gold_2 = pygame.image.load("C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/coins/gold/02.png").convert_alpha()
coin_gold_3 = pygame.image.load("C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/coins/gold/03.png").convert_alpha()
coin_gold_4 = pygame.image.load("C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/coins/gold/04.png").convert_alpha()

coin_silver_1 = pygame.image.load("C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/coins/silver/01.png").convert_alpha()
coin_silver_2 = pygame.image.load("C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/coins/silver/02.png").convert_alpha()
coin_silver_3 = pygame.image.load("C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/coins/silver/03.png").convert_alpha()
coin_silver_4 = pygame.image.load("C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/coins/silver/04.png").convert_alpha()


class Coin(pygame.sprite.Sprite):
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
