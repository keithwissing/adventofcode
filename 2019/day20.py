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
        self.all = self.find_all_portals()

    def find_all_portals(self):
        ret = []
        for k, v in list(self.grid.items()):
            if v in ascii_uppercase:
                for t in list(adjacent(k))[1:3]:
                    if self.grid[t] in ascii_uppercase:
                        for d in chain(adjacent(k), adjacent(t)):
                            if self.grid[d] == '.':
                                ret.append((v+self.grid[t], d))
        return ret

    def find(self, portal, pos):
        for t in self.all:
            if t[0] == portal and t[1] != pos:
                return t[1]
        return None

    def portal(self, pos):
        for t in self.all:
            if t[1] == pos:
                return t[0]
        return None

def part1(lines):
    """
    >>> part1(testdata1)
    23
    >>> part1(testdata2)
    58
    """
    grid = Grid(lines)
    dist = {}
    heap = []
    pos = grid.find('AA', (0, 0))
    dist[pos] = 0
    for a in adjacent(pos):
        heappush(heap, (1, a))
    while heap:
        d, pos = heappop(heap)
        if grid.grid[pos] == '.':
            if pos not in dist or d < dist[pos]:
                dist[pos] = d
                for a in adjacent(pos):
                    if grid.grid[a] == '.':
                        heappush(heap, (d + 1, a))
                port = grid.portal(pos)
                if port and port not in ['AA', 'ZZ']:
                    os = grid.find(port, pos)
                    heappush(heap, (d + 1, os))
    pos = grid.find('ZZ', (0, 0))
    return dist[pos]

def main():
    puzzle_input = adventofcode.read_input(20)
    adventofcode.answer(1, 516, part1(puzzle_input))
    # adventofcode.answer(2, 0, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
