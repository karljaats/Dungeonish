import pygame
import shared_vars
from camera import Camera
from player import Player
from map2 import Map


class Game:
    def __init__(self):
        self.images = {"wall": pygame.image.load("pics/wall.png").convert(),
                       "floor": pygame.image.load("pics/floor.png").convert(),
                       "player": pygame.image.load("pics/player.png").convert()}

        self.camera = Camera(shared_vars.screen_w, shared_vars.screen_h, shared_vars.tile_size)

        self.map = Map(self.images)
        player_pos = self.map.generate_map()

        self.player = Player(player_pos[0], player_pos[1], self.images)
        self.characters = {"player": self.player}

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP1:
                self.player.move(-1, 1, self.map)
            elif event.key == pygame.K_DOWN or event.key == pygame.K_KP2:
                self.player.move(0, 1, self.map)
            elif event.key == pygame.K_KP3:
                self.player.move(1, 1, self.map)
            elif event.key == pygame.K_LEFT or event.key == pygame.K_KP4:
                self.player.move(-1, 0, self.map)
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_KP6:
                self.player.move(1, 0, self.map)
            elif event.key == pygame.K_KP7:
                self.player.move(-1, -1, self.map)
            elif event.key == pygame.K_UP or event.key == pygame.K_KP8:
                self.player.move(0, -1, self.map)
            elif event.key == pygame.K_KP9:
                self.player.move(1, -1, self.map)

    def update(self):
        pass

    def draw(self, screen):
        self.camera.center(self.map.width, self.map.height, self.player.x, self.player.y)
        return self.camera.draw(screen, self.map, self.characters)
