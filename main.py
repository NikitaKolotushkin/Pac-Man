#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame as pg

from Player import Player
from tools import load_image
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
        while True:
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    exit()
                if e.type == pg.KEYDOWN:
                    if e.key == pg.K_LEFT or e.key == pg.K_a:
                        pass
                    if e.key == pg.K_RIGHT or e.key == pg.K_d:
                        pass
                    if e.key == pg.K_UP or e.key == pg.K_w:
                        pass
                    if e.key == pg.K_DOWN or e.key == pg.K_s:
                        pass
            
            pg.display.flip()
            self.clock.tick(self.fps)


if __name__ == '__main__':
    App().run()
