#!/usr/bin/env python3
from collections import defaultdict
from itertools import product
from math import prod

import adventofcode

t1 = [
    '467..114..',
    '...*......',
    '..35..633.',
    '......#...',
    '617*......',
    '.....+.58.',
    '..592.....',
    '......755.',
    '...$.*....',
    '.664.598..',
]

def get_part_number(grid, x, y):
    if grid[(x - 1, y)].isdigit():
        return 0
    part = 0
    while grid[(x, y)].isdigit():
        part = part * 10 + int(grid[(x, y)])
        x += 1
    return part

def adjacent_symbols(grid, x, y, part):
    symbols = []
    for x1 in range(x - 1, x + len(str(part)) + 1):
        for y1 in range(y - 1, y + 2):
            symbols.append(grid[(x1, y1)])
    return [x for x in symbols if x != '.' and not x.isdigit()]

def part1(lines):
    """
    >>> part1(t1)
    4361
    """
    grid, height, width = parse_grid(lines)
    sum = 0
    for x, y in product(range(width), range(height)):
        part_number = get_part_number(grid, x, y)
        if part_number:
            symbols = adjacent_symbols(grid, x, y, part_number)
            if symbols:
                sum += part_number
    return sum

def parse_grid(lines):
    grid = defaultdict(lambda: '.')
    width = len(lines[0])
    height = len(lines)
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid[(x, y)] = c
    return grid, height, width

def find_adjacent_parts(grid, x, y):
    parts = set()
    for x1, y1 in product(range(x - 1, x + 2), range(y - 1, y + 2)):
        if grid[(x1, y1)].isdigit():
            x2 = x1
            while grid[(x2 - 1, y1)].isdigit():
                x2 -= 1
            parts.add(get_part_number(grid, x2, y1))
    return parts

def part2(lines):
    """
    >>> part2(t1)
    467835
    """
    grid, height, width = parse_grid(lines)
    sum = 0
    for x, y in product(range(width), range(height)):
        if grid[(x, y)] == '*':
            parts = find_adjacent_parts(grid, x, y)
            if len(parts) > 1:
                sum += prod(parts)
    return sum

def main():
    puzzle_input = adventofcode.read_input(3)
    adventofcode.answer(1, 549908, part1(puzzle_input))
    adventofcode.answer(2, 81166799, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
