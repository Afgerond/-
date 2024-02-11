import pygame, sys, os, random
from settings import *
from tiles import Tile
from level import *
from sprites import *
from player import Player
from health import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 60
level = Level(level_map, screen)

pygame.display.set_caption('Pixel Platformer - Duo Game')

class Cloud:
    def __init__(self, x, y, speed, size, image):
        self.x = x
        self.y = y
        self.speed = speed
        self.size = size
        self.image = image

    def move(self):
        self.x += self.speed

        if self.x > WIDTH:
            self.x = -self.size

    def draw(self, surface):
        surface.blit(self.image, (int(self.x), int(self.y)))

cloud_list = []

for _ in range(8):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT // 2)
    speed = random.uniform(0.1, 0.5)
    size = random.randint(30, 80)
    image = random.choice([big_cloud_image, small_cloud1_image, small_cloud2_image, small_cloud3_image])
    cloud = Cloud(x, y, speed, size, image)
    cloud_list.append(cloud)

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

    for cloud in cloud_list:
        cloud.move()

    screen.fill("black")
    screen.blit(background, (0, 0))

    for cloud in cloud_list:
        cloud.draw(screen)

    health_bar.draw(screen)
    level.run()

    pygame.display.update()
    clock.tick(FPS)