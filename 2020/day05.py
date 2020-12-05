#!/usr/bin/env python3

import adventofcode

def seatid(code):
    """
    >>> seatid('BFFFBBFRRR')
    567
    """
    ids = code.replace('B', '1').replace('F', '0').replace('L', '0').replace('R', '1')
    return int(ids, 2)

def part1(lines):
    return max([seatid(l) for l in lines])

def part2(lines):
    seats = [seatid(l) for l in lines]
    a = [x+1 for x in seats if x+1 not in seats and x+2 in seats]
    return a[0]

def main():
    puzzle_input = adventofcode.read_input(5)
    adventofcode.answer(1, 904, part1(puzzle_input))
    adventofcode.answer(2, 669, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
