#!/usr/bin/env python3

from collections import Counter
import adventofcode

t1 = [
    'abc',
    '',
    'a',
    'b',
    'c',
    '',
    'ab',
    'ac',
    '',
    'a',
    'a',
    'a',
    'a',
    '',
    'b',
]

def groups(lines):
    group = []
    for l in lines:
        if len(l) < 1:
            if len(group) > 0:
                yield group
            group = []
        else:
            group.append(l)
    if len(group) > 0:
        yield group

def part1(lines):
    """
    >>> part1(t1)
    11
    """
    return sum([len(Counter(''.join(group)).keys()) for group in groups(lines)])

def part2(lines):
    """
    >>> part2(t1)
    6
    """
    tot = 0
    for group in groups(lines):
        a = [set(l) for l in group]
        b = a[0]
        for c in a[1:]:
            b &= c
        tot += len(b)
    return tot

def main():
    puzzle_input = adventofcode.read_input(6)
    adventofcode.answer(1, 6532, part1(puzzle_input))
    adventofcode.answer(2, 3427, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
