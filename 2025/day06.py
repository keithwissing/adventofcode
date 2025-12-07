#!/usr/bin/env python3
import operator
from functools import reduce

import adventofcode

t1 = [
    '123 328  51 64 ',
    ' 45 64  387 23 ',
    '  6 98  215 314',
    '*   +   *   +  ',
]

def part1(lines):
    """
    >>> part1(t1)
    4277556
    """
    rows = [x.split() for x in lines]
    total = 0
    for x in range(len(rows[0])):
        if rows[-1][x] == '+':
            val = sum(int(r[x]) for r in rows[:-1])
        if rows[-1][x] == '*':
            val = reduce(operator.mul, (int(r[x]) for r in rows[:-1]), 1)
        total += val
    return total

def part2(lines):
    """
    >>> part2(t1)
    3263827
    """
    rows = lines
    total = 0
    vals = []
    for x in range(len(rows[0]) - 1, -1, -1):
        col = [r[x] for r in rows[:-1]]
        if all(c == ' ' for c in col):
            vals = []
        cv = ''.join(col).strip()
        if cv:
            vals.append(cv)
        if x < len(rows[-1]) and rows[-1][x] != ' ':
            if rows[-1][x] == '+':
                val = sum(int(x) for x in vals)
            if rows[-1][x] == '*':
                val = reduce(operator.mul, (int(x) for x in vals), 1)
            total += val
    return total

def main():
    puzzle_input = adventofcode.read_input(6)
    adventofcode.answer(1, 8108520669952, part1(puzzle_input))
    adventofcode.answer(2, 11708563470209, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
