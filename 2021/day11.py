#!/usr/bin/env python3

import heapq
from itertools import product, repeat, takewhile
import adventofcode

t1 = [
    '5483143223',
    '2745854711',
    '5264556173',
    '6141336146',
    '6357385478',
    '4167524645',
    '2176841721',
    '6882881134',
    '4846848554',
    '5283751526',
]

def parse(lines):
    return [[int(c) for c in r] for r in lines]

def adjacent(pos):
    for dy, dx in product(range(-1, 2), range(-1, 2)):
        if dx != 0 or dy != 0:
            yield (pos[0] + dx, pos[1] + dy)

def increase(grid, q, pos):
    x, y = pos
    if x >= 0 and y >= 0 and x < 10 and y < 10 and grid[y][x] < 10:
        grid[y][x] += 1
        if grid[y][x] == 10:
            for p in adjacent((x, y)):
                heapq.heappush(q, p)
            return 1
    return 0

def iterate(grid):
    q = []
    f = 0
    for y, x in product(range(10), range(10)):
        f += increase(grid, q, (x, y))
    while q:
        pos = heapq.heappop(q)
        f += increase(grid, q, pos)
    for y, x in product(range(10), range(10)):
        if grid[y][x] == 10:
            grid[y][x] = 0
    return f

def part1(lines):
    """
    >>> part1(t1)
    1656
    """
    grid = parse(lines)
    return sum(iterate(grid) for _ in range(100))

def part2(lines):
    """
    >>> part2(t1)
    195
    """
    grid = parse(lines)
    return sum(takewhile(lambda _: iterate(grid) != 100, repeat(1))) + 1

def main():
    puzzle_input = adventofcode.read_input(11)
    adventofcode.answer(1, 1591, part1(puzzle_input))
    adventofcode.answer(2, 314, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
