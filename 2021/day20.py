#!/usr/bin/env python3

from collections import defaultdict
from functools import reduce
from itertools import accumulate
import adventofcode

t1 = [
    '..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#',
    '',
    '#..#.',
    '#....',
    '##..#',
    '..#..',
    '..###',
]

def parse(lines):
    iia = lines[0]
    grid = defaultdict(lambda: '.')
    for y, row in enumerate(lines[2:]):
        for x, v in enumerate(row):
            if v == '#':
                grid[(x, y)] = '#'
    return iia, grid

def index(grid, pos):
    acc = []
    for y in range(pos[1] - 1, pos[1] + 2):
        for x in range(pos[0] - 1, pos[0] + 2):
            acc.append(grid[(x, y)])
    return int(''.join(acc).replace('.', '0').replace('#', '1'), 2)

def iterate(iia, grid, size, c):
    ng = defaultdict(lambda: iia[511] if grid[(10000, 0)] == '#' else iia[0])
    for y in range(0 - c, size + c):
        for x in range(0 - c, size + c):
            i = index(grid, (x, y))
            ng[(x, y)] = iia[i]
    return ng

def display(grid):
    limits = reduce(lambda a, b: (min(a[0], b[0]), min(a[1], b[1]), max(a[2], b[0]), max(a[3], b[1])), grid.keys(), (0, 0, 0, 0))
    for y in range(limits[1], limits[3] + 1):
        row = [grid[(x, y)] for x in range(limits[0], limits[2] + 1)]
        print(''.join(row))

def part1(lines):
    """
    >>> part1(t1)
    35
    """
    size = len(lines[2])
    iia, grid = parse(lines)
    for c in range(2):
        grid = iterate(iia, grid, size, c + 1)
    return sum(1 for x in grid.values() if x == '#')

def part2(lines):
    """
    >>> part2(t1)
    3351
    """
    size = len(lines[2])
    iia, grid = parse(lines)
    for c in range(50):
        grid = iterate(iia, grid, size, c + 1)
    return sum(1 for x in grid.values() if x == '#')

def main():
    puzzle_input = adventofcode.read_input(20)
    adventofcode.answer(1, 4968, part1(puzzle_input))
    adventofcode.answer(2, 16793, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
