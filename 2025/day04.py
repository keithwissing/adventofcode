#!/usr/bin/env python3
from collections import defaultdict
from itertools import product

import adventofcode

t1 = [
    '..@@.@@@@.',
    '@@@.@.@.@@',
    '@@@@@.@.@@',
    '@.@@@@..@.',
    '@@.@@@@.@@',
    '.@@@@@@@.@',
    '.@.@.@.@@@',
    '@.@@@.@@@@',
    '.@@@@@@@@.',
    '@.@.@@@.@.',
]

def adjacent1(pos):
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dy != 0 or dx != 0:
                yield pos[0] + dx, pos[1] + dy

def adjacent2(pos):
    for d in product([-1, 0, 1], repeat=2):
        if d != (0, 0):
            yield pos[0] + d[0], pos[1] + d[1]

def adjacent3(pos):
    for dy, dx in product(range(-1, 2), range(-1, 2)):
        if dx != 0 or dy != 0:
            yield pos[0] + dx, pos[1] + dy

def adjacent4(pos): # This one is slowest
    for delta in product(*[range(-1, 2) for _ in range(len(pos))]):
        if any(a != 0 for a in delta):
            yield tuple(x + y for x, y in zip(pos, delta))

adjacent = adjacent1

def part1(lines):
    """
    >>> part1(t1)
    13
    """
    grid = defaultdict(lambda: '.', {(x, y): c for y, line in enumerate(lines) for x, c in enumerate(line)})
    total = 0
    for y in range(0, len(lines)):
        for x in range(0, len(lines[y])):
            if grid[(x, y)] == '@' and sum(grid[p] == '@' for p in adjacent((x, y))) < 4:
                total += 1
    return total

def part2(lines):
    """
    >>> part2(t1)
    43
    """
    grid = defaultdict(lambda: '.', {(x, y): c for y, line in enumerate(lines) for x, c in enumerate(line)})
    total = 0
    last = -1
    while last != total:
        last = total
        for y in range(0, len(lines)):
            for x in range(0, len(lines[y])):
                if grid[(x, y)] == '@' and sum(grid[p] == '@' for p in adjacent((x, y))) < 4:
                    total += 1
                    grid[(x, y)] = '.'
    return total

def main():
    puzzle_input = adventofcode.read_input(4)
    adventofcode.answer(1, 1604, part1(puzzle_input))
    adventofcode.answer(2, 9397, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
