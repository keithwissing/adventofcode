#!/usr/bin/env python3

import adventofcode

t1 = [
    'forward 5',
    'down 5',
    'forward 8',
    'up 3',
    'down 8',
    'forward 2',
]

def part1(lines):
    """
    >>> part1(t1)
    150
    """
    x, y = 0, 0
    for line in lines:
        d, v = line.split()
        v = int(v)
        if d == 'forward':
            x += v
        elif d == 'down':
            y += v
        elif d == 'up':
            y -= v
    return x * y

def part2(lines):
    """
    >>> part2(t1)
    900
    """
    x, y, a = 0, 0, 0
    for line in lines:
        d, v = line.split()
        v = int(v)
        if d == 'forward':
            x += v
            y += a * v
        elif d == 'down':
            a += v
        elif d == 'up':
            a -= v
    return x * y

def main():
    puzzle_input = adventofcode.read_input(2)
    adventofcode.answer(1, 1507611, part1(puzzle_input))
    adventofcode.answer(2, 1880593125, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
