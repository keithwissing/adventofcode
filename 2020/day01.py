#!/usr/bin/env python3

import itertools
import adventofcode

def part1(entries):
    """
    >>> part1([1721, 979, 366, 299, 675, 1456])
    514579
    """
    for t in itertools.combinations(entries, 2):
        if t[0] + t[1] == 2020:
            return t[0] * t[1]

def part2(entries):
    """
    >>> part2([1721, 979, 366, 299, 675, 1456])
    241861950
    """
    for t in itertools.combinations(entries, 3):
        if t[0] + t[1] + t[2] == 2020:
            return t[0] * t[1] * t[2]

def main():
    puzzle_input = adventofcode.read_input(1)
    puzzle_input = [int(x) for x in puzzle_input]
    adventofcode.answer(1, 1019371, part1(puzzle_input))
    adventofcode.answer(2, 278064990, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
