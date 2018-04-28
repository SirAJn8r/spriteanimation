import pygame as pg
from sprites import *

class Player(pg.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        bat = SpriteSheet("bat.gif", 6, 2)
        self.images = []
        for i in range(6):
            self.images.append(bat.get_image(i, 0))
        self.image = self.images[1]
        self.rect = self.image.get_rect()
        self.rect.center = pos


    def update(self):
        (width, height) = (pg.display.Info().current_w, pg.display.Info().current_h)
