#!/usr/bin/env python3

from collections import defaultdict
from heapq import heappop, heappush
from itertools import chain
from string import ascii_uppercase
import adventofcode

testdata1 = [
    '         A           ',
    '         A           ',
    '  #######.#########  ',
    '  #######.........#  ',
    '  #######.#######.#  ',
    '  #######.#######.#  ',
    '  #######.#######.#  ',
    '  #####  B    ###.#  ',
    'BC...##  C    ###.#  ',
    '  ##.##       ###.#  ',
    '  ##...DE  F  ###.#  ',
    '  #####    G  ###.#  ',
    '  #########.#####.#  ',
    'DE..#######...###.#  ',
    '  #.#########.###.#  ',
    'FG..#########.....#  ',
    '  ###########.#####  ',
    '             Z       ',
    '             Z       '
]

testdata2 = [
    '                   A               ',
    '                   A               ',
    '  #################.#############  ',
    '  #.#...#...................#.#.#  ',
    '  #.#.#.###.###.###.#########.#.#  ',
    '  #.#.#.......#...#.....#.#.#...#  ',
    '  #.#########.###.#####.#.#.###.#  ',
    '  #.............#.#.....#.......#  ',
    '  ###.###########.###.#####.#.#.#  ',
    '  #.....#        A   C    #.#.#.#  ',
    '  #######        S   P    #####.#  ',
    '  #.#...#                 #......VT',
    '  #.#.#.#                 #.#####  ',
    '  #...#.#               YN....#.#  ',
    '  #.###.#                 #####.#  ',
    'DI....#.#                 #.....#  ',
    '  #####.#                 #.###.#  ',
    'ZZ......#               QG....#..AS',
    '  ###.###                 #######  ',
    'JO..#.#.#                 #.....#  ',
    '  #.#.#.#                 ###.#.#  ',
    '  #...#..DI             BU....#..LF',
    '  #####.#                 #.#####  ',
    'YN......#               VT..#....QG',
    '  #.###.#                 #.###.#  ',
    '  #.#...#                 #.....#  ',
    '  ###.###    J L     J    #.#.###  ',
    '  #.....#    O F     P    #.#...#  ',
    '  #.###.#####.#.#####.#####.###.#  ',
    '  #...#.#.#...#.....#.....#.#...#  ',
    '  #.#####.###.###.#.#.#########.#  ',
    '  #...#.#.....#...#.#.#.#.....#.#  ',
    '  #.###.#####.###.###.#.#.#######  ',
    '  #.#.........#...#.............#  ',
    '  #########.###.###.#############  ',
    '           B   J   C               ',
    '           U   P   P               '
]

testdata3 = [
    '             Z L X W       C                 ',
    '             Z P Q B       K                 ',
    '  ###########.#.#.#.#######.###############  ',
    '  #...#.......#.#.......#.#.......#.#.#...#  ',
    '  ###.#.#.#.#.#.#.#.###.#.#.#######.#.#.###  ',
    '  #.#...#.#.#...#.#.#...#...#...#.#.......#  ',
    '  #.###.#######.###.###.#.###.###.#.#######  ',
    '  #...#.......#.#...#...#.............#...#  ',
    '  #.#########.#######.#.#######.#######.###  ',
    '  #...#.#    F       R I       Z    #.#.#.#  ',
    '  #.###.#    D       E C       H    #.#.#.#  ',
    '  #.#...#                           #...#.#  ',
    '  #.###.#                           #.###.#  ',
    '  #.#....OA                       WB..#.#..ZH',
    '  #.###.#                           #.#.#.#  ',
    'CJ......#                           #.....#  ',
    '  #######                           #######  ',
    '  #.#....CK                         #......IC',
    '  #.###.#                           #.###.#  ',
    '  #.....#                           #...#.#  ',
    '  ###.###                           #.#.#.#  ',
    'XF....#.#                         RF..#.#.#  ',
    '  #####.#                           #######  ',
    '  #......CJ                       NM..#...#  ',
    '  ###.#.#                           #.###.#  ',
    'RE....#.#                           #......RF',
    '  ###.###        X   X       L      #.#.#.#  ',
    '  #.....#        F   Q       P      #.#.#.#  ',
    '  ###.###########.###.#######.#########.###  ',
    '  #.....#...#.....#.......#...#.....#.#...#  ',
    '  #####.#.###.#######.#######.###.###.#.#.#  ',
    '  #.......#.......#.#.#.#.#...#...#...#.#.#  ',
    '  #####.###.#####.#.#.#.#.###.###.#.###.###  ',
    '  #.......#.....#.#...#...............#...#  ',
    '  #############.#.#.###.###################  ',
    '               A O F   N                     ',
    '               A A D   M                     '
]

