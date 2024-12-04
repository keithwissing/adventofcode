#!/usr/bin/env python3
from collections import defaultdict
from itertools import permutations, product

import adventofcode

t1 = [
    'MMMSXXMASM',
    'MSAMXMSMSA',
    'AMXSXMAAMM',
    'MSAMASMSMX',
    'XMASAMXAMM',
    'XXAMMXXAMA',
    'SMSMSASXSS',
    'SAXAMASAAA',
    'MAMMMXMMMM',
    'MXMXAXMASX',
]

def add(pos, delta):
    return pos[0] + delta[0], pos[1] + delta[1]

def part1(lines):
    """
    >>> part1(t1)
    18
    """
    width, height = len(lines[0]), len(lines)
    grid = defaultdict(lambda: '.', {(x, y): lines[y][x] for x in range(0, width) for y in range(0, height)})
    total = 0
    for y in range(0, height):
        for x in range(0, width):
            if grid[(x, y)] == 'X':
                for delta in product([-1, 0, 1], [-1, 0, 1]):
                    if delta == [0, 0]:
                        continue
                    pos = (x, y)
                    val = ''
                    for _ in range(4):
                        val += grid[pos]
                        pos = add(pos, delta)
                    if val == 'XMAS':
                        total += 1
    return total

def part2(lines):
    """
    >>> part2(t1)
    9
    """
    width, height = len(lines[0]), len(lines)
    grid = defaultdict(lambda: '.', {(x, y): lines[y][x] for x in range(0, width) for y in range(0, height)})
    total = 0
    for y in range(0, height):
        for x in range(0, width):
            if grid[(x, y)] == 'A':
                a = grid[add((x, y), (-1, -1))] + grid[add((x, y), (1, 1))]
                b = grid[add((x, y), (-1, 1))] + grid[add((x, y), (1, -1))]
                if all(t in ['MS', 'SM'] for t in [a, b]):
                    total += 1
    return total

def main():
    puzzle_input = adventofcode.read_input(4)
    adventofcode.answer(1, 2401, part1(puzzle_input))
    adventofcode.answer(2, 1822, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
