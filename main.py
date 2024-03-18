import pygame, sys, os, random
from settings import *
from tiles import Tile
from level import Level
from sprites import *
from player import Player
from health import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
clock = pygame.time.Clock() 
FPS = 60
level = Level(level_map, screen)

pygame.display.set_caption('Duo Game - Pixel Platformer')

coin = pygame.image.load("C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/coins/gold/01.png")
coin = pygame.transform.scale(coin, (45, 45))
coin_rect = coin.get_rect(topleft = (33, 82))

clock_icon = pygame.image.load("C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/assets/clock.png")
clock_icon = pygame.transform.scale(clock_icon, (40, 40))
clock_rect = clock_icon.get_rect(topleft = (36, 142))

# --------------------------------------------------------------- + --------------------------------------------------------------- # 

big_cloud_image = pygame.image.load("C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/clouds/Big Clouds.png").convert_alpha()
small_cloud1_image = pygame.image.load("C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/clouds/Small Cloud 1.png").convert_alpha()
small_cloud2_image = pygame.image.load("C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/clouds/Small Cloud 2.png").convert_alpha()
small_cloud3_image = pygame.image.load("C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/clouds/Small Cloud 1.png").convert_alpha()
big_cloud_image = pygame.transform.scale_by(big_cloud_image, 1.2)
small_cloud1_image = pygame.transform.scale_by(small_cloud1_image, 2)
small_cloud2_image = pygame.transform.scale_by(small_cloud2_image, 2)
small_cloud3_image = pygame.transform.scale_by(small_cloud3_image, 2)

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

for _ in range(random.randint(4, 7)):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT // 2)
    speed = random.uniform(0.1, 0.8)
    size = random.randint(30, 80)
    image = random.choice([big_cloud_image, small_cloud1_image, small_cloud2_image, small_cloud3_image])
    cloud = Cloud(x, y, speed, size, image)
    cloud_list.append(cloud)

def game():
    run = True
    while run:
        coin_txt = pygame.font.SysFont("behnschrift", 45).render(f"{level.coins}", "white", True)
        coin_txt_r = coin_txt.get_rect(topleft = (90, coin_rect.y + 10))

        time = pygame.font.SysFont("behnschrift", 45).render(f"{round((pygame.time.get_ticks() / 1000), 1)}", "white", True)
        time_r = time.get_rect(topleft = (90, 150))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
        if health_bar.hp <= 0:
            run = False

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
    
        pygame.display.update()
        clock.tick(FPS)

game()