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
    body = []
    turns = {}

    def __init__(self, color, position):
        self.color = color
        self.head = Cube(position)  # new snake contains just a head
        self.body.append(self.head)
        self.direction_x = 0
        self.direction_y = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.direction_x = -1
                    self.direction_y = 0
                    # current position of head of our snake should be stored in order to move tails towards that dir
                    self.turns[self.head.positon[:]] = [self.direction_x, self.direction_y]

                elif keys[pygame.K_RIGHT]:
                    self.direction_x = 1
                    self.direction_y = 0
                    self.turns[self.head.positon[:]] = [self.direction_x, self.direction_y]

                elif keys[pygame.K_UP]:
                    self.direction_x = 0
                    self.direction_y = -1
                    self.turns[self.head.positon[:]] = [self.direction_x, self.direction_y]

                elif keys[pygame.K_DOWN]:
                    self.direction_x = 0
                    self.direction_y = 1
                    self.turns[self.head.positon[:]] = [self.direction_x, self.direction_y]

        for i, c in enumerate(self.body):
            p = c.position[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(p)

    def reset(self):
        pass

    def add_cube(self):
        pass

    def draw(self):
        pass


def draw_grid(width_, rows_, surface):
    size_in_bw_grid = width_ // rows_
    x = 0
    y = 0
    for i in range(rows):
        x = x + size_in_bw_grid
        y = y + size_in_bw_grid
        # vertical
        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, width_))
        # horizontal
        pygame.draw.line(surface, (255, 255, 255), (0, y), (width_, y))


def redraw_window(surface):
    global rows, width
    surface.fill((0, 0, 0))   # black
    draw_grid(width, rows, surface)
    pygame.display.update()


def random_snack(rows_, items):
    pass


def message_box(subject, content):
    pass


def main():
    global rows, width
    rows = 20   # should divide 500 evenly
    width = 500

    win = pygame.display.set_mode((width, width))
    snk = Snake((255, 0, 0), (10, 10))
    flag = True
    clock = pygame.time.Clock()
    while flag:
        pygame.time.delay(50)   # ms, lower it is faster the snake
        clock.tick(10)  # 10 blocks per second/fps, lower it is, slower the snake
        redraw_window(win)


main()

