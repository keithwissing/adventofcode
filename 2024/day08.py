#!/usr/bin/env python3
from itertools import permutations

import adventofcode

t1 = [
    '............',
    '........0...',
    '.....0......',
    '.......0....',
    '....0.......',
    '......A.....',
    '............',
    '............',
    '........A...',
    '.........A..',
    '............',
    '............',
]

def part1(lines):
    """
    >>> part1(t1)
    14
    """
    d = {(x, y): f for y, row in enumerate(lines) for x, f in enumerate(row) if f != '.'}
    frequencies = set(d.values())
    nodes = set()
    for f in frequencies:
        antennas = set(p for p, v in d.items() if v == f)
        for pair in permutations(antennas, 2):
            anode = (pair[0][0] + 2 * (pair[1][0] - pair[0][0]),
                     pair[0][1] + 2 * (pair[1][1] - pair[0][1]))
            nodes.add(anode)
    width, height = len(lines[0]), len(lines)
    return sum(1 for n in nodes if 0 <= n[0] < width and 0 <= n[1] < height)

def part2(lines):
    """
    >>> part2(t1)
    34
    """
    width, height = len(lines[0]), len(lines)
    d = {(x, y): f for y, row in enumerate(lines) for x, f in enumerate(row) if f != '.'}
    frequencies = set(d.values())
    nodes = set()
    for f in frequencies:
        antennas = set(p for p, v in d.items() if v == f)
        for pair in permutations(antennas, 2):
            pos = pair[0]
            delta = (pair[1][0] - pair[0][0], pair[1][1] - pair[0][1])
            while 0 <= pos[0] < width and 0 <= pos[1] < height:
                nodes.add(pos)
                pos = (pos[0] + delta[0], pos[1] + delta[1])

    return sum(1 for n in nodes if 0 <= n[0] < width and 0 <= n[1] < height)

def main():
    puzzle_input = adventofcode.read_input(8)
    adventofcode.answer(1, 379, part1(puzzle_input))
    adventofcode.answer(2, 1339, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
