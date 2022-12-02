#!/usr/bin/env python3

import adventofcode

t1 = [
    'A Y',
    'B X',
    'C Z',
]

def to_number(c):
    return 'ABCXYZRPS'.index(c) % 3

def outcome(i):
    return [3, 6, 0][(to_number(i[1]) - to_number(i[0]) + 3) % 3]

def score(line):
    i = line.split()
    return 1 + to_number(i[1]) + outcome(i)

def my_play(i):
    return 'RPS'[('ABC'.index(i[0]) + 'XYZ'.index(i[1]) - 1) % 3]

def score_2(line):
    i = line.split()
    i[1] = my_play(i)
    return 1 + to_number(i[1]) + outcome(i)

def part1(lines):
    """
    >>> part1(t1)
    15
    """
    return sum(score(line) for line in lines)

def part2(lines):
    """
    >>> part2(t1)
    12
    """
    return sum(score_2(line) for line in lines)

def main():
    puzzle_input = adventofcode.read_input(2)
    adventofcode.answer(1, 9241, part1(puzzle_input))
    adventofcode.answer(2, 14610, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
