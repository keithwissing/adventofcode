#!/usr/bin/env python3

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
    if 'a' <= c <= 'z':
        return ord(c) - ord('a') + 1
    return ord(c) - ord('A') + 26 + 1

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
    x = set(c for c in lines[0])
    y = set(c for c in lines[1])
    z = set(c for c in lines[2])
    return x.intersection(y).intersection(z).pop()

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
