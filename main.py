import pygame, sys
from settings import *
from tiles import Tile
from level import *
from sprites import *
from player import Player

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 60 
level = Level(level_map, screen)

pygame.display.set_caption('Pixel Platformer')

class Health:
    def __init__(self, x, y, w, h, max_hp):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = max_hp
        self.max_hp = max_hp

    def draw(self, surface):
        ratio = self.hp / self.max_hp
        pygame.draw.rect(surface, "red", (self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, "green", (self.x, self.y, self.w * ratio, self.h))

health_bar = Health(250, 200, 300, 40, 100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
    if health_bar.hp <= 0:
        pygame.quit()
        sys.exit()


    screen.fill("black")
    screen.blit(background, (0, 0))

    health_bar.hp = 30
    health_bar.draw(screen)
    level.run()

    pygame.display.update()
    clock.tick(FPS)