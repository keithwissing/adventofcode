#!/usr/bin/env python3

import adventofcode

t1 = [
    'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
    'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
    'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
    'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
    'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
    'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11',
]

def part1(lines):
    """
    >>> part1(t1)
    13
    """
    points = 0
    for line in lines:
        card, numbers = line.split(':')
        a = numbers.split('|')
        b = [set(int(x) for x in y.split()) for y in a]
        c = b[0].intersection(b[1])
        # print(c)
        if c:
            points += 1 << (len(c) - 1)
    return points

def part2(lines):
    """
    >>> part2(t1)
    30
    """
    counts = [1] * len(lines)
    for i, line in enumerate(lines):
        card, numbers = line.split(':')
        a = numbers.split('|')
        b = [set(int(x) for x in y.split()) for y in a]
        c = b[0].intersection(b[1])
        if c:
            for x in range(i + 1, i + 1 + len(c)):
                counts[x] += counts[i]
    return sum(counts)

def main():
    puzzle_input = adventofcode.read_input(4)
    adventofcode.answer(1, 21158, part1(puzzle_input))
    adventofcode.answer(2, 6050769, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
