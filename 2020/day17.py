#!/usr/bin/env python3

from collections import defaultdict
import itertools
import adventofcode

t1 = [
    '.#.',
    '..#',
    '###',
]

def parse(lines):
    grid = defaultdict(lambda: 0)
    for y, line in enumerate(lines):
        for x, val in enumerate(line):
            if val == '#':
                grid[(x, y, 0)] = 1
    return grid

def adjacent(pos):
    for d in itertools.product([-1, 0, 1], repeat=3):
        if d == (0, 0, 0):
            continue
        yield (pos[0] + d[0], pos[1] + d[1], pos[2] + d[2])

def iterate(grid):
    ng = defaultdict(lambda: 0)
    for pos in itertools.product(range(-10, 20), repeat=3):
        nc = sum(grid[tp] for tp in adjacent(pos))
        if grid[pos] == 1:
            ng[pos] = 1 if nc in [2, 3] else 0
        if grid[pos] == 0:
            ng[pos] = 1 if nc == 3 else 0
    return ng

def part1(lines):
    """
    >>> part1(t1)
    112
    """
    grid = parse(lines)
    for _ in range(6):
        grid = iterate(grid)
    return sum(grid.values())

def parse2(lines):
    grid = defaultdict(lambda: 0)
    for y, line in enumerate(lines):
        for x, val in enumerate(line):
            if val == '#':
                grid[(x, y, 0, 0)] = 1
    return grid

def adjacent2(pos):
    for d in itertools.product([-1, 0, 1], repeat=4):
        if d == (0, 0, 0, 0):
            continue
        yield (pos[0] + d[0], pos[1] + d[1], pos[2] + d[2], pos[3] + d[3])

def iterate2(grid):
    ng = defaultdict(lambda: 0)
    mins = list(map(lambda x: x - 1, map(min, zip(*grid.keys()))))
    maxs = list(map(lambda x: x + 2, map(max, zip(*grid.keys()))))
    ranges = map(lambda t: range(t[0], t[1]), zip(mins, maxs))
    for pos in itertools.product(*ranges):
        nc = sum(grid[tp] for tp in adjacent2(pos))
        if grid[pos] == 1 and nc in [2, 3]:
            ng[pos] = 1
        if grid[pos] == 0 and nc == 3:
            ng[pos] = 1
    return ng

def part2(lines):
    """
    >>> part2(t1)
    848
    """
    grid = parse2(lines)
    for _ in range(6):
        grid = iterate2(grid)
    return sum(grid.values())

def main():
    puzzle_input = adventofcode.read_input(17)
    adventofcode.answer(1, 267, part1(puzzle_input))
    adventofcode.answer(2, 1812, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
