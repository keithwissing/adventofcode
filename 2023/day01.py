#!/usr/bin/env python3

import adventofcode

t1 = [
    '1abc2',
    'pqr3stu8vwx',
    'a1b2c3d4e5f',
    'treb7uchet'
]

t2 = [
    'two1nine',
    'eightwothree',
    'abcone2threexyz',
    'xtwone3four',
    '4nineeightseven2',
    'zoneight234',
    '7pqrstsixteen',
]

def part1(lines):
    """
    >>> part1(t1)
    142
    """
    sum = 0
    for line in lines:
        digits = [int(x) for x in line if x.isdigit()]
        sum += digits[0] * 10 + digits[-1]
    return sum

def digit(line):
    spelled = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    if line[0].isdigit():
        return int(line[0])
    for i, w in enumerate(spelled):
        if line.startswith(w):
            return i + 1
    return None

def part2(lines):
    """
    >>> part2(t2)
    281
    """
    sum = 0
    for line in lines:
        for i in range(len(line)):
            d = digit(line[i:])
            if d is not None:
                first = d
                break
        for i in range(len(line) - 1, -1, -1):
            d = digit(line[i:])
            if d is not None:
                last = d
                break
        sum += first * 10 + last
    return sum

def main():
    puzzle_input = adventofcode.read_input(1)
    adventofcode.answer(1, 54597, part1(puzzle_input))
    adventofcode.answer(2, 54504, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
