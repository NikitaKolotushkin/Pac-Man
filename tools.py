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

TILE_WIDTH = TILE_HEIGHT = 50


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


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '/':
                pass
            elif level[y][x] == '-':
                pass
            elif level[y][x] == '\\':
                pass
            elif level[y][x] == '|':
                pass
            elif level[y][x] == '0':
                pass


def load_level(filename):
    filename = 'data/levels/' + filename
    with open(filename) as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '#'), level_map))


TILES_IMAGES = {
    'corner_left_top': load_image('corner_left_top.png'),
    'corner_left_bottom': load_image('corner_left_bottom.png'),
    'corner_right_top': load_image('corner_right_top.png'),
    'corner_right_bottom': load_image('corner_right_bottom.png'),
    'box': load_image('box.png'),
    'door': load_image('door.png'),
    'eat': load_image('eat.png'),
    'booster': load_image('booster.png'),
    'vertical_wall_1': load_image('vertical_wall_1.png'),
    'vertical_wall_2': load_image('vertical_wall_2.png'),
    'vertical_wall_3': load_image('vertical_wall_3.png'),
    'horizontal_wall_1': load_image('horizontal_wall_1.png'),
    'horizontal_wall_2': load_image('horizontal_wall_2.png'),
    'horizontal_wall_3': load_image('horizontal_wall_3.png'),
}
