#!/usr/bin/env python3

import adventofcode

t1 = '11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'

def is_invalid(val):
    test = str(val)
    if test[0:(len(test)//2)] == test[(len(test)//2):]:
        return True
    return False

def is_invalid_2(val):
    """
    >>> is_invalid_2(11)
    True
    >>> is_invalid_2(1188511885)
    True
    """
    test = str(val)
    for l in range(1, len(test)//2+1):
        if test == test[0:l] * (len(test) // l):
            return True
    return False

def run(line, test_func):
    ranges = line.split(',')
    total = 0
    for r in ranges:
        low, hi = (int(x) for x in r.split('-'))
        for val in range(low, hi+1):
            if test_func(val):
                total += val
    return total

def part1(lines):
    """
    >>> part1(t1)
    1227775554
    """
    return run(lines, is_invalid)

def part2(lines):
    """
    >>> part2(t1)
    4174379265
    """
    return run(lines, is_invalid_2)

def main():
    puzzle_input = adventofcode.read_input(2)
    adventofcode.answer(1, 19219508902, part1(puzzle_input))
    adventofcode.answer(2, 27180728081, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
