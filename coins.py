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

coin_images = []

class Coin(pygame.sprite.Sprite):
    def __init__(self): 
        super().__init__()
        self.coin_images = coin_images

    def load_image(self, coin_type, size):
        for i in range(1, 5):
            image = pygame.image.load(f"C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/coins/{coin_type}/0{i}.png").convert_alpha()
            image = pygame.transform.scale(image, size)
            self.coin_images.append(image)

    def create_coin(self, pos, size, coin_type, animation_speed):
        self.coin_type = coin_type

        self.animation_speed = animation_speed
        self.index = 0
        self.last_update_time = 0

        tile_image = self.load_image(self.coin_type, size)
        self.image = self.coin_images[self.index]
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        if self.index >= len(self.coin_images):
            self.index = 0
        else:
            self.index += self.animation_speed
        self.rect.x += x_shift
            

    def get_current_image(self):
        return self.coin_images[self.index]
    