#!/usr/bin/env python3

import itertools
import adventofcode

t1 = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102,
      117, 150, 182, 127, 219, 299, 277, 309, 576]

def meets(lines, val):
    for t in itertools.combinations(lines, 2):
        if t[0] + t[1] == val:
            return True
    return False

def find_part1(lines, bs):
    """
    >>> find_part1(t1, 5)
    127
    """
    for p in range(bs, len(lines)):
        pv = lines[p - bs:p]
        tv = lines[p]
        if not meets(pv, tv):
            return tv
    raise 'Not Found'

def find_weakness(lines, val):
    """
    >>> find_weakness(t1, 127)
    62
    """
    f, l = 0, 1
    while True:
        tot = sum(lines[f:l])
        if tot == val:
            break
        elif tot > val:
            f += 1
        elif tot < val:
            l += 1
    r = lines[f:l]
    return min(r) + max(r)

def main():
    puzzle_input = adventofcode.read_input(9)
    puzzle_input = [int(x) for x in puzzle_input]
    adventofcode.answer(1, 36845998, p1 := find_part1(puzzle_input, 25))
    adventofcode.answer(2, 4830226, find_weakness(puzzle_input, p1))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
