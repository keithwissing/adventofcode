#!/usr/bin/env python3

import heapq
import adventofcode

t1 = [
    '2199943210',
    '3987894921',
    '9856789892',
    '8767896789',
    '9899965678',
]

def adjacent(pos):
    yield (pos[0] - 1, pos[1])
    yield (pos[0], pos[1] - 1)
    yield (pos[0] + 1, pos[1])
    yield (pos[0], pos[1] + 1)

def get(map, pos):
    if pos[0] < 0 or pos[1] < 0 or pos[0] >= len(map[0]) or pos[1] >= len(map):
        return 9
    return int(map[pos[1]][pos[0]])

def part1(map):
    """
    >>> part1(t1)
    15
    """
    val = 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            ma = min([get(map, p) for p in adjacent((x, y))])
            c = get(map, (x, y))
            if c < ma:
                val += c + 1
    return val

def basin_size(map, pos):
    q = [pos]
    size = 0
    while q:
        p = heapq.heappop(q)
        if get(map, p) < 9:
            map[p[1]][p[0]] = 9
            size += 1
            for a in adjacent(p):
                heapq.heappush(q, a)
    return size

def part2(map):
    """
    >>> part2(t1)
    1134
    """
    map = [[c for c in r] for r in map]
    lows = []
    for y in range(len(map)):
        for x in range(len(map[y])):
            ma = min([get(map, p) for p in adjacent((x, y))])
            c = get(map, (x, y))
            if c < ma:
                lows.append((x, y))
    q = []
    for p in lows:
        s = basin_size(map, p)
        heapq.heappush(q, s)
        if len(q) > 3:
            heapq.heappop(q)
    return q[0] * q[1] * q[2]

def main():
    puzzle_input = adventofcode.read_input(9)
    adventofcode.answer(1, 585, part1(puzzle_input))
    adventofcode.answer(2, 827904, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
