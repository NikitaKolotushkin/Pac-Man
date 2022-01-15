#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame as pg

from tools import *


class Player(pg.sprite.Sprite):
    """
    Player class
    """

    walkLeft = [
        load_image('pac-man_left_1.png'),
        load_image('pac-man_left_2.png'),
        load_image('pac-man_full.png'),
    ]
    walkRight = [
        load_image('pac-man_right_1.png'),
        load_image('pac-man_right_2.png'),
        load_image('pac-man_full.png'),
    ]
    walkUp = [
        load_image('pac-man_top_1.png'),
        load_image('pac-man_top_2.png'),
        load_image('pac-man_full.png'),
    ]
    walkDown = [
        load_image('pac-man_bottom_1.png'),
        load_image('pac-man_bottom_2.png'),
        load_image('pac-man_full.png'),
    ]

    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)

    def update(self, x, y):
        pass