import pygame
from sprites import import_folder, jump_sound
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
        self.gravity = 1.2
        self.jump_speed = -18

        # Jump 
        self.max_jump_count = 3
        self.jump_count = 0
        self.jump_cooldown = False
        self.jump_cooldown_duration = 0.45
        self.last_jump_time = 0.0

        # Status
        self.status = 'idle'
        self.rechts = True

        # Health
        self.health = 100

        # Sound
        self.sound_played = True

    def imports(self):
        character_path = 'C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/character/'
        self.animations = {'idle': [], 'run':[], 'jump': [], 'fall': [], 'die': [], 'shoot': []}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def animatie(self):
        animation = self.animations[self.status]

        self.index += self.animation_speed

        if self.index >= len(animation):
            if self.status == 'shoot':
                self.index = 0
                self.get_status()
            else:
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

        if self.keys[pygame.K_SPACE] or self.keys[pygame.K_UP] or self.keys[pygame.K_w]:
            if self.sound_played == True:
                self.sound_played = False
            if self.sound_played == False:
                #jump_sound.play()
                self.sound_played = True
            self.jump()

        if self.keys[pygame.K_s]:
            self.status = 'shoot'

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
        current_time = time.time()

        if self.jump_count < self.max_jump_count:
            if self.jump_cooldown == False:
                self.direction.y = self.jump_speed
                self.jump_count += 1
                self.last_jump_time = current_time
                self.jump_cooldown = True
                # jump_sound.play()

        if self.jump_cooldown and current_time - self.last_jump_time >= self.jump_cooldown_duration:
            self.jump_cooldown = False
            self.jump_count = 0

    def shoot(self):
        pass

    def update(self):
        self.movement()
        self.get_status()
        self.animatie()
  