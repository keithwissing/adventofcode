#!/usr/bin/env python3

from itertools import product
import adventofcode

def parse(line):
    p = line.replace('=', ' ').replace('.', ' ').replace(',', ' ').split()
    return ((int(p[3]), int(p[4])), (int(p[6]), int(p[7])))

def shoot(target, initial):
    pos = (0, 0)
    vel = initial
    hit = False
    high = 0
    while pos[1] >= target[1][0]:
        pos = (pos[0] + vel[0], pos[1] + vel[1])
        if high < pos[1]:
            high = pos[1]
        d = 1 if vel[0] < 0 else -1 if vel[0] > 0 else 0
        vel = (vel[0] + d, vel[1] - 1)
        if target[0][0] <= pos[0] <= target[0][1] and target[1][0] <= pos[1] <= target[1][1]:
            hit = True
            break
    return hit, high

def part1(lines):
    """
    >>> part1('target area: x=20..30, y=-10..-5')
    45
    """
    target = parse(lines)
    mh = 0
    for x, y in product(range(100), range(200)):
        h, hi = shoot(target, (x, y))
        if h and mh < hi:
            mh = hi
    return mh

def part2(lines):
    """
    >>> part2('target area: x=20..30, y=-10..-5')
    112
    """
    target = parse(lines)
    mh = 0
    hits = []
    for x, y in product(range(0, 250), range(-150, 150)):
        h, _ = shoot(target, (x, y))
        if h:
            hits.append((x, y))
    # print(min(x for x, y in hits))
    # print(max(x for x, y in hits))
    # print(min(y for x, y in hits))
    # print(max(y for x, y in hits))
    return len(hits)

def main():
    puzzle_input = adventofcode.read_input(17)
    adventofcode.answer(1, 8646, part1(puzzle_input))
    adventofcode.answer(2, 5945, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
