#!/usr/bin/env python3
from collections import defaultdict

import adventofcode

t1 = [
    '....#.....',
    '.........#',
    '..........',
    '..#.......',
    '.......#..',
    '..........',
    '.#..^.....',
    '........#.',
    '#.........',
    '......#...',
]

def add(pos, delta):
    return pos[0] + delta[0], pos[1] + delta[1]

def part1(lines):
    """
    >>> part1(t1)
    41
    """
    width, height = len(lines[0]), len(lines)
    grid = defaultdict(lambda: ' ', {(x, y): lines[y][x] for x in range(width) for y in range(height)})

    deltas = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    pos = next(k for k, v in grid.items() if v == '^')
    state = (pos, 0)

    while grid[state[0]] != ' ':
        pos, dir = state
        grid[pos] = 'X'
        test = add(pos, deltas[dir])
        while grid[test] == '#':
            dir = (dir + 1) % 4
            test = add(pos, deltas[dir])
        state = (test, dir)

    return sum(1 for k, v in grid.items() if v == 'X')

def test_for_loop(grid, state):
    grid = defaultdict(lambda: ' ', grid)
    deltas = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    history = set()
    while grid[state[0]] != ' ':
        if state in history:
            return True, grid
        history.add(state)

        pos, dir = state
        grid[pos] = 'X'
        test = add(pos, deltas[dir])
        while grid[test] == '#':
            dir = (dir + 1) % 4
            test = add(pos, deltas[dir])
        state = (test, dir)
    return False, grid

def part2(lines):
    """
    >>> part2(t1)
    6
    """
    width, height = len(lines[0]), len(lines)
    grid = defaultdict(lambda: ' ', {(x, y): lines[y][x] for x in range(width) for y in range(height)})

    pos = next(k for k, v in grid.items() if v == '^')
    state = (pos, 0)

    _, walked = test_for_loop(grid, state)

    total = 0

    for k, v in walked.items():
        if v != 'X' or grid[k] != '.':
            continue
        temp = grid[k]
        grid[k] = '#'
        loop, _ = test_for_loop(grid, state)
        grid[k] = temp

        if loop:
            total += 1

    return total

def main():
    puzzle_input = adventofcode.read_input(6)
    adventofcode.answer(1, 4789, part1(puzzle_input))
    adventofcode.answer(2, 1304, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
