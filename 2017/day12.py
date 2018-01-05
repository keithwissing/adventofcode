#!/usr/bin/env python

import adventofcode

def parse_input_line(line):
    """
    >>> parse_input_line("2 <-> 0, 3, 4")
    (2, [0, 3, 4])
    """
    (p, rest) = line.split(" <-> ")
    links = [int(x) for x in rest.split(",")]
    return (int(p), links)

def part1(pipes):
    """
    >>> part1([(0, [2]), (1, [1]), (2, [0, 3, 4]), (3, [2, 4]), (4, [2, 3, 6]), (5, [6]), (6, [4, 5])])
    6
    """
    connected = { 0: True}
    lastlen = 0
    dpipes = { p: c for (p, c) in pipes}
    while (len(connected) != lastlen):
        lastlen = len(connected)
        for key in connected.keys():
            for p in dpipes[key]:
                connected[p] = True
    return lastlen

def part2(pipes):
    """
    >>> part2([(0, [2]), (1, [1]), (2, [0, 3, 4]), (3, [2, 4]), (4, [2, 3, 6]), (5, [6]), (6, [4, 5])])
    2
    """
    dpipes = { p: c for (p, c) in pipes}
    groups = 0
    while len(dpipes) > 0:
        groups += 1
        connected = { dpipes.keys()[0] : True}
        lastlen = 0
        while (len(connected) != lastlen):
            lastlen = len(connected)
            for key in connected.keys():
                for p in dpipes[key]:
                    connected[p] = True
        for rem in connected.keys():
            del dpipes[rem]
    return groups

def main():
    puzzle_input = adventofcode.read_input(12)
    pipes = [parse_input_line(x) for x in puzzle_input]
    adventofcode.answer(1, 378, part1(pipes))
    adventofcode.answer(2, 204, part2(pipes))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
