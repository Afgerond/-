import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type):
        super().__init__()
        self.tile_type = tile_type
        
        self.size = None
        self.image = None
        self.rect = None

    def load_image(self, image_path, size):
        image = pygame.image.load(image_path)
        image = pygame.transform.scale(image, (size, size))
        return image

    def create_tile(self, pos, size, tile_type):
        if self.tile_type == 'grass':
            image_path = "C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/Grass.png"
        elif self.tile_type == 'dirt':
            image_path = "C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/Dirt.png"
        elif self.tile_type == 'border':
            image_path = "C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/transparant.png"
        elif self.tile_type == 'killingborder':
            image_path = "C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/transparant.png"  
        elif self.tile_type == 'wheel':
            image_path = "C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/wheel/Ship Helm Turn 01.png"
        elif self.tile_type == 'spikes':
            image_path = "C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/spikes/Spikes.png"
        elif self.tile_type == 'flag':
            image_path = "C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/flag/1.png"
        elif self.tile_type == 'coin':
            image_paths = ["C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/coins/gold/01.png",
                           "C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/coins/gold/02.png",
                           "C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/coins/gold/03.png",
                           "C:/Users/josey/Privé/Programmeren/Portfolio/Platformer/Animations/graphics/map/coins/gold/04.png"]
            self.animation_frames = [pygame.image.load(image_path).convert_alpha() for image_path in image_paths]
            self.frame_index = 0
            self.animation_delay = 200  # Vertraging tussen frames in milliseconden
            self.last_frame_time = pygame.time.get_ticks()
            self.image = self.animation_frames[self.frame_index]
        else:
            raise ValueError("Ongeldig tegeltype")

        if self.tile_type != 'coin':
            self.image = pygame.image.load(image_path).convert_alpha()

        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect(topleft=self.pos)

    def update(self):
        if self.tile_type == 'coin':
            current_time = pygame.time.get_ticks()
            if current_time - self.last_frame_time > self.animation_delay:
                self.frame_index = (self.frame_index + 1) % len(self.animation_frames)
                self.image = self.animation_frames[self.frame_index]
                self.last_frame_time = current_time