#!/usr/bin/env python3

from collections import defaultdict
from itertools import product
import adventofcode

t1 = [
    '.#.',
    '..#',
    '###',
]

def parse(lines, dims=3):
    grid = defaultdict(lambda: 0)
    for y, line in enumerate(lines):
        for x, val in enumerate(line):
            if val == '#':
                grid[tuple([x, y] + [0] * (dims - 2))] = 1
    return grid

def adjacent(pos):
    if len(pos) == 3:
        return adjacent3(pos)
    if len(pos) == 4:
        return adjacent4(pos)
    return adjacent0(pos)

def adjacent0(pos):
    zero = tuple([0] * len(pos))
    for delta in product([-1, 0, 1], repeat=len(pos)):
        if delta == zero:
            continue
        yield tuple([a + b for a, b in zip(pos, delta)])
        # yield tuple(map(sum, zip(pos, delta)))
        # yield tuple(sum(x) for x in zip(pos, delta))

def adjacent3(pos):
    for d in product([-1, 0, 1], repeat=3):
        if d == (0, 0, 0):
            continue
        yield (pos[0] + d[0], pos[1] + d[1], pos[2] + d[2])

def adjacent4(pos):
    for d in product([-1, 0, 1], repeat=4):
        if d == (0, 0, 0, 0):
            continue
        yield (pos[0] + d[0], pos[1] + d[1], pos[2] + d[2], pos[3] + d[3])

def iterate(grid):
    ng = defaultdict(lambda: 0)
    limits = [(min(c) - 1, max(c) + 2) for c in zip(*grid.keys())]
    ranges = map(lambda t: range(t[0], t[1]), limits)
    for pos in product(*ranges):
        nc = sum(grid[tp] for tp in adjacent(pos))
        if grid[pos] == 1 and nc in [2, 3]:
            ng[pos] = 1
        if grid[pos] == 0 and nc == 3:
            ng[pos] = 1
    return ng

def solve(lines, dims=3):
    grid = parse(lines, dims)
    for _ in range(6):
        grid = iterate(grid)
    return sum(grid.values())

def part1(lines):
    """
    >>> part1(t1)
    112
    """
    return solve(lines, 3)

def part2(lines):
    """
    >>> part2(t1)
    848
    """
    return solve(lines, 4)

def main():
    puzzle_input = adventofcode.read_input(17)
    adventofcode.answer(1, 267, part1(puzzle_input))
    adventofcode.answer(2, 1812, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
