#!/usr/bin/env python3

import adventofcode

t1 = [
'..##.......',
'#...#...#..',
'.#....#..#.',
'..#.#...#.#',
'.#...##..#.',
'..#.##.....',
'.#.#.#....#',
'.#........#',
'#.##...#...',
'#...##....#',
'.#..#...#.#',
]

def hits(lines, r, d):
    trees = 0
    down = 0
    pos = 0
    while down < len(lines):
        if lines[down][pos%len(lines[0])] == '#':
            trees += 1
        down += d
        pos += r
    return trees

def part1(lines):
    """
    >>> part1(t1)
    7
    """
    pos = 0
    trees = 0
    for line in lines:
        if line[pos%len(line)] == '#':
            trees += 1
        pos += 3
    return trees

def part2(lines):
    """
    >>> part2(t1)
    336
    """
    tot = 1
    tries = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for t in tries:
        tot *= hits(lines, t[0], t[1])
    return tot


def main():
    puzzle_input = adventofcode.read_input(3)
    adventofcode.answer(1, 145, part1(puzzle_input))
    adventofcode.answer(2, 3424528800, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
