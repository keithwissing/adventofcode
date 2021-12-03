#!/usr/bin/env python3

import adventofcode

t1 = [
    '00100',
    '11110',
    '10110',
    '10111',
    '10101',
    '01111',
    '00111',
    '11100',
    '10000',
    '11001',
    '00010',
    '01010',
]

def part1(lines):
    """
    >>> part1(t1)
    198
    """
    counts = [0] * len(lines[0])
    for line in lines:
        for i, v in enumerate(line):
            if v == '1':
                counts[i] += 1
    gama = ['0'] * len(lines[0])
    epsilon = ['0'] * len(lines[0])
    for i in range(len(counts)):
        if counts[i] > len(lines) / 2:
            gama[i] = '1'
        else:
            epsilon[i] = '1'
    g = int(''.join(gama), base=2)
    e = int(''.join(epsilon), base=2)
    return g * e

def find_value(lines, val):
    remaining = lines[:]
    pos = 0
    while len(remaining) > 1:
        ones = sum([1 for l in remaining if l[pos] == '1'])
        target = val if ones >= len(remaining) / 2 else 1 - val
        remaining = [l for l in remaining if l[pos] == str(target)]
        pos += 1
    return int(''.join(remaining[0]), base=2)

def part2(lines):
    """
    >>> part2(t1)
    230
    """
    oxygen = find_value(lines, 1)
    co2 = find_value(lines, 0)
    return oxygen * co2

def main():
    puzzle_input = adventofcode.read_input(3)
    adventofcode.answer(1, 3895776, part1(puzzle_input))
    adventofcode.answer(2, 7928162, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
