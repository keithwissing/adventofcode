#!/usr/bin/env python3

import adventofcode

t1 = [
    '987654321111111',
    '811111111111119',
    '234234234234278',
    '818181911112111',
]

def part1(lines):
    """
    >>> part1(t1)
    357
    """
    total = 0
    for line in lines:
        hi = 0
        for a in range(0, len(line)):
            for b in range(a + 1, len(line)):
                j = int(line[a] + line[b])
                if j > hi:
                    hi = j
        total += hi
    return total

def joltage(line, num):
    """
    >>> joltage('987654321111111', 12)
    '987654321111'
    >>> joltage('811111111111119', 12)
    '811111111119'
    """
    if num == 0:
        return ''
    d = max(line[:len(line) - num + 1])
    i = line.find(d)
    return d + joltage(line[i + 1:], num - 1)

def part2(lines):
    """
    >>> part2(t1)
    3121910778619
    """
    return sum(int(joltage(line, 12)) for line in lines)

def main():
    puzzle_input = adventofcode.read_input(3)
    adventofcode.answer(1, 17100, part1(puzzle_input))
    adventofcode.answer(2, 170418192256861, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
