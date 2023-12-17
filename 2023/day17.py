#!/usr/bin/env python3
from collections import defaultdict
from heapq import heappush, heappop
from sys import maxsize

import adventofcode

t1 = [
    '2413432311323',
    '3215453535623',
    '3255245654254',
    '3446585845452',
    '4546657867536',
    '1438598798454',
    '4457876987766',
    '3637877979653',
    '4654967986887',
    '4564679986453',
    '1224686865563',
    '2546548887735',
    '4322674655533',
]

t2 = [
    '111111111111',
    '999999999991',
    '999999999991',
    '999999999991',
    '999999999991',
]

def parse_grid(lines):
    width, height = len(lines[0]), len(lines)
    grid = defaultdict(lambda: maxsize, {(x, y): int(c) for y, line in enumerate(lines) for x, c in enumerate(line)})
    return grid, width, height

# 0 = N, 1 = E, 2 = S, 3 = W
# def adjacent(pos, _a, _b):
#     for d in [(0, -1, 0), (1, 0, 1), (0, 1, 2), (-1, 0, 3)]:
#         if (pos[2] + 2) % 4 != d[2] and (pos[3] != 2 or pos[2] != d[2]):
#             yield (pos[0] + d[0], pos[1] + d[1], d[2], pos[3] + 1 if pos[2] == d[2] else 0)
#
# def adjacent2(pos, _a, _b):
#     for d in [(0, -1, 0), (1, 0, 1), (0, 1, 2), (-1, 0, 3)]:
#         if pos[3] < 3:
#             if pos[2] == d[2]:
#                 yield (pos[0] + d[0], pos[1] + d[1], pos[2], pos[3] + 1)
#         else:
#             if (pos[2] + 2) % 4 != d[2] and (pos[3] < 9 or pos[2] != d[2]):
#                 yield (pos[0] + d[0], pos[1] + d[1], d[2], pos[3] + 1 if pos[2] == d[2] else 0)

def adjacent_v(pos, min_move, max_move):
    for d in [(0, -1, 0), (1, 0, 1), (0, 1, 2), (-1, 0, 3)]:
        if pos[3] < min_move - 1:
            if pos[2] == d[2]:
                yield (pos[0] + d[0], pos[1] + d[1], pos[2], pos[3] + 1)
        else:
            if (pos[2] + 2) % 4 != d[2] and (pos[3] < max_move - 1 or pos[2] != d[2]):
                yield (pos[0] + d[0], pos[1] + d[1], d[2], pos[3] + 1 if pos[2] == d[2] else 0)

def in_grid(pos, w, h):
    return 0 <= pos[0] < w and 0 <= pos[1] < h

def solve_with(lines, adj, min_move, max_move):
    grid, w, h = parse_grid(lines)
    distances = {(0, 0, 1, 0): 0, (0, 0, 2, 0): 0}
    look = []
    heappush(look, (0, 0, 1, 0))
    heappush(look, (0, 0, 2, 0))
    while look:
        pos = heappop(look)
        for n in adj(pos, min_move, max_move):
            if in_grid(n, w, h):
                if n not in distances or distances[n] > distances[pos] + grid[(n[0], n[1])]:
                    distances[n] = distances[pos] + grid[(n[0], n[1])]
                    heappush(look, n)
    v = maxsize
    for a in range(4):
        for b in range(min_move - 1, max_move):
            k = (w - 1, h - 1, a, b)
            if k in distances and v > distances[k]:
                v = distances[k]
    return v

def part1(lines):
    """
    >>> part1(t1)
    102
    """
    return solve_with(lines, adjacent_v, 1, 3)

def part2(lines):
    """
    >>> part2(t1)
    94
    >>> part2(t2)
    71
    """
    return solve_with(lines, adjacent_v, 4, 10)

def main():
    puzzle_input = adventofcode.read_input(17)
    adventofcode.answer(1, 1260, part1(puzzle_input))
    adventofcode.answer(2, 1416, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
