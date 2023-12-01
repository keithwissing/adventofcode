#!/usr/bin/env python3

import adventofcode

def search(line, u):
    for p in range(len(line)):
        # if max(Counter(line[p:p + u]).values()) == 1:
        if len(set(line[p:p + u])) == u:
            return p + u

def part1(line):
    """
    >>> part1('mjqjpqmgbljsphdztnvjfqwrcgsmlb')
    7
    """
    return search(line, 4)

def part2(line):
    """
    >>> part2('mjqjpqmgbljsphdztnvjfqwrcgsmlb')
    19
    """
    return search(line, 14)

def main():
    puzzle_input = adventofcode.read_input(6)
    adventofcode.answer(1, 1987, part1(puzzle_input))
    adventofcode.answer(2, 3059, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