def adjacent(pos):
    # clockwise, starting up, negative y is up
    for d in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        yield (pos[0]+d[0], pos[1]+d[1])

class Grid:
    def __init__(self, lines):
        self.grid = defaultdict(lambda: ' ')
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                self.grid[(x, y)] = c
        self.width = len(lines[0])
        self.height = len(lines)
        self.portals = self.find_all_portals()

    def find_all_portals(self):
        ret = []
        for k, v in list(self.grid.items()):
            if v in ascii_uppercase:
                for t in list(adjacent(k))[1:3]: # right or down
                    if self.grid[t] in ascii_uppercase:
                        for d in chain(adjacent(k), adjacent(t)):
                            if self.grid[d] == '.':
                                ret.append((v+self.grid[t], d))
        return ret

    def portal_at(self, pos):
        for t in self.portals:
            if t[1] == pos:
                return t[0]
        return None

    def other_side(self, portal, pos):
        for t in self.portals:
            if t[0] == portal and t[1] != pos:
                return t[1]
        return None

    def isinner(self, pos):
        x, y = pos
        return 3 < y < self.height - 4 and 3 < x < self.width - 4

    def isouter(self, pos):
        x, y = pos
        return y < 3 or y > self.height - 4 or x < 3 or x > self.width - 4

    def adjacent_1(self, pos):
        for a in adjacent(pos):
            if self.grid[a] == '.':
                yield a
        port = self.portal_at(pos)
        if port and port not in ['AA', 'ZZ']:
            os = self.other_side(port, pos)
            yield os

    def adjacent_2(self, tpos):
        pos, l = tpos
        for a in adjacent(pos):
            if self.grid[a] == '.':
                yield (a, l)
        port = self.portal_at(pos)
        if port and port not in ['AA', 'ZZ']:
            os = self.other_side(port, pos)
            if self.isinner(pos) and self.isouter(os):
                yield (os, l + 1)
            if self.isouter(pos) and self.isinner(os) and l > 0:
                yield (os, l - 1)

def distances(dist, start, goal, adjf, limf=None):
    heap = []
    for a in adjf(start):
        heappush(heap, (1, a))
    while heap and goal not in dist:
        d, pos = heappop(heap)
        if pos not in dist or d < dist[pos]:
            dist[pos] = d
            for a in adjf(pos):
                if limf is None or limf(a):
                    heappush(heap, (d + 1, a))
    return dist

def part1(lines):
    """
    >>> part1(testdata1)
    23
    >>> part1(testdata2)
    58
    """
    grid = Grid(lines)
    start = grid.other_side('AA', 0)
    goal = grid.other_side('ZZ', 0)
    dist = distances({start: 0}, start, goal, grid.adjacent_1)
    return dist[goal]

def part2(lines):
    """
    >>> part2(testdata1)
    26
    >>> part2(testdata2)
    -1
    >>> part2(testdata3)
    396
    """
    grid = Grid(lines)
    start = (grid.other_side('AA', 0), 0)
    goal = (grid.other_side('ZZ', 0), 0)
    max_level = 50 # limit of 25 works for my input
    dist = distances({start: 0}, start, goal, grid.adjacent_2, lambda p: p[1] <= max_level)
    return dist[goal] if goal in dist else -1

def main():
    puzzle_input = adventofcode.read_input(20)
    adventofcode.answer(1, 516, part1(puzzle_input))
    adventofcode.answer(2, 5966, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
