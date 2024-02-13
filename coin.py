import pygame
from sprites import import_folder


class Coin(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.imports()
        self.index = 0
        self.animation_speed = 0.15

        self.image = self.animations['gold'][self.index]
        self.rect = self.image.get_rect(topleft = pos)

        self.status = 'gold'

    def imports(self):
        character_path = 'C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/coins/'
        self.animations = {'gold': [], 'silver': []}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def animatie(self):
        animation = self.animations['gold']

        self.index += self.animation_speed

        if self.index >= len(animation):
            self.index = 0

        print(self.index)

        image = animation[int(self.index)]
        self.image = image

    def update(self, x_shift):
        self.animatie()
        self.rect.x += x_shift