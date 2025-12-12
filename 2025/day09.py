#!/usr/bin/env python3
from collections import defaultdict

import adventofcode

t1 = [
    '7,1',
    '11,1',
    '11,7',
    '9,7',
    '9,5',
    '2,5',
    '2,3',
    '7,3',
]

def area(a, b):
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)

def part1(lines):
    """
    >>> part1(t1)
    50
    """
    tiles = (line.split(',') for line in lines)
    tiles = list(((int(x), int(y)) for x, y in tiles))
    l = 0
    for a in tiles:
        for b in tiles:
            t = area(a, b)
            if l < t:
                l = t
    return l

def sign(x):
    if x == 0:
        return 0
    return 1 if x > 0 else -1

def add(a, b):
    return a[0] + b[0], a[1] + b[1]

def adjacent(p):
    for d in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        yield add(p, d)

def fill(grid):
    w = max(x for x, _ in grid.keys()) + 2
    h = max(y for _, y in grid.keys()) + 2
    start = None
    for y in range(0, h):
        for x in range(0, w):
            if grid[(x, y)] == 'X':
                if grid[(x + 1, y)] == '.':
                    start = (x + 1, y)
                break
        if start is not None:
            break

    todo = {start}
    while todo:
        p = todo.pop()
        grid[p] = 'F'
        for t in adjacent(p):
            if grid[t] == '.':
                todo.add(t)

def rectangle(a, b):
    for y in range(min(a[1], b[1]), max(a[1], b[1]) + 1):
        for x in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
            yield x, y

def display(grid):
    w = max(x for x, _ in grid.keys()) + 1
    h = max(y for _, y in grid.keys()) + 1
    for y in range(0, h):
        print(''.join(grid[(x, y)] for x in range(0, w)))

def part2(lines):
    """
    # >>> part2(t1)
    24
    """
    tiles = (line.split(',') for line in lines)
    tiles = list(((int(x), int(y)) for x, y in tiles))
    xs = sorted(set(x for x, _ in tiles))
    ys = sorted(set(y for _, y in tiles))
    tis = list((xs.index(x) * 2, ys.index(y) * 2) for x, y in tiles)

    def to_real(a):
        return xs[a[0] // 2], ys[a[1] // 2]

    def real_area(a, b):
        return area(to_real(a), to_real(b))

    grid = defaultdict(lambda: '.', {p: '#' for p in tis})
    for i in range(len(tis)):
        a = tis[i]
        b = tis[(i + 1) % len(tis)]
        d = (sign(b[0] - a[0]), sign(b[1] - a[1]))
        p = add(a, d)
        while p != b:
            grid[p] = 'X'
            p = add(p, d)

    fill(grid)
    # display(grid)

    l = 0
    for ai, a in enumerate(tis):
        for b in tis[ai + 1:]:
            ra = real_area(a, b)
            if ra > l:
                if all(grid[p] != '.' for p in rectangle(a, b)):
                    l = ra

    return l

def main():
    puzzle_input = adventofcode.read_input(9)
    adventofcode.answer(1, 4776100539, part1(puzzle_input))
    adventofcode.answer(2, 1476550548, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
