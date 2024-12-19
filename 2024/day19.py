#!/usr/bin/env python3
import functools

import adventofcode

t1 = [
    'r, wr, b, g, bwu, rb, gb, br',
    '',
    'brwrr',
    'bggr',
    'gbbr',
    'rrbgbr',
    'ubwu',
    'bwurrg',
    'brgr',
    'bbrgwb',
]

def can_make(design, towels):
    @functools.cache
    def can(design):
        for t in towels:
            if design == t:
                return True
            if design.startswith(t) and can(design[len(t):]):
                return True
        return False

    return can(design)

def part1(lines):
    """
    >>> part1(t1)
    6
    """
    towels = lines[0].split(', ')
    designs = lines[2:]
    return sum(can_make(design, towels) for design in designs)

def possibles(design, towels):
    @functools.cache
    def can(design):
        total = 0
        for t in towels:
            if design == t:
                total += 1
            if design.startswith(t):
                total += can(design[len(t):])
        return total

    return can(design)

def part2(lines):
    """
    >>> part2(t1)
    16
    """
    towels = lines[0].split(', ')
    designs = lines[2:]
    return sum(possibles(d, towels) for d in designs)

def main():
    puzzle_input = adventofcode.read_input(19)
    adventofcode.answer(1, 298, part1(puzzle_input))
    adventofcode.answer(2, 572248688842069, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
