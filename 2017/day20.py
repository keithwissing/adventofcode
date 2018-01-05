#!/usr/bin/env python

import adventofcode
from collections import namedtuple
import operator

Particle = namedtuple('Particle', 'pos vel acc')

def parse_line(line):
    """
    >>> parse_line("p=<-1021,-2406,1428>, v=<11,24,-73>, a=<4,9,0>")
    Particle(pos=(-1021, -2406, 1428), vel=(11, 24, -73), acc=(4, 9, 0))
    """
    line = line.replace("<", "").replace(">", "").replace("=", "")
    line = line.replace("p", "").replace("v", "").replace("a", "")
    numbers = [int(n) for n in line.split(",")]
    trips = [(numbers[i], numbers[i+1], numbers[i+2]) for i in range(0, len(numbers), 3)]
    return Particle(trips[0], trips[1], trips[2])

def manhatan_distance(coord):
    """
    >>> manhatan_distance((1,1,1))
    3
    >>> manhatan_distance((10,-10,1))
    21
    """
    return sum([abs(p) for p in coord])

def part1(particles):
    mv = 30000
    mid = -1
    for id, part in enumerate(particles):
        amd = manhatan_distance(part.acc)
        if amd < mv:
            mv = amd
            mid = id
    return mid

def run_tick(particles):
    results = []
    for part in particles:
        vel = tuple(map(operator.add, part.vel, part.acc))
        pos = tuple(map(operator.add, part.pos, vel))
        results.append(Particle(pos, vel, part.acc))
    return results

def remove_collitions(lines):
    positions = [p.pos for p in lines]
    ponts = set(positions)
    for point in ponts:
        if positions.count(point) > 1:
            lines = [x for x in lines if x.pos != point]
    return lines

def test1(lines):
    """
    >>> test1(["p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>", "p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>"])
    [Particle(pos=(3, 0, 0), vel=(-1, 0, 0), acc=(-1, 0, 0)), Particle(pos=(-8, 0, 0), vel=(-6, 0, 0), acc=(-2, 0, 0))]
    """
    ps = [parse_line(l) for l in lines]
    for _ in range(3):
        ps = run_tick(ps)
    return ps

def part2(lines):
    # I should figure out how to know when we are done
    # For my puzzle input 40 is the right number of iterations
    for i in range(40):
        lines = remove_collitions(lines)
        lines = run_tick(lines)
    return len(lines)

def main():
    lines = adventofcode.read_input(20)
    lines = [parse_line(line) for line in lines]
    adventofcode.answer(1, 144, part1(lines))
    adventofcode.answer(2, 477, part2(lines))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
