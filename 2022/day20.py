#!/usr/bin/env python3

import adventofcode

t1 = [1, 2, -3, 3, -2, 0, 4, ]

def mix(file):
    pass

def part1(lines):
    """
    >>> part1(t1)
    3
    """

def part2(lines):
    """
    # >>> part2(t1)
    """

def main():
    puzzle_input = adventofcode.read_input(20)
    puzzle_input = [int(x) for x in puzzle_input]
    adventofcode.answer(1, 0, part1(puzzle_input))
    # adventofcode.answer(2, 0, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
