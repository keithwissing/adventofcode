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
    (-1, 0): ('-LF', '-J7iS'),
    (1, 0): ('-J7', '-LFS'),
    (0, -1): ('|7F', '|LJS'),
    (0, 1): ('|LJ', '|7FS')
}

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
    checks = set([start])
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
    if (x, y) in pipe:
        return False

    hor = [
        [pipe.get((i, y), '.') for i in range(0, x)],
        [pipe.get((i, y), '.') for i in range(x + 1, w)]
    ]

    vert = [
        [pipe.get((x, i), '.') for i in range(0, y)],
        [pipe.get((x, i), '.') for i in range(y + 1, h)],
    ]

    for hh in hor:
        cnt = Counter(hh)
        test = cnt['|']
        test += min(cnt['7'], cnt['L'])
        test += min(cnt['J'], cnt['F'])
        if test % 2 == 0:
            return False

    for vv in vert:
        cnt = Counter(vv)
        test = cnt['-']
        test += min(cnt['7'], cnt['L'])
        test += min(cnt['J'], cnt['F'])
        if test % 2 == 0:
            return False

    return True

def calc_s(p):
    if p[0] in '-FL' and p[1] in '|F7':
        return 'J'
    if p[0] in '-FL' and p[2] in '-7J':
        return '-'
    if p[0] in '-FL' and p[3] in '|JL':
        return '7'
    if p[1] in '|F7' and p[2] in '-7J':
        return 'L'
    if p[1] in '|F7' and p[3] in '|JL':
        return '|'
    if p[2] in '-7J' and p[3] in '|JL':
        return 'F'
    raise Exception(p)

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
    pipe = defaultdict(lambda: '.')
    for p in distances.keys():
        pipe[p] = grid[p]
        if pipe[p] == 'S':
            pipe[p] = calc_s([grid.get(add(p, d), '.') for d in [(-1, 0), (0, -1), (1, 0), (0, 1)]])
    sum = 0
    for x, y in product(range(0, w), range(0, h)):
        if is_inside(pipe, w, h, x, y):
            sum += 1
    return sum

def main():
    puzzle_input = adventofcode.read_input(10)
    adventofcode.answer(1, 6890, part1(puzzle_input))
    adventofcode.answer(2, 453, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
