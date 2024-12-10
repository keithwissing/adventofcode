#!/usr/bin/env python3
from collections import defaultdict
from itertools import product

import adventofcode

t1 = [
    '89010123',
    '78121874',
    '87430965',
    '96549874',
    '45678903',
    '32019012',
    '01329801',
    '10456732',
]

def add(pos, delta):
    return pos[0] + delta[0], pos[1] + delta[1]

def both(lines):
    width, height = len(lines[0]), len(lines)
    grid = defaultdict(lambda: '', {(x, y): int(lines[y][x]) for x in range(width) for y in range(height)})

    score = 0
    rating = 0

    deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for x, y in product(range(width), range(height)):
        if grid[(x, y)] == 0:
            peaks = set()
            steps = [((x, y), 0)]
            while steps:
                pos, h = steps.pop()
                for d in deltas:
                    if grid[add(pos, d)] == h + 1:
                        if h + 1 == 9:
                            rating += 1
                            peaks.add(add(pos, d))
                        else:
                            steps.append((add(pos, d), h + 1))
            score += len(peaks)

    return score, rating

def part1(lines):
    """
    >>> part1(t1)
    36
    """
    return both(lines)[0]

def part2(lines):
    """
    >>> part2(t1)
    81
    """
    return both(lines)[1]

def main():
    puzzle_input = adventofcode.read_input(10)
    adventofcode.answer(1, 754, part1(puzzle_input))
    adventofcode.answer(2, 1609, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
