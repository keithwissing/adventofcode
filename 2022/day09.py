#!/usr/bin/env python3

import adventofcode

t1 = [
    'R 4',
    'U 4',
    'L 3',
    'D 1',
    'R 4',
    'D 1',
    'L 5',
    'R 2',
]

t2 = [
    'R 5',
    'U 8',
    'L 8',
    'D 3',
    'R 17',
    'D 10',
    'L 25',
    'U 20',
]

def sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0

def pull(h, t):
    diff = tuple(x - y for x, y in zip(h, t))
    if max(abs(x) for x in diff) == 2:
        delta = tuple(sign(x) for x in diff)
        return tuple(x + y for x, y in zip(t, delta))
    return t

def move(h, d):
    delta = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}[d]
    return tuple(x + y for x, y in zip(h, delta))

def generalized(lines, rope_length):
    knots = [(0, 0)] * rope_length
    visited = {(0, 0)}
    for line in lines:
        d, r = line.split()
        for _ in range(int(r)):
            knots[0] = move(knots[0], d)
            for i in range(rope_length - 1):
                knots[i + 1] = pull(knots[i], knots[i + 1])
            visited.add(knots[rope_length - 1])
    return len(visited)

def part1(lines):
    """
    >>> part1(t1)
    13
    """
    return generalized(lines, 2)

def part2(lines):
    """
    >>> part2(t1)
    1
    >>> part2(t2)
    36
    """
    return generalized(lines, 10)

def main():
    puzzle_input = adventofcode.read_input(9)
    adventofcode.answer(1, 5695, part1(puzzle_input))
    adventofcode.answer(2, 2434, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
