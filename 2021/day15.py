#!/usr/bin/env python3

import heapq
import sys
import adventofcode

t1 = [
    '1163751742',
    '1381373672',
    '2136511328',
    '3694931569',
    '7463417111',
    '1319128137',
    '1359912421',
    '3125421639',
    '1293138521',
    '2311944581',
]

def adjacent(pos):
    yield (pos[0] - 1, pos[1])
    yield (pos[0], pos[1] - 1)
    yield (pos[0] + 1, pos[1])
    yield (pos[0], pos[1] + 1)

def valid(pos, size):
    return pos[0] >= 0 and pos[1] >= 0 and pos[0] < size and pos[1] < size

def find_risk(grid):
    risk = [[sys.maxsize for _ in range(len(grid[0]))] for _ in range(len(grid))]
    risk[0][0] = 0

    q = []
    heapq.heappush(q, (1, 0))

    while q:
        pos = heapq.heappop(q)
        if valid(pos, len(grid)):
            t = risk[pos[1]][pos[0]]
            for a in adjacent(pos):
                if valid(a, len(grid)):
                    if risk[pos[1]][pos[0]] > risk[a[1]][a[0]] + grid[pos[1]][pos[0]]:
                        risk[pos[1]][pos[0]] = risk[a[1]][a[0]] + grid[pos[1]][pos[0]]
            if risk[pos[1]][pos[0]] < t:
                for a in adjacent(pos):
                    heapq.heappush(q, a)
    return risk

def part1(lines):
    """
    >>> part1(t1)
    40
    """
    grid = [[int(lines[y][x]) for x in range(len(lines[0]))] for y in range(len(lines))]
    risk = find_risk(grid)
    return risk[len(risk) - 1][len(risk[0]) - 1]

def part2(lines):
    """
    >>> part2(t1)
    315
    """
    l = len(lines)
    grid = [[(int(lines[y % l][x % l]) + (y // l) + (x // l) - 1) % 9 + 1 for x in range(l * 5)] for y in range(l * 5)]
    risk = find_risk(grid)
    return risk[len(risk) - 1][len(risk[0]) - 1]

def main():
    puzzle_input = adventofcode.read_input(15)
    adventofcode.answer(1, 696, part1(puzzle_input))
    adventofcode.answer(2, 2952, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
