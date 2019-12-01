#!/usr/bin/env python3

import adventofcode

def fuel(mass):
    """
    >>> fuel(100756)
    33583
    """
    return mass // 3 - 2

def plus_fuel(mass):
    total = fuel(mass)
    more = fuel(total)
    while more > 0:
        total += more
        more = fuel(more)
    return total

def part1(masses):
    return sum([fuel(x) for x in masses])

def part2(masses):
    """
    >>> part2([1969])
    966
    >>> part2([100756])
    50346
    """
    return sum([plus_fuel(x) for x in masses])

def main():
    puzzle_input = adventofcode.read_input(1)
    puzzle_input = [int(x) for x in puzzle_input]
    adventofcode.answer(1, 3219099, part1(puzzle_input))
    adventofcode.answer(2, 4825810, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
