#!/usr/bin/env python3

import adventofcode

def main():
    puzzle_input = adventofcode.read_input(0)
    puzzle_input = [int(x) for x in puzzle_input]
    # adventofcode.answer(1, 0, part1(puzzle_input))
    # adventofcode.answer(2, 0, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
