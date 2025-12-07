#!/usr/bin/env python3

import adventofcode

t1 = [
    '3-5',
    '10-14',
    '16-20',
    '12-18',
    '',
    '1',
    '5',
    '8',
    '11',
    '17',
    '32',
]

def parse(lines):
    split = lines.index('')
    ranges = lines[:split]
    ids = lines[split + 1:]
    ranges = [(int(a), int(b)) for a, b in (tuple(x.split('-')) for x in ranges)]
    ids = [int(a) for a in ids]
    return ranges, ids

def part1(lines):
    """
    >>> part1(t1)
    3
    """
    ranges, ids = parse(lines)
    total = 0
    for i in ids:
        if any(a <= i <= b for a, b in ranges):
            total += 1
    return total

def merge(ranges: set):
    for a in ranges:
        for b in ranges:
            if a == b:
                continue
            if a[0] <= b[0] <= a[1] <= b[1]:
                ranges.remove(a)
                ranges.remove(b)
                ranges.add((a[0], b[1]))
                return ranges
            if a[0] <= b[0] <= b[1] <= a[1]:
                ranges.remove(b)
                return ranges
    return ranges

def part2(lines):
    """
    >>> part2(t1)
    14
    """
    ranges, _ = parse(lines)
    ranges = set(ranges)
    ll = 0
    while ll != len(ranges):
        ll = len(ranges)
        ranges = merge(ranges)

    return sum(r[1] - r[0] + 1 for r in ranges)

def main():
    puzzle_input = adventofcode.read_input(5)
    adventofcode.answer(1, 567, part1(puzzle_input))
    adventofcode.answer(2, 354149806372909, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
