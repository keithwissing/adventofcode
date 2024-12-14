#!/usr/bin/env python3
import re
from collections import defaultdict
from functools import reduce

import adventofcode

t1 = [
    'p=0,4 v=3,-3',
    'p=6,3 v=-1,-3',
    'p=10,3 v=-1,2',
    'p=2,0 v=2,-1',
    'p=0,0 v=1,3',
    'p=3,0 v=-2,-2',
    'p=7,6 v=-1,-3',
    'p=3,0 v=-1,-2',
    'p=9,3 v=2,3',
    'p=7,3 v=-1,2',
    'p=2,4 v=2,-3',
    'p=9,5 v=-3,-3',
]

def parse(lines):
    robots = []
    for line in lines:
        numbers = tuple(int(x) for x in re.findall(r'[\d-]+', line))
        robots.append(numbers)
    return robots

def iterate(robots, width, height):
    return [((r[0] + r[2]) % width, (r[1] + r[3]) % height, r[2], r[3]) for r in robots]

def safety(robots, width, height):
    bots = [0] * 4
    cx, cy = width // 2, height // 2
    for robot in robots:
        x, y, _, _ = robot
        if x == cx or y == cy:
            continue
        lr = 0 if x < cx else 1
        tb = 0 if y < cy else 1
        quad = lr | tb << 1
        bots[quad] += 1
    return reduce(lambda a, b: a * b, bots, 1)

def as_str(robots, width, height):
    d = defaultdict(lambda: 0)
    for r in robots:
        d[(r[0], r[1])] += 1
    return "\n".join(''.join(str(d[(x, y)] or '.') for x in range(width)) for y in range(height))

def part1(lines, width, height):
    """
    >>> part1(t1, 11, 7)
    12
    """
    robots = parse(lines)
    for _ in range(100):
        robots = iterate(robots, width, height)
    return safety(robots, width, height)

def part2(lines, width, height):
    robots = parse(lines)
    for i in range(1000000):
        robots = iterate(robots, width, height)
        pic = as_str(robots, width, height)
        if '1111111111111111111111111111111' in pic:
            print(pic)
            return i + 1

def main():
    puzzle_input = adventofcode.read_input(14)
    adventofcode.answer(1, 232253028, part1(puzzle_input, 101, 103))
    adventofcode.answer(2, 8179, part2(puzzle_input, 101, 103))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
