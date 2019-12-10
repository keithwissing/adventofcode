#!/usr/bin/env python3

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
    traces = parse(lines)
    return part1(traces)

def test2(lines):
    """
    >>> test2(['R8,U5,L5,D3', 'U7,R6,D4,L4'])
    30
    >>> test2(['R75,D30,R83,U83,L12,D49,R71,U7,L72','U62,R66,U55,R34,D71,R55,D58,R83'])
    610
    >>> test2(['R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51','U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'])
    410
    >>> test2(['R20,U10,L10,D10,R10,U10', 'U5,R25'])
    50
    """
    traces = parse(lines)
    return part2(traces)

def dist(point1, point2=(0, 0)):
    """
    >>> dist((5, -5), (-5, 5))
    20
    """
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def part1(traces):
    return min([dist(pos) for pos in set(trace_positions(traces[0])).intersection(trace_positions(traces[1]))])

def trace_positions(trace):
    pos = (0, 0)
    for (direction, length) in trace:
        change = {'R' : (1, 0), 'L' : (-1, 0), 'U' : (0, 1), 'D': (0, -1)}[direction]
        for _ in range(length):
            #pos = tuple(sum(x) for x in zip(pos, change))
            #pos = tuple(map(sum, zip(pos, change)))
            pos = (pos[0] + change[0], pos[1] + change[1])
            yield pos

def dict_from_enum_first_wins(enum):
    grid = {}
    for cnt, pos in enum:
        if pos not in grid:
            grid[pos] = cnt
    return grid

def part2(traces):
    # Dictionary comprehension is last value wins, so this gets the wrong answer for some cases
    # grids = [{pos: cnt for cnt, pos in enumerate(trace_positions(trace), start=1)} for trace in traces]
    grids = [dict_from_enum_first_wins(enumerate(trace_positions(trace), start=1)) for trace in traces]
    return min([grids[0][pos] + grids[1][pos] for pos in set(grids[0].keys()).intersection(grids[1].keys())])

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
