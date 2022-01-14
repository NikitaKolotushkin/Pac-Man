#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame as pg

from tools import *


class App:

    def __init__(self):
        self.screen = pg.display.set_mode(SIZE)
        self.clock = pg.time.Clock()
        self.fps = 60
        pg.display.set_caption('Pac-Man')

    def run(self):
        while True:
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    exit()
            
            pg.display.flip()
            self.clock.tick(self.fps)


if __name__ == '__main__':
    App().run()