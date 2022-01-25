#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame as pg


from tools import *


class App:
    """
    App class
    """

    def __init__(self):
        self.screen = pg.display.set_mode(SIZE)
        self.clock = pg.time.Clock()
        self.fps = 30
        pg.display.set_caption('Pac-Man')

    def run(self):
        player, level_x, level_y = generate_level(load_level('main.txt'))
        while True:
            self.screen.fill('black')
            tiles_group.draw(self.screen)
            player_group.draw(self.screen)
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    exit()
                if e.type == pg.KEYDOWN:
                    if e.key == pg.K_LEFT or e.key == pg.K_a:
                        player.animate_left()
                    if e.key == pg.K_RIGHT or e.key == pg.K_d:
                        player.animate_right()
                    if e.key == pg.K_UP or e.key == pg.K_w:
                        player.animate_top()
                    if e.key == pg.K_DOWN or e.key == pg.K_s:
                        player.animate_bottom()

            player.update()
            pg.display.flip()
            self.clock.tick(self.fps)


if __name__ == '__main__':
    App().run()
