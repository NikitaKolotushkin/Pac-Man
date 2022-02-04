#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import pygame as pg
import random
import sys


with open('data/levels/level_1.txt') as f:
    data = f.readlines()

all_sprites = pg.sprite.Group()
tiles_group = pg.sprite.Group()
walls_group = pg.sprite.Group()
eat_group = pg.sprite.Group()
boosters_group = pg.sprite.Group()
player_group = pg.sprite.Group()
ghost_group = pg.sprite.Group()

TILE_WIDTH = TILE_HEIGHT = 45
SIZE = WIDTH, HEIGHT = ((len(data[0]) - 1) * TILE_WIDTH, len(data) * TILE_HEIGHT)


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
    return pg.transform.scale(image, (TILE_WIDTH, TILE_HEIGHT))


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '/':
                Tile('corner_left_top', x, y)
                Wall('corner_left_top', x, y)
            if level[y][x] == '[':
                Tile('corner_left_bottom', x, y)
                Wall('corner_left_bottom', x, y)
            elif level[y][x] == '-':
                Tile('horizontal_wall_1', x, y)
                Wall('horizontal_wall_1', x, y)
            elif level[y][x] == '<':
                Tile('horizontal_wall_2', x, y)
                Wall('horizontal_wall_2', x, y)
            elif level[y][x] == '>':
                Tile('horizontal_wall_3', x, y)
                Wall('horizontal_wall_3', x, y)
            elif level[y][x] == '_':
                Tile('horizontal_wall_4', x, y)
                Wall('horizontal_wall_4', x, y)
            elif level[y][x] == '+':
                Tile('horizontal_wall_5', x, y)
                Wall('horizontal_wall_5', x, y)
            elif level[y][x] == '\\':
                Tile('corner_right_top', x, y)
                Wall('corner_right_top', x, y)
            elif level[y][x] == ']':
                Tile('corner_right_bottom', x, y)
                Wall('corner_right_bottom', x, y)
            elif level[y][x] == '|':
                Tile('vertical_wall_1', x, y)
                Wall('vertical_wall_1', x, y)
            elif level[y][x] == '=':
                Tile('vertical_wall_2', x, y)
                Wall('vertical_wall_2', x, y)
            elif level[y][x] == '^':
                Tile('vertical_wall_3', x, y)
                Wall('vertical_wall_3', x, y)
            elif level[y][x] == '1':
                Tile('vertical_wall_4', x, y)
                Wall('vertical_wall_4', x, y)
            elif level[y][x] == '!':
                Tile('vertical_wall_5', x, y)
                Wall('vertical_wall_5', x, y)
            elif level[y][x] == 'L':
                Tile('vertical_wall_left', x, y)
                Wall('vertical_wall_left', x, y)
            elif level[y][x] == 'R':
                Tile('vertical_wall_right', x, y)
                Wall('vertical_wall_right', x, y)
            elif level[y][x] == '#':
                Eat('eat', x, y)
            elif level[y][x] == '0':
                Booster('booster', x, y)
            elif level[y][x] == '~':
                Tile('door', x, y)
            elif level[y][x] == '@':
                new_player = Player(x * TILE_WIDTH, y * TILE_HEIGHT)
            elif level[y][x] == 'B':
                Ghost('blinky', x * TILE_WIDTH, y * TILE_HEIGHT)
            elif level[y][x] == 'P':
                Ghost('pinky', x * TILE_WIDTH, y * TILE_HEIGHT)
            elif level[y][x] == 'I':
                Ghost('inky', x * TILE_WIDTH, y * TILE_HEIGHT)
            elif level[y][x] == 'C':
                Ghost('clyde', x * TILE_WIDTH, y * TILE_HEIGHT)
    return new_player, x, y


def load_level(filename):
    filename = 'data/levels/' + filename
    with open(filename) as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '#'), level_map))


def play_sound(filename):
    sound = pg.mixer.Sound(f'data/sounds/{filename}')
    sound.set_volume(0.5)
    sound.play()


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
    'vertical_wall_4': load_image('vertical_wall_4.png'),
    'vertical_wall_5': load_image('vertical_wall_5.png'),
    'vertical_wall_left': load_image('vertical_wall_left.png'),
    'vertical_wall_right': load_image('vertical_wall_right.png'),
    'horizontal_wall_1': load_image('horizontal_wall_1.png'),
    'horizontal_wall_2': load_image('horizontal_wall_2.png'),
    'horizontal_wall_3': load_image('horizontal_wall_3.png'),
    'horizontal_wall_4': load_image('horizontal_wall_4.png'),
    'horizontal_wall_5': load_image('horizontal_wall_5.png'),
}


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


class Tile(pg.sprite.Sprite):
    """
    Tile class
    """

    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = TILES_IMAGES[tile_type]
        self.rect = self.image.get_rect().move(
            TILE_WIDTH * pos_x,
            TILE_HEIGHT * pos_y
        )


