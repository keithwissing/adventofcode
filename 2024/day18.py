#!/usr/bin/env python3
from collections import defaultdict
from heapq import heappop, heappush
from itertools import product

import adventofcode

t1 = [
    '5,4',
    '4,2',
    '4,5',
    '3,0',
    '2,1',
    '6,3',
    '2,4',
    '1,5',
    '0,6',
    '3,3',
    '2,6',
    '5,1',
    '1,2',
    '5,5',
    '2,5',
    '6,5',
    '1,4',
    '0,4',
    '6,4',
    '1,1',
    '6,1',
    '1,0',
    '0,5',
    '1,6',
    '2,0',
]

def display(grid, size):
    for y in range(size + 1):
        print(''.join(grid[(x, y)] for x in range(size + 1)))

def path_length(drops, size):
    grid = defaultdict(lambda: '#', {(x, y): '#' if (x, y) in drops else '.' for x, y in product(range(size + 1), range(size + 1))})
    dist = defaultdict(lambda: 1000000, {(0, 0): 0})

    deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    goal = (size, size)
    q = [(0, (0, 0))]
    while q:
        steps, pos = heappop(q)
        for d in deltas:
            test = (pos[0] + d[0], pos[1] + d[1])
            if grid[test] != '#' and dist[test] > (steps + 1):
                dist[test] = steps + 1
                heappush(q, (steps + 1, test))
    return dist[goal]

def part1(lines, size, n):
    """
    >>> part1(t1, 6, 12)
    22
    """
    points = [(int(a), int(b)) for a, b in [line.split(',') for line in lines]]
    return path_length(points[:n], size)

def part2(lines, size):
    """
    >>> part2(t1, 6)
    '6,1'
    """
    points = [(int(a), int(b)) for a, b in [line.split(',') for line in lines]]
    incr = len(points) // 4
    n = incr
    while incr:
        if path_length(points[:n], size) == 1000000:
            n -= incr
            if incr == 1:
                return f'{points[n][0]},{points[n][1]}'
            incr = max(1, incr // 4)
        n += incr

def main():
    puzzle_input = adventofcode.read_input(18)
    adventofcode.answer(1, 370, part1(puzzle_input, 70, 1024))
    adventofcode.answer(2, '65,6', part2(puzzle_input, 70))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
