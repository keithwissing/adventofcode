#!/usr/bin/env python3
from itertools import product, combinations

import adventofcode

t1 = [
    '...#......',
    '.......#..',
    '#.........',
    '..........',
    '......#...',
    '.#........',
    '.........#',
    '..........',
    '.......#..',
    '#...#.....',
]

def parse(lines):
    width, height = len(lines[0]), len(lines)
    galaxies = []
    for x, y in product(range(width), range(height)):
        if lines[y][x] == '#':
            galaxies.append((x, y))
    return galaxies, width, height

def find_expansions(galaxies, width, height):
    cols = set(x for x in range(width))
    rows = set(y for y in range(height))
    for x, y in galaxies:
        if x in cols:
            cols.remove(x)
        if y in rows:
            rows.remove(y)
    return cols, rows

def dist(a, b, e, age):
    n = min(a, b)
    x = max(a, b)
    return x - n + sum(i in e for i in range(n, x)) * (age - 1)

def part1(lines, age=2):
    """
    >>> part1(t1)
    374
    """
    g, w, h = parse(lines)
    c, r = find_expansions(g, w, h)
    tot = 0
    for ai, bi in combinations(range(len(g)), 2):
        a, b = g[ai], g[bi]
        distance = dist(a[0], b[0], c, age) + dist(a[1], b[1], r, age)
        tot += distance
    return tot

def part2(lines):
    """
    >>> part1(t1, 10)
    1030
    >>> part1(t1, 100)
    8410
    """
    return part1(lines, 1000000)

def main():
    puzzle_input = adventofcode.read_input(11)
    adventofcode.answer(1, 9522407, part1(puzzle_input))
    adventofcode.answer(2, 544723432977, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
