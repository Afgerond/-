import pygame
from sprites import import_folder, import_coins
import random


class Coin(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.imports()
        self.index = 0
        self.animation_speed = 0.05

        self.image = self.animations[self.status][self.index]
        self.rect = self.image.get_rect(topleft = pos)

        self.status = random.choice(['gold', 'silver'])

    def imports(self):
        character_path = 'C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/coins/'
        self.animations = {'gold': [], 'silver': []}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_coins(full_path)

    def animatie(self):
        animation = self.animations[self.status]

        self.index += self.animation_speed

        if self.index >= len(animation):
            self.index = 0

        image = animation[int(self.index)]
        self.image = image

    def update(self, x_shift):
        self.animatie()
        self.rect.x += x_shift

import pygame
from sprites import import_folder, import_coins


class Wheel(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.imports()
        self.index = 0
        self.animation_speed = 0.05

        self.image = self.animations[self.status][self.index]
        self.rect = self.image.get_rect(topleft = pos)

        self.status = 'random'

    def imports(self):
        character_path = 'C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/wheel/'
        self.animations = {'random': []}

        for animation in self.animations.keys():
            full_path = character_path
            self.animations[animation] = import_coins(full_path)

    def animatie(self):
        animation = self.animations['random']

        self.index += self.animation_speed

        if self.index >= len(animation):
            self.index = 0

        image = animation[int(self.index)]
        self.image = image

    def update(self, x_shift):
        self.animatie()
        self.rect.x += x_shift