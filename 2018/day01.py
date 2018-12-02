#!/usr/bin/env python

import adventofcode

def resulting_frequency(puzzle_input):
    """
    >>> resulting_frequency([+1, +1, +1])
    3
    """
    return sum(puzzle_input)

def first_duplicate_frequency(puzzle_input):
    """
    >>> first_duplicate_frequency([+1, -1])
    0
    >>> first_duplicate_frequency([+3, +3, +4, -2, -4])
    10
    >>> first_duplicate_frequency([-6, +3, +8, +5, -6])
    5
    >>> first_duplicate_frequency([+7, +7, -2, -7, -4])
    14
    """
    seen = set()
    freq = 0
    pos = 0
    while freq not in seen:
        seen.add(freq)
        freq += puzzle_input[pos%len(puzzle_input)]
        pos += 1
    return freq

def main():
    puzzle_input = adventofcode.read_input(1)
    puzzle_input = [int(x) for x in puzzle_input]
    adventofcode.answer(1, 400, resulting_frequency(puzzle_input))
    adventofcode.answer(2, 232, first_duplicate_frequency(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
