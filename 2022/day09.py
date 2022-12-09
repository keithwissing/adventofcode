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

def pull(h, t):
    diff = tuple(x - y for x, y in zip(h, t))
    moves = {(0, 2): (0, 1),
             (1, 2): (1, 1),
             (2, 2): (1, 1),
             (2, 1): (1, 1),
             (2, 0): (1, 0),
             (2, -1): (1, -1),
             (2, -2): (1, -1),
             (1, -2): (1, -1),
             (0, -2): (0, -1),
             (-1, -2): (-1, -1),
             (-2, -2): (-1, -1),
             (-2, -1): (-1, -1),
             (-2, 0): (-1, 0),
             (-2, 1): (-1, 1),
             (-2, 2): (-1, 1),
             (-1, 2): (-1, 1)}
    return tuple(x + y for x, y in zip(t, moves[diff])) if diff in moves else t

def move(h, d):
    delta = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}[d]
    return tuple(x + y for x, y in zip(h, delta))

def step(h, t, d):
    nh = move(h, d)
    return nh, pull(nh, t)

def part1(lines):
    """
    >>> part1(t1)
    13
    """
    h = t = (0, 0)
    visited = {t}
    for line in lines:
        d, r = line.split()
        for _ in range(int(r)):
            h, t = step(h, t, d)
            visited.add(t)
            # print(h, t)
    # print(visited)
    return len(visited)

def part2(lines):
    """
    >>> part2(t1)
    1
    >>> part2(t2)
    36
    """
    knots = [(0, 0)] * 10
    visited = {(0, 0)}
    for line in lines:
        d, r = line.split()
        for _ in range(int(r)):
            knots[0] = move(knots[0], d)
            for i in range(9):
                knots[i + 1] = pull(knots[i], knots[i + 1])
            visited.add(knots[9])
    return len(visited)

def main():
    puzzle_input = adventofcode.read_input(9)
    adventofcode.answer(1, 5695, part1(puzzle_input))
    adventofcode.answer(2, 2434, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
