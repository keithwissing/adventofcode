#!/usr/bin/env python3
from collections import Counter

import adventofcode

t1 = [
    '7 6 4 2 1',
    '1 2 7 8 9',
    '9 7 6 2 1',
    '1 3 2 4 5',
    '8 6 4 4 1',
    '1 3 6 7 9',
]

def is_safe(line):
    ds = [line[x + 1] - line[x] for x in range(len(line) - 1)]
    counts = Counter(ds)
    return all(k in [1, 2, 3] for k in counts.keys()) or all(k in [-1, -2, -3] for k in counts.keys())

def is_safe_2(line):
    if is_safe(line):
        return True
    for i in range(len(line)):
        if is_safe(line[:i] + line[i + 1:]):
            return True
    return False

def part1(lines):
    """
    >>> part1(t1)
    2
    """
    data = [[int(v) for v in l.split()] for l in lines]
    return sum(is_safe(line) for line in data)

def part2(lines):
    """
    >>> part2(t1)
    4
    """
    data = [[int(v) for v in l.split()] for l in lines]
    return sum(is_safe_2(line) for line in data)

def main():
    puzzle_input = adventofcode.read_input(2)
    adventofcode.answer(1, 524, part1(puzzle_input))
    adventofcode.answer(2, 569, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
