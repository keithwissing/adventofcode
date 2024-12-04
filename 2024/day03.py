#!/usr/bin/env python3
import itertools
import re
from functools import reduce

import adventofcode

t1 = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
t2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

def part1(lines):
    """
    >>> part1(t1)
    161
    """
    a = re.findall(r'mul\((\d+),(\d+)\)', lines)
    return sum(int(a) * int(b) for a, b in a)

def part2(lines):
    """
    >>> part2(t2)
    48
    """
    matches = re.findall(r'mul\((\d+),(\d+)\)|(do)\(\)|do(n)\'t\(\)', lines)
    # total = 0
    # include = True
    # for a, b, d, n in matches:
    #     if include and a and b:
    #         total += int(a) * int(b)
    #     include = (include or d) and not n
    # return total
    return reduce(
        lambda a, v: (a[0] + (int(v[0]) * int(v[1]) if v[0] and a[1] else 0), (a[1] or v[2]) and not v[3]),
        matches,
        (0, True)
    )[0]

def main():
    puzzle_input = adventofcode.read_input(3)
    puzzle_input = ''.join(puzzle_input)
    adventofcode.answer(1, 159892596, part1(puzzle_input))
    adventofcode.answer(2, 92626942, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
