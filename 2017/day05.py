#!/usr/bin/env python

import adventofcode

def escape_one(instr):
    """
    >>> escape_one([0, 3, 0, 1, -3])
    5
    """
    pos = 0
    count = 0
    while pos >= 0 and pos < len(instr):
        instr[pos] += 1
        pos += instr[pos] - 1
        count += 1
    return count

def escape_two(instr):
    """
    >>> escape_two([0, 3, 0, 1, -3])
    10
    """
    pos = 0
    count = 0
    while pos >= 0 and pos < len(instr):
        off = instr[pos]
        instr[pos] += 1 if off < 3 else -1
        pos += off
        count += 1
    return count

def main():
    puzzle_input = adventofcode.read_input(5)
    adventofcode.answer(1, 360603, escape_one([int(x) for x in puzzle_input]))
    adventofcode.answer(2, 25347697, escape_two([int(x) for x in puzzle_input]))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
