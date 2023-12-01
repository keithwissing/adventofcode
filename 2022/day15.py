#!/usr/bin/env python3

import adventofcode

t1 = [
    'Sensor at x=2, y=18: closest beacon is at x=-2, y=15',
    'Sensor at x=9, y=16: closest beacon is at x=10, y=16',
    'Sensor at x=13, y=2: closest beacon is at x=15, y=3',
    'Sensor at x=12, y=14: closest beacon is at x=10, y=16',
    'Sensor at x=10, y=20: closest beacon is at x=10, y=16',
    'Sensor at x=14, y=17: closest beacon is at x=10, y=16',
    'Sensor at x=8, y=7: closest beacon is at x=2, y=10',
    'Sensor at x=2, y=0: closest beacon is at x=2, y=10',
    'Sensor at x=0, y=11: closest beacon is at x=2, y=10',
    'Sensor at x=20, y=14: closest beacon is at x=25, y=17',
    'Sensor at x=17, y=20: closest beacon is at x=21, y=22',
    'Sensor at x=16, y=7: closest beacon is at x=15, y=3',
    'Sensor at x=14, y=3: closest beacon is at x=15, y=3',
    'Sensor at x=20, y=1: closest beacon is at x=15, y=3',
]

def parse(lines):
    return [[int(w.split('=')[1].replace(',', '').replace(':', '')) for w in line.split() if '=' in w] for line in lines]

def mdistance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def part1(lines, row):
    """
    >>> part1(t1, 10)
    26
    """
    exclusions = set()
    sensors = parse(lines)
    for line in sensors:
        s, b = (line[0], line[1]), (line[2], line[3])
        t = (s[0], row)
        step = 0
        while (mdistance(t, s) + step) <= mdistance(b, s):
            exclusions.add(t[0] + step)
            exclusions.add(t[0] - step)
            step += 1
    for line in sensors:
        if line[3] == row and line[2] in exclusions:
            exclusions.remove(line[2])
    return len(exclusions)

def is_outside(pos, sensors):
    for s in sensors:
        if mdistance(pos, s[0]) <= s[2]:
            return False
    return True

def edges(pos, d):
    # Yes, this can yield duplicates. I don't really care.
    x, y = pos
    for i in range(d + 1):
        yield x + i, y + d - i + 1
        yield x + i, y - d + i - 1
        yield x - i, y + d - i + 1
        yield x - i, y - d + i - 1

def is_on_board(pos, limit):
    return 0 <= pos[0] < limit and 0 <= pos[1] < limit

def part2(lines):
    """
    Note that this is not a complete solution, but it worked for my input
    # >>> part2(t1)
    """
    limit = 4000000

    sensors = parse(lines)
    sensors = [((s[0], s[1]), (s[2], s[3])) for s in sensors]
    sensors = [(s[0], s[1], mdistance(s[0], s[1])) for s in sensors]

    for s in sensors:
        for pos in edges(s[0], s[2]):
            if is_on_board(pos, limit) and is_outside(pos, sensors):
                return pos[0] * limit + pos[1]
    return False

def main():
    puzzle_input = adventofcode.read_input(15)
    adventofcode.answer(1, 5716881, part1(puzzle_input, 2000000))
    adventofcode.answer(2, 10852583132904, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
