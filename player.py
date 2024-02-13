import pygame
from sprites import import_folder
import time


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        # Initialisatie
        super().__init__()
        self.imports()
        self.index = 0
        self.animation_speed = 0.15

        self.image = self.animations['idle'][self.index]
        self.rect = self.image.get_rect(topleft = pos)

        # Player Movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16
        self.jump_cooldown = 3
        self.jump_count = 0

        # Status
        self.status = 'idle'
        self.rechts = True

        # Health
        self.health = 100

    def imports(self):
        character_path = 'C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/character/'
        self.animations = {'idle': [], 'run':[], 'jump': [], 'fall': []}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def animatie(self):
        animation = self.animations[self.status]

        self.index += self.animation_speed

        if self.index >= len(animation):
            self.index = 0

        image = animation[int(self.index)]
        if self.rechts == True:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image, True, False)
            self.image = flipped_image

    def movement(self):
        self.keys = pygame.key.get_pressed()

        if self.keys[pygame.K_RIGHT] or self.keys[pygame.K_d]:
            self.direction.x = 1
            self.rechts = True
        elif self.keys[pygame.K_LEFT] or self.keys[pygame.K_a]:
            self.direction.x = -1
            self.rechts = False
        else:
            self.direction.x = 0

        if (self.keys[pygame.K_SPACE] or self.keys[pygame.K_UP] or self.keys[pygame.K_w]) and self.jump_count < 2:
            current_time = time.time()
            if current_time - last_jump_time > self.jump_cooldown:
                self.jump()
                self.jump_count += 1
                last_jump_time = current_time

    def get_status(self):
        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > self.gravity:
            self.status = 'fall'
        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.movement()
        self.get_status()
        self.animatie()