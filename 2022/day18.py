#!/usr/bin/env python3
from itertools import product

import adventofcode

t1 = [
    '2,2,2',
    '1,2,2',
    '3,2,2',
    '2,1,2',
    '2,3,2',
    '2,2,1',
    '2,2,3',
    '2,2,4',
    '2,2,6',
    '1,2,5',
    '3,2,5',
    '2,1,5',
    '2,3,5',
]

def parse(lines):
    return [tuple(int(i) for i in line.split(',')) for line in lines]

def adjacent(pos):
    for delta in product(*[range(-1, 2) for _ in range(len(pos))]):
        if sum(abs(x) for x in delta) == 1:
            yield tuple(x + y for x, y in zip(pos, delta))

def part1(lines):
    """
    >>> part1(t1)
    64
    """
    sides = 0
    points = set(parse(lines))
    for p in points:
        for t in adjacent(p):
            if t not in points:
                sides += 1
    return sides

def part2(lines):
    """
    >>> part2(t1)
    58
    """
    points = set(parse(lines))
    for i, c in enumerate(['x', 'y', 'z']):
        print(c, min(p[i] for p in points), max(p[i] for p in points))

def main():
    puzzle_input = adventofcode.read_input(18)
    adventofcode.answer(1, 3390, part1(puzzle_input))
    adventofcode.answer(2, 0, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
