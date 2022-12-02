#!/usr/bin/env python3
from itertools import takewhile

import adventofcode

t1 = [
    '1000', '2000', '3000', '',
    '4000', '',
    '5000', '6000', '',
    '7000', '8000', '9000', '',
    '10000',
]

def groups(lines):
    pos = 0
    while pos < len(lines):
        group = list(takewhile(lambda x: x, lines[pos:]))
        pos += len(group) + 1
        yield group

def part1(lines):
    """
    >>> part1(t1)
    24000
    """
    return max(sum(int(x) for x in carry) for carry in groups(lines))

def part2(lines):
    """
    >>> part2(t1)
    45000
    """
    return sum(sorted(sum(int(x) for x in carry) for carry in groups(lines))[-3:])

def main():
    puzzle_input = adventofcode.read_input(1)
    adventofcode.answer(1, 69693, part1(puzzle_input))
    adventofcode.answer(2, 200945, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
