#!/usr/bin/env python3
from collections import defaultdict, Counter
from itertools import product
from sys import maxsize

import adventofcode

t1 = [
    '-L|F7',
    '7S-7|',
    'L|7||',
    '-L-J|',
    'L|-JF',
]

t2 = [
    '7-F7-',
    '.FJ|7',
    'SJLL7',
    '|F--J',
    'LJ.LJ',
]

t3 = [
    '..........',
    '.S------7.',
    '.|F----7|.',
    '.||OOOO||.',
    '.||OOOO||.',
    '.|L-7F-J|.',
    '.|II||II|.',
    '.L--JL--J.',
    '..........',
]

t4 = [
    '.F----7F7F7F7F-7....',
    '.|F--7||||||||FJ....',
    '.||.FJ||||||||L7....',
    'FJL7L7LJLJ||LJ.L-7..',
    'L--J.L7...LJS7F-7L7.',
    '....F-J..F7FJ|L7L7L7',
    '....L7.F7||L7|.L7L7|',
    '.....|FJLJ|FJ|F7|.LJ',
    '....FJL-7.||.||||...',
    '....L---J.LJ.LJLJ...',
]

t5 = [
    'FF7FSF7F7F7F7F7F---7',
    'L|LJ||||||||||||F--J',
    'FL-7LJLJ||||||LJL-77',
    'F--JF--7||LJLJ7F7FJ-',
    'L---JF-JLJ.||-FJLJJ7',
    '|F|F-JF---7F7-L7L|7|',
    '|FFJF7L7F-JF7|JL---7',
    '7-L-JL7||F7|L7F-7F7|',
    'L.L7LFJ|||||FJL7||LJ',
    'L7JLJL-JLJLJL--JLJ.L',
]

def add(a, b):
    return tuple(x + y for x, y in zip(a, b))

con = {
    (-1, 0): ('-LF', '-J7iS'),  # west
    (0, -1): ('|7F', '|LJS'),  # north
    (1, 0): ('-J7', '-LFS'),  # east
    (0, 1): ('|LJ', '|7FS'),  # south
}

wnes = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def parse_grid(lines):
    grid = defaultdict(lambda: '.')
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid[(x, y)] = c
            if c == 'S':
                start = (x, y)
    return grid, start, len(lines[0]), len(lines)

def find_pipe(grid, start):
    pipe = {start: 0}
    checks = {start}
    while checks:
        pos = checks.pop()
        for d in con.keys():
            np = add(pos, d)
            if grid[np] in con[d][0] and grid[pos] in con[d][1]:
                if pipe[pos] + 1 < pipe.get(np, maxsize):
                    pipe[np] = pipe[pos] + 1
                    checks.add(np)
    return pipe

def part1(lines):
    """
    >>> part1(t1)
    4
    >>> part1(t2)
    8
    """
    grid, start, _, _ = parse_grid(lines)
    pipe = find_pipe(grid, start)
    return max(pipe.values())

def is_inside(pipe, w, h, x, y):
    # a tile is inside if there is an odd number of pipe crossings in every direction

    if (x, y) in pipe:
        return False

    hor = [
        ('|', [pipe.get((i, y), '.') for i in range(0, x)]),
        ('|', [pipe.get((i, y), '.') for i in range(x + 1, w)]),
        ('-', [pipe.get((x, i), '.') for i in range(0, y)]),
        ('-', [pipe.get((x, i), '.') for i in range(y + 1, h)]),
    ]

    with_counts = [(x[0], Counter(x[1])) for x in hor]
    tests = [c[x] + min(c['7'], c['L']) + min(c['J'], c['F']) for x, c in with_counts]
    return not any(t % 2 == 0 for t in tests)

def calc_s(p):
    connections = [x[0] in con[x[1]][0] for x in zip(p, wnes)]
    aaa = ''.join([str(i) for i, v in enumerate(connections) if v])
    return {'01': 'J', '02': '-', '03': '7', '12': 'L', '13': '|', '23': 'F'}[aaa]

def part2(lines):
    """
    >>> part2(t3)
    4
    >>> part2(t4)
    8
    >>> part2(t5)
    10
    """
    grid, start, w, h = parse_grid(lines)
    distances = find_pipe(grid, start)
    pipe = defaultdict(lambda: '.', {
        p: grid[p] if grid[p] != 'S' else calc_s([grid.get(add(p, d), '.') for d in wnes])
        for p in distances.keys()
    })
    return sum(is_inside(pipe, w, h, x, y) for x, y in product(range(0, w), range(0, h)))

def main():
    puzzle_input = adventofcode.read_input(10)
    adventofcode.answer(1, 6890, part1(puzzle_input))
    adventofcode.answer(2, 453, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
