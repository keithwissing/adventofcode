#!/usr/bin/env python

import itertools
import adventofcode

test_1 = """
 0,0,0,0
 3,0,0,0
 0,3,0,0
 0,0,3,0
 0,0,0,3
 0,0,0,6
 9,0,0,0
12,0,0,0
""".split('\n')

test_2 = """
-1,2,2,0
0,0,2,-2
0,0,0,-2
-1,2,0,0
-2,-2,-2,2
3,0,2,-1
-1,3,2,2
-1,0,-1,0
0,2,1,-2
3,0,0,0
""".split('\n')

test_3 = """
1,-1,0,1
2,0,-1,0
3,2,-1,0
0,0,3,1
0,0,-1,-1
2,3,-2,0
-2,2,0,0
2,-2,0,-1
1,-1,0,-1
3,2,0,2
""".split('\n')

test_4 = """
1,-1,-1,-2
-2,-2,0,1
0,2,1,3
-2,3,-2,1
0,2,3,-2
-1,-1,1,-2
0,-2,-1,0
-2,2,3,-1
1,2,2,0
-1,-2,0,-2
""".split('\n')

def part1(points):
    """
    >>> part1(parse_input(test_1))
    2
    >>> part1(parse_input(test_2))
    4
    >>> part1(parse_input(test_3))
    3
    >>> part1(parse_input(test_4))
    8
    """
    close = []
    for a, b in itertools.combinations(points, 2):
        d = distance(a, b)
        if d <= 3:
            close.append((a, b))
    copy = set(points)
    count = 0
    while copy:
        count += 1
        con = set([copy.pop()])
        llen = 0
        while llen != len(con):
            llen = len(con)
            add = set()
            for i in con:
                for x in close:
                    if i in x:
                        add.add(x[0])
                        add.add(x[1])
            con.update(add)
        for i in con:
            copy.discard(i)
    return count

def distance(a, b):
    return sum(abs(i[0] - i[1]) for i in zip(a, b))

def parse_input(puzzle_input):
    points = []
    for _, line in enumerate(puzzle_input):
        if not line:
            continue
        point = tuple(int(x) for x in line.replace(',', ' ').split())
        points.append(point)
    return points

def main():
    puzzle_input = adventofcode.read_input(25)
    points = parse_input(puzzle_input)
    adventofcode.answer(1, 0, part1(points))
    #adventofcode.answer(2, 0, part2(points))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
