#!/usr/bin/env python3
from functools import reduce
from itertools import product

import adventofcode

t1 = [
    '30373',
    '25512',
    '65332',
    '33549',
    '35390',
]

def valid(pos, size):
    return 0 <= pos[0] < size and 0 <= pos[1] < size

def is_visible(grid, tree):
    height = grid[tree[1]][tree[0]]
    for delta in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        heights = []
        pos = tree
        pos = tuple(x + y for x, y in zip(pos, delta))
        while valid(pos, len(grid)):
            heights.append(grid[pos[1]][pos[0]])
            pos = tuple(x + y for x, y in zip(pos, delta))
        if len(heights) == 0 or max(heights) < height:
            return True
    return False

def part1(lines):
    """
    >>> part1(t1)
    21
    """
    size = len(lines)
    return sum(1 for pos in product(range(size), range(size)) if is_visible(lines, pos))

def score(grid, tree):
    height = grid[tree[1]][tree[0]]
    distance = []
    for delta in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        pos = tree
        d = 0
        pos = tuple(x + y for x, y in zip(pos, delta))
        while valid(pos, len(grid)):
            d += 1
            if grid[pos[1]][pos[0]] >= height:
                break
            pos = tuple(x + y for x, y in zip(pos, delta))
        distance.append(d)
    return reduce(lambda x, y: x * y, distance)

def part2(lines):
    """
    >>> part2(t1)
    8
    """
    size = len(lines)
    return max(score(lines, pos) for pos in product(range(size), range(size)))

def main():
    puzzle_input = adventofcode.read_input(8)
    adventofcode.answer(1, 1835, part1(puzzle_input))
    adventofcode.answer(2, 263670, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
