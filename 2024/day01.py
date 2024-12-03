#!/usr/bin/env python3

import adventofcode

t1 = [
    '3   4',
    '4   3',
    '2   5',
    '1   3',
    '3   9',
    '3   3',
]

def part1(lines):
    """
    >>> part1(t1)
    11
    """
    lines = [l.split() for l in lines]
    lists = [[int(x[ln]) for x in lines] for ln in [0, 1]]
    lists = [sorted(l) for l in lists]
    pairs = zip(lists[0], lists[1])
    dists = [abs(i[1] - i[0]) for i in pairs]
    return sum(dists)

def part2(lines):
    """
    >>> part2(t1)
    31
    """
    lines = [l.split() for l in lines]
    lists = [[int(x[ln]) for x in lines] for ln in [0, 1]]
    lists = [sorted(l) for l in lists]
    return sum([i * lists[1].count(i) for i in lists[0]])

def main():
    puzzle_input = adventofcode.read_input(1)
    adventofcode.answer(1, 1882714, part1(puzzle_input))
    adventofcode.answer(2, 19437052, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
