import pygame
from sprites import import_folder, import_coins, import_wheel
import random


class Coin(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.imports()
        self.index = 0
        self.animation_speed = 0.05

        self.image = self.animations['gold'][self.index]
        self.rect = self.image.get_rect(topleft = pos)

        self.status = 'gold'

    def imports(self):
        character_path = 'C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/coins/'
        self.animations = {'gold': []}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_coins(full_path)

    def animatie(self):
        animation = self.animations['gold']

        self.index += self.animation_speed

        if self.index >= len(animation):
            self.index = 0

        image = animation[int(self.index)]
        self.image = image

    def update(self, x_shift):
        self.animatie()
        self.rect.x += x_shift

class Diamond(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.imports()
        self.index = 0
        self.animation_speed = 0.05

        self.image = self.animations['diamond'][self.index]
        self.rect = self.image.get_rect(topleft = pos)

        self.status = 'diamond'

    def imports(self):
        character_path = 'C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/diamond/'
        self.animations = {'diamond': []}

        for animation in self.animations.keys():
            full_path = character_path
            self.animations[animation] = import_coins(full_path)

    def animatie(self):
        animation = self.animations['diamond']

        self.index += self.animation_speed

        if self.index >= len(animation):
            self.index = 0

        image = animation[int(self.index)]
        self.image = image

    def update(self, x_shift):
        self.animatie()
        self.rect.x += x_shift


class Wheel(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.imports()
        self.index = 0
        self.animation_speed = 0.15

        self.image = self.animations['random'][self.index]
        self.rect = self.image.get_rect(topleft = pos)

        self.status = 'random'

    def imports(self):
        character_path = 'C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/wheel'
        self.animations = {'random': []}

        for animation in self.animations.keys():
            full_path = character_path
            self.animations[animation] = import_wheel(full_path)

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

class Flag(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.imports()
        self.index = 0
        self.animation_speed = 0.15

        self.image = self.animations['flag'][self.index]
        self.rect = self.image.get_rect(topleft = pos)

        self.status = 'flag'

    def imports(self):
        character_path = 'C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/flag'
        self.animations = {'flag': []}

        for animation in self.animations.keys():
            full_path = character_path
            self.animations[animation] = import_wheel(full_path)

    def animatie(self):
        animation = self.animations['flag']

        self.index += self.animation_speed

        if self.index >= len(animation):
            self.index = 0

        image = animation[int(self.index)]
        self.image = image

    def update(self, x_shift):
        self.animatie()
        self.rect.x += x_shift

class Cannon(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.imports()
        self.index = 0
        self.animation_speed = 0.15

        self.image = self.animations['idle'][self.index]
        self.rect = self.image.get_rect(topleft = pos)

        self.status = 'idle'

    def imports(self):
        character_path = 'C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/cannon/idle'
        self.animations = {'idle': []}

        for animation in self.animations.keys():
            full_path = character_path
            self.animations[animation] = import_wheel(full_path)

    def animatie(self):
        animation = self.animations['idle']

        self.index += self.animation_speed

        if self.index >= len(animation):
            self.index = 0

        image = animation[int(self.index)]
        self.image = image

    def update(self, x_shift):
        self.animatie()
        self.rect.x += x_shift