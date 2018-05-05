import pygame as pg
import random

class Rock(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("rock.png")
        self.image = pg.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.vy = 0
        self.vx = -10
        self.rect.y = random.randint(50, pg.display.Info().current_h - 50)
        self.rect.x = pg.display.Info().current_w + 50

    def update(self):
        (width, height) = (pg.display.Info().current_w, pg.display.Info().current_h)
        self.rect.x += self.vx
        self.rect.y += self.vy
