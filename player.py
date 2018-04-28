import pygame as pg
from sprites import *

class Player(pg.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        bat = SpriteSheet("bat.gif", 6, 2)
        self.images = []
        for i in range(5):
            self.images.append(bat.get_image(i, 0))
        self.image = pg.transform.scale(self.images[1], (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.frame = 0

    def update(self):
        (width, height) = (pg.display.Info().current_w, pg.display.Info().current_h)
        self.frame = pg.time.get_ticks() // 100 % 5
        self.image = pg.transform.scale(self.images[self.frame], (100, 100))
