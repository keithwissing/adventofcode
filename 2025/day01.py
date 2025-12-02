#!/usr/bin/env python3

import adventofcode

t1 = [
    'L68',
    'L30',
    'R48',
    'L5',
    'R60',
    'L55',
    'L1',
    'L99',
    'R14',
    'L82',
]

def part1(lines):
    """
    >>> part1(t1)
    3
    """
    pos = 50
    count = 0
    for line in lines:
        d = -1 if line[0] == 'L' else 1
        v = int(line[1:])
        pos = (pos + d*v) % 100
        if pos == 0:
            count += 1
    return count

def part2(lines):
    """
    >>> part2(t1)
    6
    >>> part2(['R1000'])
    10
    """
    pos = 50
    count = 0
    for line in lines:
        d = -1 if line[0] == 'L' else 1
        v = int(line[1:])
        while v > 0:
            pos = (pos + d) % 100
            v -= 1
            if pos == 0:
                count += 1
    return count

def main():
    puzzle_input = adventofcode.read_input(1)
    adventofcode.answer(1, 1135, part1(puzzle_input))
    adventofcode.answer(2, 6558, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
