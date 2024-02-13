import pygame, sys
from tiles import *
from settings import tile_size, WIDTH
from player import Player
from health import *
from coin import Coin

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0
        self.collision_cooldown = 0
        self.coins = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.coin = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size

                if cell == 'G':
                    tile = Tile('grass')
                    tile.create_tile((x, y), tile_size, 'grass')
                    self.tiles.add(tile)
                elif cell == 'D':
                    tile = Tile('dirt')
                    tile.create_tile((x, y), tile_size, 'dirt')
                    self.tiles.add(tile)
                elif cell == 'B':
                    tile = Tile('border')
                    tile.create_tile((x,y), tile_size, 'border')
                    self.tiles.add(tile)
                elif cell == 'K':
                    tile = Tile('killingborder')
                    tile.create_tile((x, y), tile_size, 'killingborder')
                    self.tiles.add(tile)
                elif cell == 'W':
                    tile = Tile('wheel')
                    tile.create_tile((x,y), tile_size, 'wheel')
                    self.tiles.add(tile)
                elif cell == 'S':
                    tile = Tile('spikes')
                    tile.create_tile((x,y), tile_size, 'spikes')
                    self.tiles.add(tile)
                elif cell == 'F':
                    tile = Tile('flag')
                    tile.create_tile((x,y), tile_size * 2, 'flag')
                    self.tiles.add(tile)
                elif cell == 'V':
                    tile = Tile('barrel')
                    tile.create_tile((x, y), tile_size, 'barrel')
                    self.tiles.add(tile)
                elif cell == '1':
                    player = Player((x, y))
                    self.player.add(player)
                elif cell == 'C':
                    coin = Coin((x, y))
                    self.coin.add(coin)

    def scroll_systeem(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < WIDTH / 4 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > WIDTH - (WIDTH / 4) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else: 
            self.world_shift = 0
            player.speed = 8

    def horizontale_movement_collisions(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if isinstance(sprite, Tile) and sprite.tile_type == 'spikes':
                    health_bar.hp -= 1
                    self.collision_cooldown = 60
                elif isinstance(sprite, Tile) and sprite.tile_type == 'flag':
                    print("Gewonnen")
                    health_bar.hp = health_bar.max_hp
                elif isinstance(sprite, Tile) and sprite.tile_type == 'killingborder':
                    pygame.quit()
                    sys.exit()
                else:
                    if player.direction.x < 0:
                        player.rect.left = sprite.rect.right
                    elif player.direction.x > 0:
                        player.rect.right = sprite.rect.left

    def verticale_movement_collisions(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if isinstance(sprite, Tile) and sprite.tile_type == 'spikes':
                    health_bar.hp -= 1
                    self.collision_cooldown = 60
                elif isinstance(sprite, Tile) and sprite.tile_type == 'flag':
                    print("Gewonnen")
                    health_bar.hp = health_bar.max_hp
                elif isinstance(sprite, Tile) and sprite.tile_type == 'killingborder':
                    pygame.quit()
                    sys.exit()
                else:
                    if player.direction.y > 0:
                        player.rect.bottom = sprite.rect.top
                        player.direction.y = 0
                    elif player.direction.y < 0:
                        player.rect.top = sprite.rect.bottom
                        player.direction.y = 0
                
    def run(self):

        # Level tiles
        self.tiles.update(self.world_shift) # Snelheid waarmee de map een bepaalde kant op beweegt!
        self.tiles.draw(self.display_surface)

        # Player
        self.player.update()

        self.scroll_systeem()
        self.horizontale_movement_collisions()
        self.verticale_movement_collisions()
        self.player.draw(self.display_surface)

        # Coin
        self.coin.draw(self.display_surface)
        self.coin.update(self.world_shift) # Snelheid waarmee de map een bepaalde kant op beweegt!

        if self.collision_cooldown > 0:
            self.collision_cooldown -= 1