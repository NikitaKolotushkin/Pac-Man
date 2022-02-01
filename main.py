#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame as pg
import sys

from tools import *


class App:
    """
    App class
    """

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(SIZE)
        self.clock = pg.time.Clock()
        self.fps = 30
        pg.display.set_caption('Pac-Man')

    def terminate(self):
        pg.quit()
        sys.exit()

    def start_screen(self):
        intro_text = [
            'PAC-MAN',
            '',
            'LMB - Первый Уровень',
            'RMB - Второй Уровень',
        ]

        play_sound('intro.wav')

        self.screen.blit(pg.transform.scale(pg.image.load('data/img/pac-man.png'), SIZE), (0, 0))
        self.font = pg.font.SysFont('arialblack', 30)
        self.text_coords = 75

        for line in intro_text:
            rendered_string = self.font.render(line, True, pg.Color('white'))
            intro_rect = rendered_string.get_rect()
            self.text_coords += 25
            intro_rect.top = self.text_coords
            intro_rect.x = 10
            self.text_coords += intro_rect.height
            self.screen.blit(rendered_string, intro_rect)

        while True:
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    self.terminate()
                elif e.type == pg.MOUSEBUTTONDOWN:
                    if e.button == 1:
                        return generate_level(load_level('level_1.txt'))
                    if e.button == 3:
                        return generate_level(load_level('level_2.txt'))

            pg.display.flip()
            self.clock.tick(self.fps)

    def run(self):
        player, level_x, level_y = self.start_screen()

        while True:
            self.screen.fill('black')

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
            all_sprites.draw(self.screen)
            score = pg.font.SysFont('arialblack', 24).render(f'Score: {player.score}', True, (255, 255, 255))
            self.screen.blit(score, (10, 0))
            pg.display.flip()
            self.clock.tick(self.fps)


if __name__ == '__main__':
    App().run()
