#!/usr/bin/env python3

import adventofcode

t1 = [
    '2-4,6-8',
    '2-3,4-5',
    '5-7,7-9',
    '2-8,3-7',
    '6-6,4-6',
    '2-6,4-8',
]

def fully_contained(p):
    if p[0] <= p[2] <= p[1] and p[0] <= p[3] <= p[1]:
        return True
    if p[2] <= p[0] <= p[3] and p[2] <= p[1] <= p[3]:
        return True
    return False

def overlap(p):
    if p[0] <= p[2] <= p[1] or p[0] <= p[3] <= p[1]:
        return True
    if p[2] <= p[0] <= p[3] or p[2] <= p[1] <= p[3]:
        return True
    return False

def part1(lines):
    """
    >>> part1(t1)
    2
    """
    lines = [[int(x) for x in line.replace('-', ' ').replace(',', ' ').split()] for line in lines]
    return sum(1 if fully_contained(p) else 0 for p in lines)

def part2(lines):
    """
    >>> part2(t1)
    4
    """
    lines = [[int(x) for x in line.replace('-', ' ').replace(',', ' ').split()] for line in lines]
    return sum(1 if overlap(p) else 0 for p in lines)

def main():
    puzzle_input = adventofcode.read_input(4)
    adventofcode.answer(1, 588, part1(puzzle_input))
    adventofcode.answer(2, 911, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
