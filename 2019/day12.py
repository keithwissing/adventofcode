#!/usr/bin/env python3

from itertools import chain, combinations
from math import gcd
import adventofcode

testcase1 = [
    '<x=-1, y=0, z=2>',
    '<x=2, y=-10, z=-7>',
    '<x=4, y=-8, z=8>',
    '<x=3, y=5, z=-1>'
]

testcase2 = [
    '<x=-8, y=-10, z=0>',
    '<x=5, y=5, z=10>',
    '<x=2, y=-7, z=3>',
    '<x=9, y=-8, z=-3>'
]

def dv(a, b):
    if b > a:
        return 1
    if a > b:
        return -1
    return 0

class Moon:
    def __init__(self, pos):
        self.pos = pos
        self.vel = (0, 0, 0)

    def pull(self, other):
        x1, y1, z1 = self.pos
        x2, y2, z2 = other.pos
        change = (dv(x1, x2), dv(y1, y2), dv(z1, z2))
        self.vel = tuple(map(sum, zip(self.vel, change)))

    def move(self):
        self.pos = tuple(map(sum, zip(self.pos, self.vel)))

    def energy(self):
        return sum([abs(x) for x in self.pos]) * sum([abs(x) for x in self.vel])

    def dump(self):
        print(f'pos={self.pos} vel={self.vel}')

def test1(puzzle_input, rounds):
    """
    >>> test1(testcase1, 10)
    179
    >>> test1(testcase2, 100)
    1940
    """
    parsed = parse(puzzle_input)
    return part1(parsed, rounds)

def test2(puzzle_input):
    """
    >>> test2(testcase1)
    2772
    >>> test2(testcase2)
    4686774924
    """
    parsed = parse(puzzle_input)
    return part2(parsed)

def timestep(moons):
    for a, b in combinations(moons, 2):
        a.pull(b)
        b.pull(a)
    for m in moons:
        m.move()

def part1(parsed, rounds):
    moons = [Moon(pos) for pos in parsed]
    for _ in range(0, rounds):
        timestep(moons)
    return sum([m.energy() for m in moons])

def part2(parsed):
    moons = [Moon(pos) for pos in parsed]
    mem = [{}, {}, {}]
    loops = [[], [], []]
    time = 0
    while [] in loops:
        axes = [tuple(chain(*[[m.pos[c], m.vel[c]] for m in moons])) for c in range(0, 3)]
        for c in range(0, 3):
            if not loops[c]:
                if axes[c] in mem[c]:
                    loops[c] = [mem[c][axes[c]], time]
                else:
                    mem[c][axes[c]] = time
        timestep(moons)
        time += 1
    # print(loops)
    return lcm(lcm(loops[0][1], loops[1][1]), loops[2][1])

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

def parse(lines):
    ret = []
    for line in lines:
        line = line.replace('<', '').replace('>', '').replace(',', '')
        line = [x[2:] for x in line.split()]
        line = [int(x) for x in line]
        ret.append(line)
    return ret

def main():
    puzzle_input = adventofcode.read_input(12)
    puzzle_input = parse(puzzle_input)
    adventofcode.answer(1, 8310, part1(puzzle_input, 1000))
    adventofcode.answer(2, 319290382980408, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
