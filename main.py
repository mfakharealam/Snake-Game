import tkinter as tk
import pygame
import random
import math
from tkinter import messagebox


class Cube(object):
    rows = 0
    width = 0

    def __init__(self, start, direction_x=1, direction_y=0, color=(255, 0, 0)):
        pass

    def move(self, direction_x, direction_y):
        pass

    def draw(self, surface, eyes=False):
        pass


class Snake(object):
    def __init__(self, color, position):
        pass

    def move(self):
        pass

    def reset(self):
        pass

    def add_cube(self):
        pass

    def draw(self):
        pass


def draw_grid(width_, rows_, surface):
    pass


def redraw_window(surface):
    pass


def random_snack(rows_, items):
    pass


def message_box(subject, content):
    pass


def main():
    rows = 20   # should divide 500 evenly
    width = 500
    height = 500

    win = pygame.display.set_mode(width, height)
    snk = Snake((255, 0, 0), (10, 10))
    flag = True
    clock = pygame.time.Clock()
    while flag:
        pygame.time.delay(50)
        clock.tick(10)


main()

