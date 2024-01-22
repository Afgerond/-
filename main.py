import pygame, sys
from settings import *
from tiles import Tile
from level import *
from sprites import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 60 
level = Level(level_map, screen)

pygame.display.set_caption('Pixel Platformer')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("black")
    screen.blit(background, (0, 0))
    level.run()

    pygame.display.update()
    clock.tick(FPS)
    # Cool