class Player(pg.sprite.Sprite):
    """
    Player class
    """

    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)

        self.walkLeft = [
            load_image('pac-man_left_1.png'),
            load_image('pac-man_left_2.png'),
            load_image('pac-man_full.png'),
            load_image('pac-man_left_2.png'),
        ]

        self.walkRight = [
            load_image('pac-man_right_1.png'),
            load_image('pac-man_right_2.png'),
            load_image('pac-man_full.png'),
            load_image('pac-man_right_2.png'),
        ]

        self.walkUp = [
            load_image('pac-man_top_1.png'),
            load_image('pac-man_top_2.png'),
            load_image('pac-man_full.png'),
            load_image('pac-man_top_2.png'),
        ]

        self.walkDown = [
            load_image('pac-man_bottom_1.png'),
            load_image('pac-man_bottom_2.png'),
            load_image('pac-man_full.png'),
            load_image('pac-man_bottom_2.png'),
        ]

        self.score = 0
        self.current_sprite = 0
        self.image = self.walkRight[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.direction = 'right'
        self.walkDirections = {
            'left': (-TILE_WIDTH // 5, 0),
            'right': (TILE_WIDTH // 5, 0),
            'top': (0, -TILE_HEIGHT // 5),
            'bottom': (0, TILE_HEIGHT // 5),
        }
        self.animDirections = {
            'left': self.walkLeft,
            'right': self.walkRight,
            'top': self.walkUp,
            'bottom': self.walkDown,
        }

    def update(self):
        self.rect = self.rect.move(self.walkDirections[self.direction])
        if pg.sprite.spritecollideany(self, walls_group):
            self.rect = self.rect.move(
                -(self.walkDirections[self.direction][0]),
                -(self.walkDirections[self.direction][1])
            )

        if pg.sprite.spritecollideany(self, ghost_group):
            with open('results.txt', 'a') as f:
                f.write(f'{self.score} - LOSE')
                f.close()
            sys.exit()

        for eat in pg.sprite.groupcollide(eat_group, player_group, False, False):
            play_sound('eat.wav')
            eat.destroy()
            self.score += 100

        for booster in pg.sprite.groupcollide(boosters_group, player_group, False, False):
            play_sound('booster.wav')
            booster.destroy()
            self.score += 1000

        if len(eat_group) == 0 and len(boosters_group) == 0:
            with open('results.txt', 'a') as f:
                f.write(f'{self.score} - WIN')
                f.close()
            sys.exit()

        self.update_anim()

    def update_anim(self):
        self.current_sprite = (self.current_sprite + 1) % len(self.walkRight)
        self.image = self.animDirections[self.direction][self.current_sprite]

    def animate_left(self):
        self.image = self.walkLeft[self.current_sprite]
        self.direction = 'left'

    def animate_right(self):
        self.image = self.walkRight[self.current_sprite]
        self.direction = 'right'

    def animate_top(self):
        self.image = self.walkUp[self.current_sprite]
        self.direction = 'top'

    def animate_bottom(self):
        self.image = self.walkDown[self.current_sprite]
        self.direction = 'bottom'


class Ghost(pg.sprite.Sprite):
    def __init__(self, name, pos_x, pos_y):
        super().__init__(ghost_group, all_sprites)

        self.walkLeft = [
            load_image(f'{name}_left_1.png'),
            load_image(f'{name}_left_2.png'),
        ]

        self.walkRight = [
            load_image(f'{name}_right_1.png'),
            load_image(f'{name}_right_2.png'),
        ]

        self.walkUp = [
            load_image(f'{name}_top_1.png'),
            load_image(f'{name}_top_2.png'),
        ]

        self.walkDown = [
            load_image(f'{name}_bottom_1.png'),
            load_image(f'{name}_bottom_2.png'),
        ]

        self.current_sprite = 0
        self.image = self.walkRight[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)
        self.direction = 'right'
        self.walkDirections = {
            'left': (-TILE_WIDTH // 7, 0),
            'right': (TILE_WIDTH // 7, 0),
            'top': (0, -TILE_HEIGHT // 7),
            'bottom': (0, TILE_HEIGHT // 7),
        }
        self.animDirections = {
            'left': self.walkLeft,
            'right': self.walkRight,
            'top': self.walkUp,
            'bottom': self.walkDown,
        }

    def update(self):
        self.rect = self.rect.move(self.walkDirections[self.direction])
        if pg.sprite.spritecollideany(self, walls_group):
            self.rect = self.rect.move(
                -(self.walkDirections[self.direction][0]),
                -(self.walkDirections[self.direction][1])
            )
            self.direction = random.choice([*self.walkDirections])

        self.update_anim()

    def update_anim(self):
        self.current_sprite = (self.current_sprite + 1) % len(self.walkRight)
        self.image = self.animDirections[self.direction][self.current_sprite]


class Eat(pg.sprite.Sprite):
    """
    Eat class
    """

    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(eat_group, all_sprites)
        self.image = TILES_IMAGES[tile_type]
        self.rect = self.image.get_rect().move(
            TILE_WIDTH * pos_x,
            TILE_HEIGHT * pos_y
        )

    def destroy(self):
        eat_group.remove(self)
        all_sprites.remove(self)
        self.kill()


class Booster(pg.sprite.Sprite):
    """
    Booster class
    """

    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(boosters_group, all_sprites)
        self.image = TILES_IMAGES[tile_type]
        self.rect = self.image.get_rect().move(
            TILE_WIDTH * pos_x,
            TILE_HEIGHT * pos_y
        )

    def destroy(self):
        eat_group.remove(self)
        all_sprites.remove(self)
        self.kill()
