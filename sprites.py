from os import walk
import pygame
from settings import WIDTH, HEIGHT
from level import Level

pygame.init()

background = pygame.image.load("C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/assets/background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

health = pygame.image.load("C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/assets/heart.png")
health = pygame.transform.scale(health, (40, 40))
health_rect = health.get_rect(topleft=(36, 42))

coin = pygame.image.load("C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/coins/01.png")
coin = pygame.transform.scale(coin, (40, 40))
coin_rect = coin.get_rect(topleft=(36, 82))

level_data = [...]  # Level data
surface = pygame.display.set_mode((WIDTH, HEIGHT))
level_inst = Level(level_data, surface)
amount_coins = level_inst.coins

coin_txt = pygame.font.SysFont("arial", 40).render(f"{amount_coins}", "white", True)
coin_txt_r = coin_txt.get_rect(topleft=(90, 82))

def import_folder(path):
    surface_list = []

    for _,__,img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            image_surf = pygame.transform.scale_by(image_surf, 0.1)
            surface_list.append(image_surf)

    return surface_list