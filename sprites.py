from os import walk
import pygame
from settings import WIDTH, HEIGHT

pygame.init()

background = pygame.image.load("C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/assets/background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# CLOUDS
big_cloud_image = pygame.image.load("C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/clouds/Big Clouds.png").convert_alpha()
small_cloud1_image = pygame.image.load("C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/clouds/Small Cloud 1.png").convert_alpha()
small_cloud2_image = pygame.image.load("C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/clouds/Small Cloud 2.png").convert_alpha()
small_cloud3_image = pygame.image.load("C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/clouds/Small Cloud 1.png").convert_alpha()
big_cloud_image = pygame.transform.scale_by(big_cloud_image, 2)
small_cloud1_image = pygame.transform.scale_by(small_cloud1_image, 2)
small_cloud2_image = pygame.transform.scale_by(small_cloud2_image, 2)
small_cloud3_image = pygame.transform.scale_by(small_cloud3_image, 2)

def import_folder(path):
    surface_list = []

    for _,__,img_files in walk(path):

        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            image_surf = pygame.transform.scale_by(image_surf, 0.1)
            surface_list.append(image_surf)

        return surface_list