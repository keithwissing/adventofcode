#!/usr/bin/env python3
from itertools import takewhile

import adventofcode

t1 = [

]

def part1(lines):
    """
    >>> part1(t1)
    0
    """
    ret = 0
    pos = 0
    while pos < len(lines):
        carry = list(takewhile(lambda x: x, lines[pos:]))
        total = sum(int(x) for x in carry)
        if total > ret:
            ret = total
        pos += len(carry) + 1
    return ret

def part2(lines):
    """
    >>> part2(t1)
    0
    """
    vals = []
    pos = 0
    while pos < len(lines):
        carry = list(takewhile(lambda x: x, lines[pos:]))
        vals.append(sum(int(x) for x in carry))
        pos += len(carry) + 1
    return sum(list(reversed(sorted(vals)))[:3])

def main():
    puzzle_input = adventofcode.read_input(1)
    adventofcode.answer(1, 69693, part1(puzzle_input))
    adventofcode.answer(2, 200945, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
