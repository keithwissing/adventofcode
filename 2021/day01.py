#!/usr/bin/env python3

import adventofcode

t1 = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263,
]

def part1(lines):
    """
    >>> part1(t1)
    7
    """
    count = 0
    for i, v in enumerate(lines):
        if i > 0 and v > lines[i-1]:
            count += 1
    return count

def part2(lines):
    """
    >>> part2(t1)
    5
    """
    count = 0
    for i in range(2, len(lines)-1):
        if sum(lines[i-1:i+2]) > sum(lines[i-2:i+1]):
            count += 1
    return count

def main():
    puzzle_input = adventofcode.read_input(1)
    puzzle_input = [int(x) for x in puzzle_input]
    adventofcode.answer(1, 1754, part1(puzzle_input))
    adventofcode.answer(2, 1789, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
