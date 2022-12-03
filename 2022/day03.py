#!/usr/bin/env python3
from functools import reduce
from string import ascii_letters

import adventofcode

t1 = [
    'vJrwpWtwJgWrhcsFMMfFFhFp',
    'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
    'PmmdzqPrVvPwwTWBwg',
    'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
    'ttgJtRGJQctTZtZT',
    'CrZsJsPPZsGzwwsLwLmpwMDw',
]

def priority(c):
    return ascii_letters.index(c) + 1

def in_both_compartments(line):
    f = set([c for c in line[:(len(line) // 2)]])
    s = set([c for c in line[(len(line) // 2):]])
    return f.intersection(s).pop()

def part1(lines):
    """
    >>> part1(t1)
    157
    """
    return sum(priority(in_both_compartments(line)) for line in lines)

def badge(lines):
    s = [set(c for c in line) for line in lines]
    return reduce(lambda x, y: x.intersection(y), s).pop()

def groups_of_three(lines):
    for p in range(0, len(lines), 3):
        yield lines[p:p + 3]

def part2(lines):
    """
    >>> part2(t1)
    70
    """
    return sum(priority(badge(g)) for g in groups_of_three(lines))

def main():
    puzzle_input = adventofcode.read_input(3)
    adventofcode.answer(1, 7875, part1(puzzle_input))
    adventofcode.answer(2, 2479, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
