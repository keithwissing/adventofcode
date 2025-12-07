#!/usr/bin/env python3
from collections import defaultdict
from functools import cache

import adventofcode

t1 = [
    '.......S.......',
    '...............',
    '.......^.......',
    '...............',
    '......^.^......',
    '...............',
    '.....^.^.^.....',
    '...............',
    '....^.^...^....',
    '...............',
    '...^.^...^.^...',
    '...............',
    '..^...^.....^..',
    '...............',
    '.^.^.^.^.^...^.',
    '...............',
]

def part1(lines):
    """
    >>> part1(t1)
    21
    """
    grid = defaultdict(lambda: '.', {(x, y): c for y, line in enumerate(lines) for x, c in enumerate(line)})
    beams = set(p for p, v in grid.items() if v == 'S')
    splits = set()
    while beams:
        p = beams.pop()
        p = (p[0], p[1] + 1)
        while p[1] < len(lines):
            if grid[p] == '^':
                splits.add(p)
                beams.add((p[0] - 1, p[1]))
                beams.add((p[0] + 1, p[1]))
                break
            p = (p[0], p[1] + 1)
    return len(splits)

def part2(lines):
    """
    >>> part2(t1)
    40
    """
    grid = defaultdict(lambda: '.', {(x, y): c for y, line in enumerate(lines) for x, c in enumerate(line)})
    height = len(lines)

    @cache
    def routes(p):
        while p[1] < height:
            if grid[p] == '^':
                return routes((p[0] - 1, p[1])) + routes((p[0] + 1, p[1]))
            p = (p[0], p[1] + 1)
        return 1

    start = next((p for p, v in grid.items() if v == 'S'))
    return routes(start)

def main():
    puzzle_input = adventofcode.read_input(7)
    adventofcode.answer(1, 1642, part1(puzzle_input))
    adventofcode.answer(2, 47274292756692, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
