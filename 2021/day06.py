#!/usr/bin/env python3

import adventofcode

def iterate(fish):
    n = fish[1:] + fish[:1]
    n[6] += fish[0]
    return n

def part1(input, days):
    """
    >>> part1([3,4,3,1,2], 80)
    5934
    >>> part1([3,4,3,1,2], 256)
    26984457539
    """
    fish = [input.count(x) for x in range(9)]
    for _ in range(days):
        fish = iterate(fish)
    return sum(fish)

def main():
    puzzle_input = adventofcode.read_input(6)
    puzzle_input = [int(x) for x in puzzle_input.split(',')]
    adventofcode.answer(1, 350605, part1(puzzle_input, 80))
    adventofcode.answer(2, 1592778185024, part1(puzzle_input, 256))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
