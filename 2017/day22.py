#!/usr/bin/env python

import adventofcode

def input_to_dict(lines):
    """
    >>> input_to_dict(["..#", "#..", "..."])
    {(1, 1): '#', (-1, 0): '#'}
    """
    result = {}
    upperleft = [-(len(lines[0])/2), len(lines)/2]
    for ypos, row in enumerate(lines):
        for xpos, cell in enumerate(row):
            if cell == "#":
                result[(upperleft[0]+xpos, upperleft[1]-ypos)] = '#'
    return result

class Grid(object):
    def __init__(self, infections):
        self.infections = infections
        self.pos = (0, 0)
        self.direction = 0
        self.movement = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        self.infection_count = 0

    def turn(self):
        self.direction += 1 if self.infections.get(self.pos, 0) else -1
        self.direction %= 4

    def infect_or_clean(self):
        if self.pos in self.infections:
            del self.infections[self.pos]
        else:
            self.infections[self.pos] = '#'
            self.infection_count += 1

    def move(self):
        self.pos = (self.pos[0] + self.movement[self.direction][0], self.pos[1] + self.movement[self.direction][1])

    def iterate(self):
        self.turn()
        self.infect_or_clean()
        self.move()

    def get_infection_count(self):
        return self.infection_count

class Grid2(Grid):
    def turn(self):
        cur = self.infections.get(self.pos, '.')
        if cur == '.':
            self.direction -= 1
        elif cur == '#':
            self.direction += 1
        elif cur == 'F':
            self.direction += 2
        self.direction %= 4

    def infect_or_clean(self):
        cur = self.infections.get(self.pos, '.')
        if cur == '.':
            self.infections[self.pos] = 'W'
        elif cur == 'W':
            self.infections[self.pos] = '#'
            self.infection_count += 1
        elif cur == '#':
            self.infections[self.pos] = 'F'
        elif cur == 'F':
            del self.infections[self.pos]

def part1(lines):
    start_grid = input_to_dict(lines)
    grid = Grid(start_grid)
    for _ in xrange(10000):
        grid.iterate()
    return grid.get_infection_count()

def part2(lines):
    start_grid = input_to_dict(lines)
    grid = Grid2(start_grid)
    for _ in xrange(10000000):
        grid.iterate()
    return grid.get_infection_count()

def main():
    lines = adventofcode.read_input(22)
    adventofcode.answer(1, 5462, part1(lines))
    adventofcode.answer(2, 2512135, part2(lines))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
