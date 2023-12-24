#!/usr/bin/env python3
from itertools import combinations

import adventofcode

t1 = [
    '19, 13, 30 @ -2,  1, -2',
    '18, 19, 22 @ -1, -1, -2',
    '20, 25, 34 @ -2, -2, -4',
    '12, 31, 28 @ -1, -2, -1',
    '20, 19, 15 @  1, -5, -3',
]

def parse(lines):
    return [
        tuple(int(w) for w in line.replace(',', '').replace('@', '').split())
        for line in lines]

def sign(a):
    return -1 if a < 0 else 1 if a > 0 else 0

def part1(lines, least, most):
    """
    >>> part1(t1, 7, 27)
    2
    """
    stones = parse(lines)
    total = 0
    for a, b in combinations(stones, 2):
        slope1 = a[4] / a[3]
        slope2 = b[4] / b[3]
        if slope1 != slope2:
            point1 = (a[0], a[1])
            point2 = (b[0], b[1])
            i1 = - slope1 * point1[0] + point1[1]
            i2 = - slope2 * point2[0] + point2[1]
            x = (i2 - i1) / (slope1 - slope2)
            y = slope1 * x - slope1 * point1[0] + point1[1]
            if (least <= x <= most and least <= y <= most
                    and sign(x - point1[0]) == sign(a[3])
                    and sign(x - point2[0]) == sign(b[3])):
                total += 1
    return total

def part2(lines):
    """
    # >>> part2(t1)
    47
    """
    ipos, ivel = (24, 13, 10), (-3, 1, 2)

def main():
    puzzle_input = adventofcode.read_input(24)
    adventofcode.answer(0, 2, part1(t1, 7, 27))
    adventofcode.answer(1, 20847, part1(puzzle_input, 200000000000000, 400000000000000))
    # adventofcode.answer(2, 0, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
