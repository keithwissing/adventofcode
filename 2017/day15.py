#!/usr/bin/env python

import adventofcode

def parse_input_line(line):
    """
    >>> parse_input_line("Generator A starts with 634")
    634
    """
    (_, start) = line.split("with ")
    return int(start)

class Generator(object):
    def __init__(self, factor, seed):
        self.factor = factor
        self.state = seed
    def next(self):
        self.state = (self.state * self.factor) % 2147483647
        return self.state

class PickyGenerator(object):
    def __init__(self, factor, mult, seed):
        self.factor = factor
        self.mult = mult
        self.state = seed
    def next(self):
        while True:
            self.state = (self.state * self.factor) % 2147483647
            if self.state % self.mult == 0:
                break
        return self.state

def test_generator():
    """
    >>> test_generator()
    1092455
    430625591
    """
    genA = Generator(16807, 65)
    genB = Generator(48271, 8921)
    print genA.next()
    print genB.next()

def part1(seeds):
    gens = [Generator(16807, seeds[0]), Generator(48271, seeds[1])]
    count = 0
    for x in range(40000000):
        pair = [x.next() & 0xffff for x in gens]
        if pair[0] == pair[1]:
            count += 1
    return count

def part2(seeds):
    gens = [PickyGenerator(16807, 4, seeds[0]), PickyGenerator(48271, 8, seeds[1])]
    count = 0
    for x in range(5000000):
        pair = [x.next() & 0xffff for x in gens]
        if pair[0] == pair[1]:
            count += 1
    return count

def main():
    puzzle_input = adventofcode.read_input(15)
    seeds = [parse_input_line(x) for x in puzzle_input]
    adventofcode.answer(1, 573, part1(seeds))
    adventofcode.answer(2, 294, part2(seeds))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
