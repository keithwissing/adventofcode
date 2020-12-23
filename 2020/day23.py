#!/usr/bin/env python3

import adventofcode

def iterate(cups):
    cc = len(cups)
    pick = cups[1:4]
    pulled = cups[:1] + cups[4:]
    dest = (cups[0] - 2) % cc + 1
    while dest not in pulled:
        dest = (dest - 2) % cc + 1
    idx = (pulled.index(dest) + 1) % cc
    rep = pulled[:idx] + pick + pulled[idx:]
    return rep[1:] + rep[:1]

def part1(lines, rounds):
    """
    >>> part1('389125467', 10)
    92658374
    >>> part1('389125467', 100)
    67384529
    """
    cups = [int(x) for x in lines]
    for _ in range(rounds):
        cups = iterate(cups)
    idx = (cups.index(1) + 1) % len(cups)
    return int(''.join(str(c) for c in cups[idx:] + cups[:idx - 1]))

def main():
    puzzle_input = adventofcode.read_input(23)
    puzzle_input = '925176834'
    adventofcode.answer(1, 69852437, part1(puzzle_input, 100))
    # adventofcode.answer(2, 0, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
