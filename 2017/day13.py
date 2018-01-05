#!/usr/bin/env python

import adventofcode

def parse_input_line(line):
    """
    >>> parse_input_line("24: 10")
    (24, 10)
    """
    (depth, range) = line.split(": ")
    return (int(depth), int(range))

def part1(layers):
    """
    >>> part1([(0, 3), (1, 2), (4, 4), (6, 4)])
    24
    """
    (_, severity) = make_a_run(layers, 0)
    return severity

def make_a_run(layers, delay):
    caught = False
    severity = 0
    for layer in layers:
        (depth, range) = layer
        if ((depth+delay) % (2*range-2)) == 0:
            caught = True
            severity += depth * range
    return (caught, severity)

def is_caught(layers, delay):
    (caught, _) = make_a_run(layers, delay)
    return caught

def part2(layers):
    """
    >> part2([(0, 3), (1, 2), (4, 4), (6, 4)])
    10
    """
    delay = 0
    while is_caught(layers, delay):
        delay += 1
    return delay

def main():
    puzzle_input = adventofcode.read_input(13)
    layers = [parse_input_line(x) for x in puzzle_input]
    adventofcode.answer(1, 2384, part1(layers))
    adventofcode.answer(2, 3921270, part2(layers))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
