import tkinter as tk
import pygame
import random
import math
from tkinter import messagebox


class Cube(object):
    rows = 20
    width = 500

    def __init__(self, start, direction_x=1, direction_y=0, color=(255, 0, 0)):
        self.position = start
        self.direction_x = 1
        self.direction_y = 0
        self.color = color  # for snack

    def move(self, direction_x, direction_y):
        self.direction_x = direction_x
        self.direction_y = direction_y
        self.position = (self.position[0] + self.direction_x, self.position[1] + self.direction_y)

    def draw(self, surface, eyes=False):
        distance = self.width // self.rows
        i = self.position[0]
        j = self.position[1]
        pygame.draw.rect(surface, self.color, (i * distance + 1, j * distance + 1, distance - 2, distance - 2))
        if eyes:
            centre = distance // 2
            radius = 3
            circle_middle = (i * distance + centre - radius, j * distance + 8)
            circle_middle_2 = (i * distance + distance - radius * 2, j * distance + 8)
            pygame.draw.circle(surface, (0, 0, 0), circle_middle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circle_middle_2, radius)


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
                    self.turns[self.head.position[:]] = [self.direction_x, self.direction_y]

                elif keys[pygame.K_RIGHT]:
                    self.direction_x = 1
                    self.direction_y = 0
                    self.turns[self.head.position[:]] = [self.direction_x, self.direction_y]

                elif keys[pygame.K_UP]:
                    self.direction_x = 0
                    self.direction_y = -1
                    self.turns[self.head.position[:]] = [self.direction_x, self.direction_y]

                elif keys[pygame.K_DOWN]:
                    self.direction_x = 0
                    self.direction_y = 1
                    self.turns[self.head.position[:]] = [self.direction_x, self.direction_y]

        for i, c in enumerate(self.body):   # for each cube object
            p = c.position[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                if c.direction_x == -1 and c.position[0] <= 0:  # left
                    c.position = (c.rows - 1, c.position[1])
                elif c.direction_x == 1 and c.position[0] >= c.rows - 1:    # right
                    c.position = (0, c.position[1])
                elif c.direction_y == 1 and c.position[1] >= c.rows - 1:    # down
                    c.position = (c.position[0], 0)
                elif c.direction_y == -1 and c.position[1] <= 0:    # up
                    c.position = (c.position[0], c.rows - 1)
                else:   # not on edge of the screen
                    c.move(c.direction_x, c.direction_y)    # keep moving in same direction

    def reset(self):
        pass

    def add_cube(self):
        pass

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)


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
    global rows, width, snk
    surface.fill((0, 0, 0))   # black
    snk.draw(surface)
    draw_grid(width, rows, surface)
    pygame.display.update()


def random_snack(rows_, items):
    global rows
    positions = items.body
    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z: z.position == (x, y), positions))) > 0:
            continue
        else:
            break
    return


def message_box(subject, content):
    pass


def main():
    global rows, width, snk
    rows = 20   # should divide 500 evenly
    width = 500

    win = pygame.display.set_mode((width, width))
    snk = Snake((255, 0, 0), (10, 10))
    flag = True
    clock = pygame.time.Clock()
    while flag:
        pygame.time.delay(50)   # ms, lower it is faster the snake
        clock.tick(10)  # 10 blocks per second/fps, lower it is, slower the snake
        snk.move()
        redraw_window(win)


main()

