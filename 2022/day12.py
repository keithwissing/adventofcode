#!/usr/bin/env python3
import heapq

import adventofcode

t1 = [
    'Sabqponm',
    'abcryxxl',
    'accszExk',
    'acctuvwj',
    'abdefghi',
]

def add(a, b):
    return tuple(x + y for x, y in zip(a, b))

class Grid:
    def __init__(self, lines):
        self.lines = [[v for v in line] for line in lines]
        self.height = len(lines)
        self.width = len(lines[0])

    def valid_pos(self, pos):
        return 0 <= pos[0] < self.width and 0 <= pos[1] < self.height

    def get(self, pos):
        return self.lines[pos[1]][pos[0]] if self.valid_pos(pos) else '.'

    def set(self, pos, val):
        self.lines[pos[1]][pos[0]] = val

    def find(self, val):
        for y in range(self.height):
            try:
                x = self.lines[y].index(val)
                yield x, y
            except ValueError:
                pass

    def print(self):
        for y in range(self.height):
            print(self.lines[y])

    def adjacent(self, pos):
        for d in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            n = add(pos, d)
            if self.valid_pos(n):
                yield n

def steps(grid, pos):
    cur = ord(grid.get(pos))
    for n in grid.adjacent(pos):
        if ord(grid.get(n)) <= cur + 1:
            yield n

def setup(lines):
    grid = Grid(lines)
    distance = Grid([[10000 for _ in range(grid.width)] for _ in range(grid.height)])
    start = list(grid.find('S'))[0]
    end = list(grid.find('E'))[0]
    grid.set(start, 'a')
    grid.set(end, 'z')
    return grid, distance, start, end

def fill_distances(grid, distance, heap):
    while heap:
        sc, pos = heapq.heappop(heap)
        if sc < distance.get(pos):
            distance.set(pos, sc)
            for n in steps(grid, pos):
                heapq.heappush(heap, (sc + 1, n))

def part1(lines):
    """
    >>> part1(t1)
    31
    """
    grid, distance, start, end = setup(lines)
    heap = [(0, start)]
    fill_distances(grid, distance, heap)
    return distance.get(end)

def part2(lines):
    """
    >>> part2(t1)
    29
    """
    grid, distance, _, end = setup(lines)
    heap = [(0, a) for a in grid.find('a')]
    heapq.heapify(heap)
    fill_distances(grid, distance, heap)
    return distance.get(end)

def main():
    puzzle_input = adventofcode.read_input(12)
    adventofcode.answer(1, 517, part1(puzzle_input))
    adventofcode.answer(2, 512, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
