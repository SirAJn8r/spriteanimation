import pygame as pg
from pygame.locals import *
import sys
from player import *
from sprites import *
from rock import *

pg.init()

size = (width, height) = (pg.display.Info().current_w, pg.display.Info().current_h)
screen = pg.display.set_mode(size)
clock = pg.time.Clock()
color = (100, 100, 200)

pgroup = pg.sprite.Group()
p = Player((width/2, height/2))
pgroup.add(p)

bgroup = pg.sprite.Group()
boulders = []
numboulders = 5
for i in range(numboulders):
    temp = Rock()
    boulders.append(temp)
    bgroup.add(temp)

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
                if event.key == K_d:
                    p.d = True
                if event.key == K_a:
                    p.a = True
                if event.key == K_SPACE:
                    p.space = True
            if event.type == KEYUP:
                if event.key == K_d:
                    p.d = False
                if event.key == K_a:
                    p.a = False
                if event.key == K_SPACE:
                    p.space = False
        p.update()
        for i in range(len(boulders)):
            boulders[i].update()
        while True:
            temp = True
            for i in range(len(boulders)):
                if boulders[i].rect.right < 0:
                    boulders.pop(i)
                    temp = False
                    break
            if temp:
                break
        if len(boulders) < numboulders:
            for i in range(numboulders-len(boulders)):
                temp = Rock()
                boulders.append(temp)
                bgroup.add(temp)
        screen.fill(color)
        pgroup.draw(screen)
        bgroup.draw(screen)
        pg.display.flip()

if __name__ == "__main__":
    main()