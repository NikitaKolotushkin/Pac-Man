#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame as pg

from tools import *


class Wall(pg.sprite.Sprite):
    """
    Wall class
    """

    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(walls_group, all_sprites)
        self.image = TILES_IMAGES[tile_type]
        self.rect = self.image.get_rect().move(
            TILE_WIDTH * pos_x,
            TILE_HEIGHT * pos_y
        )