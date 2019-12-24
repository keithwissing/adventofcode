#!/usr/bin/env python3

from collections import defaultdict
from itertools import product
import adventofcode

def adjacent(pos):
    # clockwise, starting up, negative y is up
    for d in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        yield (pos[0]+d[0], pos[1]+d[1])

class Grid:
    def __init__(self, lines):
        self.grid = [list(l) for l in lines]
        self.width = len(self.grid[0])
        self.height = len(self.grid)

    def get(self, pos):
        if 0 <= pos[0] < self.width and 0 <= pos[1] < self.height:
            return self.grid[pos[1]][pos[0]]
        return '.'

    def evolve(self):
        ng = []
        for _ in range(self.height):
            ng.append([' '] * self.width)
        for x, y in product(range(self.width), range(self.height)):
            me = self.get((x, y))
            nei = sum(1 if self.get(p) == '#' else 0 for p in adjacent((x, y)))
            if me == '#' and nei != 1:
                ng[y][x] = '.'
            elif me == '.' and nei in [1, 2]:
                ng[y][x] = '#'
            else:
                ng[y][x] = me
        self.grid = ng

    def asstr(self):
        return ''.join(i for s in self.grid for i in s)

    def biodiversity(self):
        a = [item for sublist in self.grid for item in sublist]
        a = ['1' if x == '#' else '0' for x in a]
        a = ''.join(a)
        return int(a[::-1], 2)

    def __repr__(self):
        return '\n'.join([''.join(l) for l in self.grid])

testdata1 = [
    '....#',
    '#..#.',
    '#..##',
    '..#..',
    '#....',
]

def part1(lines):
    """
    >>> part1(testdata1)
    2129920
    """
    g = Grid(lines)
    seen = set([g.asstr()])
    while True:
        g.evolve()
        s = g.asstr()
        if s in seen:
            return g.biodiversity()
        seen.add(s)

def fold_adjacent(pos):
    x, y, l = pos
    for p in adjacent((x, y)):
        if p[0] == -1:
            yield (1, 2, l-1)
        elif p[0] == 5:
            yield (3, 2, l-1)
        elif p[1] == -1:
            yield (2, 1, l-1)
        elif p[1] == 5:
            yield (2, 3, l-1)
        elif p == (2, 2):
            if x == 1:
                for s in range(5):
                    yield (0, s, l+1)
            elif x == 3:
                for s in range(5):
                    yield (4, s, l+1)
            elif y == 1:
                for s in range(5):
                    yield (s, 0, l+1)
            elif y == 3:
                for s in range(5):
                    yield (s, 4, l+1)
        else:
            yield (p[0], p[1], l)

class FoldedSpace:
    def __init__(self, lines):
        self.grid = defaultdict(lambda: '.')
        self.width = len(lines[0])
        self.height = len(lines)
        for x, y in product(range(self.width), range(self.height)):
            if lines[y][x] == '#':
                self.grid[(x, y, 0)] = '#'

    def evolve(self, hint):
        ng = defaultdict(lambda: '.')
        minl, maxl = -hint//2, hint//2
        for x, y, l in product(range(5), range(5), range(minl, maxl+1)):
            if x == 2 and y == 2:
                continue
            k = (x, y, l)
            me = self.grid[k]
            nei = sum(1 if self.grid[p] == '#' else 0 for p in fold_adjacent(k))
            if me == '#' and nei != 1:
                ng[k] = '.'
            elif me == '.' and nei in [1, 2]:
                ng[k] = '#'
            else:
                ng[k] = me
        self.grid.update(ng)

    def count_bugs(self):
        return sum(1 if x == '#' else 0 for x in self.grid.values())

    def display(self, l):
        for y in range(5):
            print(''.join(self.grid[(x, y, l)] for x in range(5)))

def part2(lines, minutes):
    g = FoldedSpace(lines)
    for _ in range(minutes):
        g.evolve(minutes)
    return g.count_bugs()

def main():
    puzzle_input = adventofcode.read_input(24)
    adventofcode.answer(1, 28615131, part1(puzzle_input))
    adventofcode.answer(2, 1926, part2(puzzle_input, 200))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
