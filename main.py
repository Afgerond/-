import pygame as pg
import sys, os, random
from settings import *
from tiles import Tile
from level import Level
from sprites import *
from player import Player
from health import *

pg.init()

screen, clock, FPS = pg.display.set_mode((WIDTH, HEIGHT)), pg.time.Clock(), 60
level = Level(level_map, screen)

pg.display.set_caption('Duo Game - Pixel Platformer')
pg.display.set_icon(logo)

coin = pg.transform.scale(pg.image.load("C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/coins/gold/01.png"), (45, 45)), 
coin_rect = coin.get_rect(topleft=(33, 82))

clock_icon = pg.transform.scale(pg.image.load("C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/assets/clock.png"), (40, 40))
clock_rect = clock_icon.get_rect(topleft=(36, 142))

big_cloud_image, small_cloud1_image, small_cloud2_image, small_cloud3_image = pg.transform.scale_by(pg.image.load("C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/clouds/Big Clouds.png").convert_alpha(), 3), pg.transform.scale_by(pg.image.load("C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/clouds/Small Cloud 1.png").convert_alpha(), 2), pg.transform.scale_by(pg.image.load("C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/clouds/Small Cloud 2.png").convert_alpha(), 2), pg.transform.scale_by(pg.image.load("C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/clouds/Small Cloud 3.png").convert_alpha(), 2)
cloud_images = [big_cloud_image, small_cloud1_image, small_cloud2_image, small_cloud3_image]

class Cloud:
    def __init__(self, x, y, speed, image):
        self.x, self.y, self.speed = x, y, speed
        self.image = image
        self.size = image.get_size()

    def move(self):
        self.x += self.speed

        if self.x > WIDTH:
            self.x = -self.size[0]

    def draw(self, surface):
        surface.blit(self.image, (int(self.x), int(self.y)))

cloud_list = [Cloud(random.randint(0, WIDTH), random.randint(0, HEIGHT // 2), random.uniform(0.1, 0.8), random.choice(cloud_images)) for _ in range(random.randint(3, 5))]

def main():
    while True:
        pg.display.update()
        clock.tick(FPS)


def game():
    run = True
    while run:
        coin_txt = pg.font.SysFont("behnschrift", 45).render(f"{level.coins}", True, "white")
        coin_txt_r = coin_txt.get_rect(topleft=(90, coin_rect.y + 10))

        time = pg.font.SysFont("behnschrift", 45).render(f"{round((pg.time.get_ticks() / 1000), 1)}", True, "white")
        time_r = time.get_rect(topleft=(90, 150))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    pg.quit()
                    sys.exit()

        for cloud in cloud_list:
            cloud.move()

        screen.fill("black")

        screen.blit(background, (0, 0))

        for cloud in cloud_list:
            cloud.draw(screen)

        health_bar.draw(screen)
        screen.blit(health, health_rect)
        screen.blit(coin_txt, coin_txt_r)
        screen.blit(coin, coin_rect)
        screen.blit(clock_icon, clock_rect)
        screen.blit(time, time_r)

        level.run()

        pg.display.update()
        clock.tick(FPS)


game()