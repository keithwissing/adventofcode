#!/usr/bin/env python3
from itertools import product

import adventofcode

t1 = [
    'O....#....',
    'O.OO#....#',
    '.....##...',
    'OO.#O....O',
    '.O.....O#.',
    'O.#..O.#.#',
    '..O..#O..O',
    '.......O..',
    '#....###..',
    '#OO..#....',
]

def parse(lines):
    return [[c for c in line] for line in lines]

def tilt_north(lines):
    more = True
    while more:
        more = False
        for x, y in product(range(len(lines[0])), range(len(lines))):
            if y > 0 and lines[y][x] == 'O' and lines[y - 1][x] == '.':
                lines[y - 1][x] = 'O'
                lines[y][x] = '.'
                more = True

def get_load(lines):
    h = len(lines)
    load = 0
    for x, y in product(range(len(lines[0])), range(len(lines))):
        if lines[y][x] == 'O':
            load += h - y
    return load

def part1(lines):
    """
    >>> part1(t1)
    136
    """
    grid = parse(lines)
    tilt_north(grid)
    return get_load(grid)

def in_grid(w, h, x, y):
    return 0 <= x < w and 0 <= y < h

def tilt(lines, d):
    w, h = len(lines[0]), len(lines)
    more = True
    while more:
        more = False
        for x, y in product(range(len(lines[0])), range(len(lines))):
            x1, y1 = x + d[0], y + d[1]
            if in_grid(w, h, x1, y1) and lines[y][x] == 'O' and lines[y1][x1] == '.':
                lines[y1][x1] = 'O'
                lines[y][x] = '.'
                more = True

def cycle(lines):
    tilt(lines, (0, -1))
    tilt(lines, (-1, 0))
    tilt(lines, (0, 1))
    tilt(lines, (1, 0))

def part2(lines):
    """
    >>> part2(t1)
    64
    """
    grid = parse(lines)
    hist = {}
    c = 0
    while c < 1000000000:
        cycle(grid)
        c += 1
        load = get_load(grid)
        state = ''.join(''.join(c for c in row) for row in grid)
        if state not in hist:
            hist[state] = (c, load)
        else:
            ls = c - hist[state][0]
            c += (1000000000 - c) // ls * ls
    return load

def main():
    puzzle_input = adventofcode.read_input(14)
    adventofcode.answer(1, 108918, part1(puzzle_input))
    # adventofcode.answer(0, 64, part2(t1))
    adventofcode.answer(2, 100310, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
