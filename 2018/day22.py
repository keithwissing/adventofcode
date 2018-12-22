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

def part2(depth, target):
    """
    #>>> part2(510, (10, 10))
    #45
    """
    cave = Cave(depth, target)
    cave.calc_geo()
    todo = cave.process_nodes((0, 0, 1), 0)
    tn = (target[0], target[1], 1)
    for _ in range(1000):
        more = []
        for n, _ in todo:
            more.extend(cave.process_nodes(n, cave.mt[n]))
        todo = more
    if cave.mt.has_key(tn):
        return cave.mt[tn]

class Cave(object):
    def __init__(self, depth, target):
        self.depth = depth
        self.target = target
        self.geo = dict()
        self.ero = dict()
        self.mt = dict()

    def calc_geo(self):
        for y in range(self.target[1]+1):
            for x in range(self.target[0]+1):
                _ = self.g((x, y))

    def g(self, pos):
        if not self.geo.has_key(pos):
            if pos == (0, 0):
                self.geo[pos] = 0
            elif pos == self.target:
                self.geo[pos] = 0
            elif pos[1] == 0:
                self.geo[pos] = pos[0] * 16807
            elif pos[0] == 0:
                self.geo[pos] = pos[1] * 48271
            else:
                self.geo[pos] = self.erosion((pos[0]-1, pos[1])) * self.erosion((pos[0], pos[1]-1))
        return self.geo[pos]

    def erosion(self, pos):
        if not self.ero.has_key(pos):
            self.ero[pos] = (self.g(pos) + self.depth) % 20183
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

    def process_nodes(self, node, time):
        adj = self.adjacent_nodes(node)
        todo = []
        for n, w in adj:
            if not self.mt.has_key(n) or time + w < self.mt[n]:
                self.mt[n] = time + w
                todo.append((n, w))
        return todo

    def is_valid_node(self, node):
        return node[0] >= 0 and node[1] >= 0 and is_tool_allowed(self.type_i((node[0], node[1])), node[2])

    def adjacent_nodes(self, node):
        (x, y, tool) = node
        a = [((x-1, y, tool), 1), ((x+1, y, tool), 1), ((x, y-1, tool), 1), ((x, y+1, tool), 1), ((x, y, (tool+1)%3), 7), ((x, y, (tool+2)%3), 7)]
        return [n for n in a if self.is_valid_node(n[0])]

def is_tool_allowed(terrain, tool):
    allowed = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    return allowed[terrain][tool]

def parse_input(puzzle_input):
    depth = int(puzzle_input[0][7:])
    target = tuple(map(int, puzzle_input[1][8:].replace(',', ' ').split()))
    return depth, target

def main():
    puzzle_input = adventofcode.read_input(22)
    depth, target = parse_input(puzzle_input)
    adventofcode.answer(1, 11359, part1(depth, target))
    adventofcode.answer(2, 976, part2(depth, target))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
