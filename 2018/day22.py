#!/usr/bin/env python

import adventofcode

def part1(depth, target):
    """
    >>> part1(510, (10, 10))
    114
    """
    cave = Cave(depth, target)
    cave.calc_geo()
    return cave.part1()

class Cave(object):
    def __init__(self, depth, target):
        self.depth = depth
        self.target = target
        self.geo = dict()
        self.ero = dict()

    def calc_geo(self):
        for y in range(self.target[1]+1):
            for x in range(self.target[0]+1):
                if (x, y) == (0, 0):
                    self.geo[(x, y)] = 0
                elif (x, y) == self.target:
                    self.geo[(x, y)] = 0
                elif y == 0:
                    self.geo[(x, y)] = x * 16807
                elif x == 0:
                    self.geo[(x, y)] = y * 48271
                else:
                    self.geo[(x, y)] = self.erosion((x-1, y)) * self.erosion((x, y-1))

    def erosion(self, pos):
        if not self.ero.has_key(pos):
            self.ero[pos] = (self.geo[pos] + self.depth) % 20183
        return self.ero[pos]

    def type_c(self, pos):
        return '.=|'[self.erosion(pos)%3]

    def type_i(self, pos):
        return self.erosion(pos)%3
    
    def display(self):
        for y in range(self.target[1]+1):
            print ''.join([self.type_c((x, y)) for x in range(self.target[0]+1)])

    def part1(self):
        risk = 0
        for y in range(self.target[1]+1):
            for x in range(self.target[0]+1):
                risk += self.type_i((x, y))
        return risk

def parse_input(puzzle_input):
    depth = int(puzzle_input[0][7:])
    target = tuple(map(int, puzzle_input[1][8:].replace(',', ' ').split()))
    return depth, target

def main():
    puzzle_input = adventofcode.read_input(22)
    depth, target = parse_input(puzzle_input)
    adventofcode.answer(1, 11359, part1(depth, target))
    #adventofcode.answer(2, 0, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
