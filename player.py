import pygame as pg
import sys
from sprites import import_folder, jump_sound
from health import health_bar

class Player(pg.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.imports()
        self.index = 0
        self.animation_speed = 0.15
        self.image = self.animations['idle'][self.index]
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pg.math.Vector2(0, 0)
        self.speed = 0.1
        self.gravity = 0.42
        self.jump_speed = -12
        self.max_jump_count = 3
        self.jump_count = 0
        self.jump_cooldown = False
        self.jump_cooldown_duration = 0.45
        self.last_jump_time = 0.0
        self.status = 'idle'
        self.rechts = True
        self.health = 100
        self.sound_played = True

    def imports(self):
        character_path = 'C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/character/'
        self.animations = {'idle': [], 'run': [], 'jump': [], 'fall': [], 'die': [], 'shoot': []}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def animatie(self):
        animation = self.animations[self.status]
        self.index += self.animation_speed

        if self.index >= len(animation):
            if self.status == 'die':
                pg.quit()
                sys.exit()
            if self.status == 'shoot':
                self.index = 0
                self.get_status()
            else:
                self.index = 0

        image = animation[int(self.index)]
        if not self.rechts:
            image = pg.transform.flip(image, True, False)
        self.image = image

    def movement(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            if self.status != 'die':
                self.direction.x = 1
                self.rechts = True
        elif keys[pg.K_LEFT] or keys[pg.K_a]:
            if self.status != 'die':
                self.direction.x = -1
                self.rechts = False
        else:
            self.direction.x = 0

        if keys[pg.K_SPACE] or keys[pg.K_UP] or keys[pg.K_w]:
            if self.status != 'die':
                if self.sound_played:
                    self.sound_played = False
                if not self.sound_played:
                    # jump_sound.play()
                    self.sound_played = True
                self.jump()

        if keys[pg.K_s]:
            if self.status != 'die':
                self.status = 'shoot'

    def get_status(self):
        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > self.gravity:
            self.status = 'fall'
        else:
            if health_bar.hp <= 0:
                self.status = 'die'
            else:
                if self.direction.x != 0:
                    self.status = 'run'
                elif pg.key.get_pressed()[pg.K_s]:
                    self.status = 'shoot'
                else:
                    self.status = 'idle'

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        current_time = pg.time.get_ticks() / 1000

        if self.jump_count < self.max_jump_count:
            if not self.jump_cooldown:
                self.direction.y = self.jump_speed
                self.jump_count += 1
                self.last_jump_time = current_time
                self.jump_cooldown = True
                # jump_sound.play()

        if self.jump_cooldown and current_time - self.last_jump_time >= self.jump_cooldown_duration:
            self.jump_cooldown = False
            self.jump_count = 0

    def shoot(self):
        if pg.key.get_pressed()[pg.K_s]:
            self.status = 'shoot'
            self.animatie()

    def update(self):
        self.movement()
        self.get_status()
        self.animatie()
        self.shoot()