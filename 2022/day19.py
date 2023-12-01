#!/usr/bin/env python3

import adventofcode

t1 = [
    'Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.',
    'Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.',
]

def parse(lines):
    for line in lines:
        yield tuple(int(x) for x in line.replace(':', '').split() if x.isdigit())

def run(bp):
    state = ((1, 0, 0, 0), (0, 0, 0, 0))

def part1(lines):
    """
    >>> part1(t1)
    33
    """
    blueprints = list(parse(lines))

def part2(lines):
    """
    # >>> part2(t1)
    """

def main():
    puzzle_input = adventofcode.read_input(19)
    # puzzle_input = [int(x) for x in puzzle_input]
    # adventofcode.answer(1, 0, part1(puzzle_input))
    # adventofcode.answer(2, 0, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
