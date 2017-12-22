#!/usr/bin/env python

def input_to_dict(lines):
    """
    >>> input_to_dict(["..#", "#..", "..."])
    {(1, 1): 1, (-1, 0): 1}
    """
    result = {}
    upperleft = [-(len(lines[0])/2), len(lines)/2]
    for ypos, row in enumerate(lines):
        for xpos, cell in enumerate(row):
            if cell == "#":
                result[(upperleft[0]+xpos, upperleft[1]-ypos)] = 1
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
            self.infections[self.pos] = 1
            self.infection_count += 1

    def move(self):
        self.pos = (self.pos[0] + self.movement[self.direction][0], self.pos[1] + self.movement[self.direction][1])

    def iterate(self):
        self.turn()
        self.infect_or_clean()
        self.move()

    def get_infection_count(self):
        return self.infection_count

def part1(lines):
    start_grid = input_to_dict(lines)
    grid = Grid(start_grid)
    for _ in xrange(10000):
        grid.iterate()
    return grid.get_infection_count()

def main():
    lines = [line.rstrip('\n') for line in open("day22_input.txt")]
    a1 = part1(lines)
    print "Part 1 Answer", a1
    assert a1 == 5462
    #a2 = part2(lines)
    #print "Part 2 Answer", a2
    #assert a2 == 17628

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
