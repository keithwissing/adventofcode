#!/usr/bin/env python

import collections
import re
import sys
import adventofcode

sys.setrecursionlimit(10000)

def part1(puzzle_input):
    """
    >>> part1('^WNE$')
    (3, 0)
    >>> part1('^ENWWW(NEEE|SSE(EE|N))$')
    (10, 0)
    >>> part1('^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$')
    (18, 0)
    >>> part1('^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$')
    (23, 0)
    >>> part1('^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$')
    (31, 0)
    """
    tokens = [i for i in re.split(r'([NSEW]+|\||\(|\))', puzzle_input) if i]
    fac = Map()
    stack = []
    pos = (0, 0)
    for token in tokens[1:-1]:
        if token == '(':
            stack.append(pos)
        elif token == ')':
            pos = stack.pop()
        elif token == '|':
            pos = stack[-1]
        else:
            pos = fac.add_rooms(pos, token)
    fac.build_distances((0, 0), 0)
    return fac.get_max_distance(), fac.get_part2()

class Map(object):
    def __init__(self):
        self.data = collections.defaultdict(lambda: ' ')
        self.data[(0, 0)] = 'X'
        self.dists = collections.defaultdict(lambda: -1)
        self.min_x = 0
        self.max_x = 0
        self.min_y = 0
        self.max_y = 0

    def display(self):
        for y in range(self.min_y, self.max_y+1):
            print ''.join([self.data[(x, y)] for x in range(self.min_x, self.max_x+1)])

    def display_d(self):
        for y in range(self.min_y, self.max_y+1):
            print ','.join([str(self.dists[(x, y)]) for x in range(self.min_x, self.max_x+1)])

    def add_rooms(self, pos, directions):
        for md in directions:
            move = {'N': [0, -1], 'S': [0, 1], 'E': [1, 0], 'W': [-1, 0]}[md]
            pos = (pos[0]+move[0], pos[1]+move[1])
            self.data[pos] = '+'
            pos = (pos[0]+move[0], pos[1]+move[1])
            self.data[pos] = '.'
            self.expand_limits(pos)
        return pos

    def expand_limits(self, pos):
        self.min_x = min(pos[0], self.min_x)
        self.max_x = max(pos[0], self.max_x)
        self.min_y = min(pos[1], self.min_y)
        self.max_y = max(pos[1], self.max_y)

    def build_distances(self, pos, dist=0):
        cd = self.dists[pos]
        if cd == -1 or dist < cd:
            self.dists[pos] = dist
            moves = {'N': [0, -1], 'S': [0, 1], 'E': [1, 0], 'W': [-1, 0]}
            for move in moves.values():
                dpos = (pos[0]+move[0], pos[1]+move[1])
                if self.data[dpos] == '+':
                    rpos = (dpos[0]+move[0], dpos[1]+move[1])
                    self.build_distances(rpos, dist+1)

    def get_max_distance(self):
        return max(self.dists.values())

    def get_part2(self):
        return sum([1 for i in self.dists.values() if i >= 1000])

def main():
    puzzle_input = adventofcode.read_input(20)
    a1, a2 = part1(puzzle_input)
    adventofcode.answer(1, 4239, a1)
    adventofcode.answer(2, 8205, a2)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
