#!/usr/bin/env python3

from collections import defaultdict
import adventofcode

t1 = [
    '0,9 -> 5,9',
    '8,0 -> 0,8',
    '9,4 -> 3,4',
    '2,2 -> 2,1',
    '7,0 -> 7,4',
    '6,4 -> 2,0',
    '0,9 -> 2,9',
    '3,4 -> 1,4',
    '0,0 -> 8,8',
    '5,5 -> 8,2',
]

def parse(line):
    a = [int(x) for x in line.replace(' -> ', ' ').replace(',', ' ').split()]
    return a

def part1(lines):
    """
    >>> part1(t1)
    5
    """
    grid = defaultdict(lambda: 0)
    for line in lines:
        a = parse(line)
        if a[0] == a[2]:
            l = min(a[1], a[3])
            h = max(a[1], a[3])
            for y in range(l, h + 1):
                grid[(a[0], y)] += 1
        if a[1] == a[3]:
            l = min(a[0], a[2])
            h = max(a[0], a[2])
            for x in range(l, h + 1):
                grid[(x, a[1])] += 1
    return sum([1 for k, v in grid.items() if v > 1])

def part2(lines):
    """
    >>> part2(t1)
    12
    """
    grid = defaultdict(lambda: 0)
    for line in lines:
        a = parse(line)
        x = a[0]
        y = a[1]
        delta = (1 if x < a[2] else -1 if x > a[2] else 0, 1 if y < a[3] else -1 if y > a[3] else 0)
        grid[(x, y)] += 1
        while x != a[2] or y != a[3]:
            x += delta[0]
            y += delta[1]
            grid[(x, y)] += 1
    return sum([1 for k, v in grid.items() if v > 1])

def main():
    puzzle_input = adventofcode.read_input(5)
    adventofcode.answer(1, 6856, part1(puzzle_input))
    adventofcode.answer(2, 20666, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
