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
        self.aimleft = False
        self.d = False
        self.a = False
        self.space = False
        self.vx = 0
        self.vy = 0

    def update(self):
        (width, height) = (pg.display.Info().current_w, pg.display.Info().current_h)
        self.frame = pg.time.get_ticks() // 150 % 5
        self.image = pg.transform.scale(self.images[self.frame], (100, 100))
        self.vx = 0
        self.vy += .4
        if self.d and not self.a:
            self.aimleft = False
            self.vx = 5
        elif self.a and not self.d:
            self.aimleft = True
            self.vx = -5
        if self.space:
            self.vy = -10
        if self.vy >= 15:
            self.vy = 15
        if self.aimleft == False:
            self.image = pg.transform.flip(self.image, True, False)
        self.rect.x += self.vx
        self.rect.y += self.vy
