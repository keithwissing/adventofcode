#!/usr/bin/env python3

import adventofcode

t1 = [
    'A Y',
    'B X',
    'C Z',
]

def translate(c):
    return {'A': 'R', 'B': 'P', 'C': 'S', 'X': 'R', 'Y': 'P', 'Z': 'S'}[c]

def outcome(i):
    if ''.join(i) in ['SR', 'RP', 'PS']:
        return 'win'
    if i[0] == i[1]:
        return 'draw'
    return 'loss'

def score(line):
    i = [translate(c) for c in line.split()]
    o = outcome(i)
    return 1 + 'RPS'.index(i[1]) + {'loss': 0, 'draw': 3, 'win': 6}[o]

def part1(lines):
    """
    >>> part1(t1)
    15
    """
    return sum(score(line) for line in lines)

def my_play(i):
    return 'RPS'[('RPS'.index(i[0]) + 'XYZ'.index(i[1]) - 1) % 3]

def score_2(line):
    i = line.split()
    i[0] = translate(i[0])
    i[1] = my_play(i)
    o = outcome(i)
    return 1 + 'RPS'.index(i[1]) + {'loss': 0, 'draw': 3, 'win': 6}[o]

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
