from os import walk
import pygame
from settings import WIDTH, HEIGHT

background = pygame.image.load("C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/assets/background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

health = pygame.image.load("C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/assets/heart.png")
print(health.get_height())

def import_folder(path):
    surface_list = []

    for _,__,img_files in walk(path):

        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            image_surf = pygame.transform.scale_by(image_surf, 0.1)
            surface_list.append(image_surf)

        return surface_list