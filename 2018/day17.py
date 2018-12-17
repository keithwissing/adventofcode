#!/usr/bin/env python

import sys
import adventofcode

sys.setrecursionlimit(10000)

test_data = [
    'x=495, y=2..7',
    'y=7, x=495..501',
    'x=501, y=3..7',
    'x=498, y=2..4',
    'x=506, y=1..2',
    'x=498, y=10..13',
    'x=504, y=10..13',
    'y=13, x=498..504']

test_data_2 = [
    'x=495, y=2..7',
    'y=7, x=497..501',
    'x=501, y=3..7',
    'x=498, y=2..4',
    'x=506, y=1..2',
    'x=498, y=10..13',
    'x=504, y=10..13',
    'y=13, x=498..504']

def part1(scans):
    """
    >>> part1(parse_input(test_data))
    (57, 29)
    >>> part1(parse_input(test_data_2))
    (17, 0)
    """
    minx, maxx, miny, maxy = 500, 500, 500, 0
    for (d, c1, c2, c3) in scans:
        if d == 'x':
            minx = min(minx, c1)
            maxx = max(maxx, c1)
            miny = min(miny, c2, c3)
            maxy = max(maxy, c2, c3)
        else:
            miny = min(miny, c1)
            maxy = max(maxy, c1)
            minx = min(minx, c2, c3)
            maxx = max(maxx, c2, c3)
    #print minx, miny, maxx, maxy
    grid = Grid(minx, miny, maxx, maxy)
    for (d, c1, c2, c3) in scans:
        if d == 'x':
            for y in range(c2, c3+1):
                grid.set_cell(c1, y, '#')
        else:
            for x in range(c2, c3+1):
                grid.set_cell(x, c1, '#')
    grid.drop_water(500, miny)
    #grid.display()
    return grid.count_water_reach(), grid.count_water_standing()

class Grid(object):
    def __init__(self, minx, miny, maxx, maxy):
        self.minx = minx - 1
        self.miny = miny
        self.maxx = maxx + 1
        self.maxy = maxy
        self.grid = [['.' for _ in range(self.maxx - self.minx + 1)] for _ in range(self.miny, self.maxy + 1)]

    def display(self):
        for y in range(self.miny, self.maxy+1):
            for x in range(self.minx, self.maxx+1):
                print self.get_cell(x, y),
            print

    def count_water_reach(self):
        return sum([sum([1 for v in row if v in '~|']) for row in self.grid])

    def count_water_standing(self):
        return sum([sum([1 for v in row if v in '~']) for row in self.grid])

    def get_cell(self, x, y):
        if y < self.miny or x < self.minx or y > self.maxy or x > self.maxx:
            return ' '
        return self.grid[y-self.miny][x-self.minx]

    def set_cell(self, x, y, v):
        self.grid[y-self.miny][x-self.minx] = v

    def drop_water(self, x, y):
        if self.get_cell(x, y) == '.':
            self.set_cell(x, y, '|')
            below = self.get_cell(x, y+1)
            if below in '.':
                self.drop_water(x, y+1)
                below = self.get_cell(x, y+1)
            if below in '#~':
                self.drop_water(x-1, y)
                self.drop_water(x+1, y)
                if self.is_water_to_wall(x, y, -1) and self.is_water_to_wall(x, y, +1):
                    self.change_to_standing(x, y)

    def is_water_to_wall(self, x, y, d):
        p = x
        while True:
            t = self.get_cell(p, y)
            if t not in '|':
                return t == '#'
            else:
                if self.get_cell(p, y+1) not in '#~':
                    return False
            p += d

    def change_to_standing(self, x, y):
        for d in [-1, 1]:
            p = x + d
            while self.get_cell(p, y) == '|':
                self.set_cell(p, y, '~')
                p += d
        self.set_cell(x, y, '~')

def parse_input(lines):
    result = []
    for line in lines:
        parts = line.replace('=', ' ').replace(',', ' ').replace('.', ' ').split()
        result.append((parts[0], int(parts[1]), int(parts[3]), int(parts[4])))
    return result

def main():
    puzzle_input = adventofcode.read_input(17)
    scans = parse_input(puzzle_input)
    a1, a2 = part1(scans)
    adventofcode.answer(1, 39162, a1)
    adventofcode.answer(2, 32047, a2)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
