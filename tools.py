#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import pygame as pg
import sys


with open('data/levels/main.txt') as f:
    data = f.readlines()


SIZE = WIDTH, HEIGHT = (len(data[0]) * 50, len(data) * 50)

all_sprites = pg.sprite.Group()
tiles_group = pg.sprite.Group()
walls_group = pg.sprite.Group()
player_group = pg.sprite.Group()


def load_image(name, colorkey=None):
    fullname = os.path.join('data/img', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pg.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha(pg.display.set_mode(SIZE))
    return image