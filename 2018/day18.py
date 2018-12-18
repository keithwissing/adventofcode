#!/usr/bin/env python

import adventofcode

test_data = [
    '.#.#...|#.',
    '.....#|##|',
    '.|..|...#.',
    '..|#.....#',
    '#.#|||#|#|',
    '...#.||...',
    '.|....|...',
    '||...#|.#|',
    '|.||||..|.',
    '...#.|..|.']

def part1(puzzle_input, size):
    """
    >>> part1(test_data, 10)
    1147
    """
    state = Board(puzzle_input, size)
    for _ in range(10):
        state.iterate()
    trees, yards = state.count_all()
    return trees * yards

class Board(object):
    def __init__(self, puzzle_input, size):
        self.size = size
        self.board = [row[:] for row in puzzle_input]

    def display(self):
        for row in self.board:
            print ''.join(row)

    def get(self, x, y):
        if x >= 0 and x < self.size and y >= 0 and y < self.size:
            return self.board[y][x]
        return ' '

    def set(self, x, y, v):
        self.board[y][x] = v

    def adjacent_counts(self, x, y):
        trees, yards = 0, 0
        for px in range(x-1, x+2):
            for py in range(y-1, y+2):
                if px != x or py != y:
                    cell = self.get(px, py)
                    if cell == '|':
                        trees += 1
                    if cell == '#':
                        yards += 1
        return trees, yards

    def count_all(self):
        trees = sum([sum([1 for cell in row if cell == '|']) for row in self.board])
        yards = sum([sum([1 for cell in row if cell == '#']) for row in self.board])
        return trees, yards

    def iterate(self):
        mut = [[' '] * self.size for _ in range(self.size)]
        for py in range(self.size):
            for px in range(self.size):
                trees, yards = self.adjacent_counts(px, py)
                current = self.get(px, py)
                if current == '.':
                    mut[py][px] = '|' if trees >= 3 else '.'
                if current == '|':
                    mut[py][px] = '#' if yards >= 3 else '|'
                if current == '#':
                    mut[py][px] = '#' if trees >= 1 and yards >= 1 else '.'
        self.board = mut

    def unique_id(self):
        return ''.join([''.join(row) for row in self.board])

def part2(puzzle_input, size, goal):
    state = Board(puzzle_input, size)
    time = 0
    seen = {}
    while time < goal:
        state.iterate()
        time += 1
        key = state.unique_id()
        if seen.has_key(key):
            dif = time - seen[key]
            need = goal - time
            skip = need / dif
            time += skip * dif
            seen = {}
        else:
            seen[key] = time
    trees, yards = state.count_all()
    return trees * yards

def main():
    puzzle_input = adventofcode.read_input(18)
    adventofcode.answer(1, 645946, part1(puzzle_input, 50))
    adventofcode.answer(2, 227688, part2(puzzle_input, 50, 1000000000))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
