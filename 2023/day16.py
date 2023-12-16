#!/usr/bin/env python3
from collections import defaultdict

import adventofcode

t1 = [
    '.|...\\....',
    '|.-.\\.....',
    '.....|-...',
    '........|.',
    '..........',
    '.........\\',
    '..../.\\\\..',
    '.-.-/..|..',
    '.|....-|.\\',
    '..//.|....',
]

def parse_grid(lines):
    width, height = len(lines[0]), len(lines)
    grid = defaultdict(lambda: '.', {(x, y): c for y, line in enumerate(lines) for x, c in enumerate(line)})
    return grid, height, width

def trace_beam(grid, w, h, energy, traced, pos, dir):
    while 0 <= pos[0] < w and 0 <= pos[1] < h:
        energy.add(pos)
        if (pos, dir) in traced:
            break
        traced.add((pos, dir))
        p = grid[pos]
        if p == '\\':
            dir = {'E': 'S', 'S': 'E', 'W': 'N', 'N': 'W'}[dir]
        if p == '/':
            dir = {'E': 'N', 'S': 'W', 'W': 'S', 'N': 'E'}[dir]
        if p == '-' and dir in 'NS':
            trace_beam(grid, w, h, energy, traced, pos, 'E')
            trace_beam(grid, w, h, energy, traced, pos, 'W')
            break
        if p == '|' and dir in 'EW':
            trace_beam(grid, w, h, energy, traced, pos, 'N')
            trace_beam(grid, w, h, energy, traced, pos, 'S')
            break
        d = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}[dir]
        pos = (pos[0] + d[0], pos[1] + d[1])

def get_energy(grid, w, h, pos, dir):
    energy = set()
    trace_beam(grid, w, h, energy, set(), pos, dir)
    return len(energy)

def part1(lines):
    """
    >>> part1(t1)
    46
    """
    grid, w, h = parse_grid(lines)
    return get_energy(grid, w, h, (0, 0), 'E')

def part2(lines):
    """
    >>> part2(t1)
    51
    """
    top = 0
    grid, w, h = parse_grid(lines)
    for x in range(w):
        top = max(top, get_energy(grid, w, h, (x, 0), 'S'))
        top = max(top, get_energy(grid, w, h, (x, h - 1), 'N'))
    for y in range(h):
        top = max(top, get_energy(grid, w, h, (0, y), 'E'))
        top = max(top, get_energy(grid, w, h, (w - 1, y), 'W'))
    return top

def main():
    puzzle_input = adventofcode.read_input(16)
    adventofcode.answer(1, 6514, part1(puzzle_input))
    adventofcode.answer(2, 8089, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
