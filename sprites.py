from os import walk
import pygame
from settings import WIDTH, HEIGHT, tile_size

pygame.init()

background = pygame.image.load("C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/assets/background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

health = pygame.image.load("C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/assets/heart.png")
health = pygame.transform.scale(health, (40, 40))
health_rect = health.get_rect(topleft = (36, 42))

coin_collect = pygame.mixer.Sound("C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/assets/coin_collect.mp3")
coin_decrease = pygame.mixer.Sound("C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/assets/coin_decrease.mp3")
jump_sound = pygame.mixer.Sound("C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/assets/jump_sound.mp3")

def import_folder(path):
    surface_list = []

    for _,__,img_files in walk(path):

        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            image_surf = pygame.transform.scale_by(image_surf, 0.075)
            surface_list.append(image_surf)

        return surface_list
    
def import_coins(path):
    surface_list = []

    for _,__,img_files in walk(path):

        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            image_surf = pygame.transform.scale(image_surf, (tile_size * 0.9, tile_size * 0.9))
            surface_list.append(image_surf)

        return surface_list
    
def import_enemies(path):
    surface_list = []

    for _,__,img_files in walk(path):

        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            #image_surf = pygame.transform.scale(image_surf, (, tile_size * 0.9))
            surface_list.append(image_surf)

        return surface_list
    
def import_wheel(path):
    surface_list = []

    for _,__,img_files in walk(path):

        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            image_surf = pygame.transform.scale(image_surf, (tile_size, tile_size))
            surface_list.append(image_surf)

        return surface_list
    