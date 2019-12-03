#!/usr/bin/env python3

from collections import defaultdict
import adventofcode

def test1(lines):
    """
    >>> test1(['R8,U5,L5,D3', 'U7,R6,D4,L4'])
    6
    >>> test1(['R75,D30,R83,U83,L12,D49,R71,U7,L72','U62,R66,U55,R34,D71,R55,D58,R83'])
    159
    >>> test1(['R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51','U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'])
    135
    """
    tr = parse(lines)
    return part1(tr)

def test2(lines):
    """
    >>> test2(['R8,U5,L5,D3', 'U7,R6,D4,L4'])
    30
    >>> test2(['R75,D30,R83,U83,L12,D49,R71,U7,L72','U62,R66,U55,R34,D71,R55,D58,R83'])
    610
    >>> test2(['R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51','U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'])
    410
    """
    tr = parse(lines)
    return part2(tr)

def dist(a, b):
    """
    >>> dist((5, -5), (-5, 5))
    20
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def part1(traces):
    grid = defaultdict(lambda: '.')
    for n, trace in enumerate(traces):
        for pos in trace_positions(trace):
            if grid[pos] == '.':
                grid[pos] = n
            elif grid[pos] != n:
                grid[pos] = 'X'
    md = 50000000
    for i in grid.items():
        if i[1] == 'X':
            nd = dist((0, 0), i[0])
            if nd < md:
                md = nd
    return md

def trace_positions(trace):
    pos = (0, 0)
    for (d, l) in trace:
        change = {'R' : (1, 0), 'L' : (-1, 0), 'U' : (0, 1), 'D': (0, -1)}[d]
        for _ in range(l):
            pos = tuple(sum(x) for x in zip(pos, change))
            yield pos

def part2(traces):
    grid = defaultdict(lambda: (0, 0))
    for n, trace in enumerate(traces):
        for cnt, pos in enumerate(trace_positions(trace)):
            ov = grid[pos]
            if ov[n] == 0 and n == 0:
                grid[pos] = (cnt + 1, 0)
            if ov[n] == 0 and n == 1:
                grid[pos] = (ov[0], cnt + 1)
    md = 50000000
    for i in grid.values():
        if i[0] != 0 and i[1] != 0:
            nd = i[0] + i[1]
            if nd < md:
                md = nd
    return md

def parse(lines):
    return [[(x[0], int(x[1:])) for x in l.split(',')] for l in lines]

def main():
    puzzle_input = adventofcode.read_input(3)
    traces = parse(puzzle_input)
    adventofcode.answer(1, 768, part1(traces))
    adventofcode.answer(2, 8684, part2(traces))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
