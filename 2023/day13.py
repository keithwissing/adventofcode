#!/usr/bin/env python3
from itertools import product

import adventofcode

t1 = [
    '#.##..##.',
    '..#.##.#.',
    '##......#',
    '##......#',
    '..#.##.#.',
    '..##..##.',
    '#.#.##.#.',
    '',
    '#...##..#',
    '#....#..#',
    '..##..###',
    '#####.##.',
    '#####.##.',
    '..##..###',
    '#....#..#',
]

def parse(lines):
    patterns = [[]]
    i = 0
    for line in lines:
        if not line:
            i += 1
            patterns.append([])
        else:
            patterns[i].append([c for c in line])
    return patterns

def find_vertical(pattern, ignore=0):
    for x in range(1, len(pattern[0])):
        if x == ignore:
            continue
        ok = True
        for i, line in enumerate(pattern):
            a, b = line[:x], line[x:]
            a = ''.join(a)
            b = ''.join(reversed(b))
            n = min(len(a), len(b))
            if not a[-n:] == b[-n:]:
                ok = False
        if ok:
            return x
    return 0

def find_horizontal(pattern, ignore=0):
    for y in range(1, len(pattern)):
        if y == ignore:
            continue
        ok = True
        for x in range(0, len(pattern[0])):
            line = ''.join([pattern[i][x] for i in range(len(pattern))])
            a, b = line[:y], line[y:]
            b = ''.join(reversed(b))
            n = min(len(a), len(b))
            if not a[-n:] == b[-n:]:
                ok = False
        if ok:
            return y
    return 0

def part1(lines):
    """
    >>> part1(t1)
    405
    """
    patterns = parse(lines)
    total = 0
    for p in patterns:
        total += find_vertical(p) + 100 * find_horizontal(p)
    return total

def part2(lines):
    """
    >>> part2(t1)
    400
    """
    patterns = parse(lines)
    total = 0
    for p in patterns:
        xi = find_vertical(p)
        yi = find_horizontal(p)
        for x, y in product(range(len(p[0])), range(len(p))):
            p[y][x] = '#' if p[y][x] == '.' else '.'
            nv = find_vertical(p, xi) + 100 * find_horizontal(p, yi)
            p[y][x] = '#' if p[y][x] == '.' else '.'
            if nv:
                total += nv
                break
    return total

def main():
    puzzle_input = adventofcode.read_input(13)
    adventofcode.answer(1, 37718, part1(puzzle_input))
    adventofcode.answer(2, 40995, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
