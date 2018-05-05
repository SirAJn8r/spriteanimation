import pygame as pg

class SpriteSheet:
    def __init__(self, img_path, maxx, maxy):
        self.ss = pg.image.load(img_path) #ss = sprite sheet
        self.width = self.ss.get_width()/maxx
        self.height = self.ss.get_height()/maxy
        self.maxx = maxx
        self.maxy = maxy
    def get_image(self, x, y):
        image = pg.Surface([self.width, self.height])
        image.blit(self.ss, (0, 0), (x*self.width, y*self.height, self.width, self.height))
        image.set_colorkey(image.get_at((0, 0)))
        return image