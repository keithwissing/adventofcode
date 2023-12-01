#!/usr/bin/env python3
from itertools import groupby

import adventofcode

t1 = [
    '        ...#',
    '        .#..',
    '        #...',
    '        ....',
    '...#.......#',
    '........#...',
    '..#....#....',
    '..........#.',
    '        ...#....',
    '        .....#..',
    '        .#......',
    '        ......#.',
    '',
    '10R5L5R10L4R5L5',
]

def add(a, b):
    return tuple(x + y for x, y in zip(a, b))

class Map:
    def __init__(self, lines):
        self.data = {}
        for y, line in enumerate(lines):
            self.data.update({(x, y): v for x, v in enumerate(line) if v != ' '})
        self.width = max(x for x, _ in self.data.keys()) + 1
        self.height = max(y for _, y in self.data.keys()) + 1

    def move(self, pos, direction):
        delta = {'<': (-1, 0), '^': (0, -1), '>': (1, 0), 'v': (0, 1)}[direction]
        np = pos
        while True:
            np = add(np, delta)
            np = ((np[0] + self.width) % self.width, (np[1] + self.height) % self.height)
            if self.data.get(np) == '.':
                return np
            if self.data.get(np) == '#':
                return pos

def split_on_blank_lines(lines):
    yield from [list(sub) for ele, sub in groupby(lines, key=bool) if ele]

def parse(lines):
    md, path = split_on_blank_lines(lines)
    jungle = Map(md)
    return jungle, path[0]

def find_start(jungle):
    return next((x, 0) for x in range(jungle.width) if (x, 0) in jungle.data and jungle.data[(x, 0)] == '.')

def part1(lines):
    """
    >>> part1(t1)
    6032
    """
    faces = ['>', 'v', '<', '^']
    jungle, path = parse(lines)
    state = (find_start(jungle), '>')
    path = list(''.join(sub) for ele, sub in groupby(path, key=lambda x: x.isdigit()))
    for step in path:
        if step.isdigit():
            distance = int(step)
            for _ in range(distance):
                state = (jungle.move(state[0], state[1]), state[1])
        else:
            nf = faces[(faces.index(state[1]) + {'R': 1, 'L': 3}[step]) % 4]
            state = (state[0], nf)
    return 1000 * (state[0][1] + 1) + 4 * (state[0][0] + 1) + faces.index(state[1])

def part2(lines):
    """
    # >>> part2(t1)
    """

def main():
    puzzle_input = adventofcode.read_input(22)
    adventofcode.answer(1, 197160, part1(puzzle_input))
    # adventofcode.answer(2, 0, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
