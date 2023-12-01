#!/usr/bin/env python3
from collections import defaultdict

import adventofcode

t1 = [
    '498,4 -> 498,6 -> 496,6',
    '503,4 -> 502,4 -> 502,9 -> 494,9',
]

def sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0

def add(a, b):
    return tuple(x + y for x, y in zip(a, b))

def print_grid(grid):
    minx = min(x for x, y in grid.keys())
    maxx = max(x for x, y in grid.keys())
    miny = min(y for x, y in grid.keys())
    maxy = max(y for x, y in grid.keys())

    print('-')
    for y in range(miny, maxy + 1):
        print(''.join(grid[(x, y)] for x in range(minx, maxx + 1)))

def parse(lines):
    grid = defaultdict(lambda: '.')
    for line in lines:
        cs = [(int(x), int(y)) for i in line.split(' -> ') for x, y in [i.split(',')]]
        for src, dst in zip(cs[:-1], cs[1:]):
            delta = tuple(sign(b - a) for a, b in zip(src, dst))
            pos = src
            grid[pos] = '#'
            while pos != dst:
                pos = add(pos, delta)
                grid[pos] = '#'
    return grid

def add_sand(grid):
    pos = (500, 0)
    maxy = max(y for x, y in grid.keys())
    flow = True
    while flow and pos[1] < maxy:
        flow = False
        for delta in [(0, 1), (-1, 1), (1, 1)]:
            t = add(pos, delta)
            if grid[t] == '.':
                pos = t
                flow = True
                break
    if not flow:
        grid[pos] = 'o'
    return flow

def part1(lines):
    """
    >>> part1(t1)
    24
    """
    grid = parse(lines)

    while not add_sand(grid):
        pass

    return sum(1 for v in grid.values() if v == 'o')

def add_sand_2(grid, floor):
    pos = (500, 0)
    flow = True
    while flow:
        flow = False
        for delta in [(0, 1), (-1, 1), (1, 1)]:
            t = add(pos, delta)
            if t[1] < floor and grid[t] == '.':
                pos = t
                flow = True
                break
    if not flow:
        grid[pos] = 'o'
    return flow

def part2(lines):
    """
    >>> part2(t1)
    93
    """
    grid = parse(lines)

    floor = max(y for x, y in grid.keys()) + 2
    while grid[(500, 0)] != 'o':
        add_sand_2(grid, floor)

    return sum(1 for v in grid.values() if v == 'o')

def main():
    puzzle_input = adventofcode.read_input(14)
    adventofcode.answer(1, 795, part1(puzzle_input))
    adventofcode.answer(2, 30214, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
