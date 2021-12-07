#!/usr/bin/env python3

import adventofcode

def cost(crabs, target):
    return sum([abs(x - target) for x in crabs])

def cost2(crabs, target):
    return int(sum([abs(x - target) * (abs(x - target) + 1) / 2 for x in crabs]))

def search(crabs, cf):
    pos = 0
    last = cf(crabs, pos)
    t = cf(crabs, pos + 1)
    while t < last:
        pos += 1
        last = t
        t = cf(crabs, pos + 1)
    return last

def part1(crabs):
    """
    >>> part1([16,1,2,0,4,2,7,1,2,14])
    37
    """
    return search(crabs, cost)

def part2(lines):
    """
    >>> part2([16,1,2,0,4,2,7,1,2,14])
    168
    """
    return search(lines, cost2)

def main():
    puzzle_input = adventofcode.read_input(7)
    puzzle_input = [int(x) for x in puzzle_input.split(',')]
    adventofcode.answer(1, 342730, part1(puzzle_input))
    adventofcode.answer(2, 92335207, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
