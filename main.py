import pygame as pg
from pygame.locals import *
import sys
from player import *
from sprites import *

pg.init()

size = (width, height) = (pg.display.Info().current_w, pg.display.Info().current_h)
screen = pg.display.set_mode(size)
clock = pg.time.Clock()
color = (100, 100, 200)

pgroup = pg.sprite.Group()
p = Player((width/2, height/2))
pgroup.add(p)

def main():
    global screen, color
    while True:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_f:
                    screen = pg.display.set_mode(size, FULLSCREEN)
                if event.key == K_ESCAPE:
                    screen = pg.display.set_mode(size)
            if event.type == KEYUP:
                pass
        p.update()
        screen.fill(color)
        pgroup.draw(screen)
        pg.display.flip()

if __name__ == "__main__":
    main()