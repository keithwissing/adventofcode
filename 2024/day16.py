#!/usr/bin/env python3
from collections import defaultdict
from heapq import heappop, heappush

import adventofcode

t1 = [
    '###############',
    '#.......#....E#',
    '#.#.###.#.###.#',
    '#.....#.#...#.#',
    '#.###.#####.#.#',
    '#.#.#.......#.#',
    '#.#.#####.###.#',
    '#...........#.#',
    '###.#.#####.#.#',
    '#...#.....#.#.#',
    '#.#.#.###.#.#.#',
    '#.....#...#.#.#',
    '#.###.#.#.#.#.#',
    '#S..#.....#...#',
    '###############',
]

t2 = [
    '#################',
    '#...#...#...#..E#',
    '#.#.#.#.#.#.#.#.#',
    '#.#.#.#...#...#.#',
    '#.#.#.#.###.#.#.#',
    '#...#.#.#.....#.#',
    '#.#.#.#.#.#####.#',
    '#.#...#.#.#.....#',
    '#.#.#####.#.###.#',
    '#.#.#.......#...#',
    '#.#.###.#####.###',
    '#.#.#...#.....#.#',
    '#.#.#.#####.###.#',
    '#.#.#.........#.#',
    '#.#.#.#########.#',
    '#S#.............#',
    '#################',
]

def add_if_not_visited(q, visits, val):
    if val[1:3] not in visits:
        heappush(q, val)

def solve(lines):
    grid = defaultdict(lambda: '', {(x, y): v for y, l in enumerate(lines) for x, v in enumerate(l)})
    sp = next(k for k, v in grid.items() if v == 'S')
    start = (0, sp, 0, [sp])

    deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    q = [start]
    visits = set()
    paths = set()
    won = False
    last_score = 0
    while q:
        score, pos, r, path = heappop(q)
        if won and score > last_score:
            return score, len(paths)
        visits.add((pos, r))
        step = (pos[0] + deltas[r][0], pos[1] + deltas[r][1])
        if grid[step] == 'E':
            won = True
            paths.update(path)
            paths.add(step)
        if grid[step] != '#':
            add_if_not_visited(q, visits, (score + 1, step, r, path[:] + [step]))
        add_if_not_visited(q, visits, (score + 1000, pos, (r + 1) % 4, path))
        add_if_not_visited(q, visits, (score + 1000, pos, (r + 3) % 4, path))
        last_score = score

def part1(lines):
    """
    >>> part1(t1)
    7036

    >>> part1(t2)
    11048
    """
    a, _ = solve(lines)
    return a

def part2(lines):
    """
    >>> part2(t1)
    45

    >>> part2(t2)
    64
    """
    _, a = solve(lines)
    return a

def main():
    puzzle_input = adventofcode.read_input(16)
    adventofcode.answer(1, 160624, part1(puzzle_input))
    adventofcode.answer(2, 692, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
