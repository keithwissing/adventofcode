#!/usr/bin/env python3
import string
from itertools import cycle
from math import lcm

import adventofcode

t1 = [
    'RL',
    '',
    'AAA = (BBB, CCC)',
    'BBB = (DDD, EEE)',
    'CCC = (ZZZ, GGG)',
    'DDD = (DDD, DDD)',
    'EEE = (EEE, EEE)',
    'GGG = (GGG, GGG)',
    'ZZZ = (ZZZ, ZZZ)',
]

t2 = [
    'LLR',
    '',
    'AAA = (BBB, BBB)',
    'BBB = (AAA, ZZZ)',
    'ZZZ = (ZZZ, ZZZ)',
]

t3 = [
    'LR',
    '',
    '11A = (11B, XXX)',
    '11B = (XXX, 11Z)',
    '11Z = (11B, XXX)',
    '22A = (22B, XXX)',
    '22B = (22C, 22C)',
    '22C = (22Z, 22Z)',
    '22Z = (22B, 22B)',
    'XXX = (XXX, XXX)',
]

def parse(lines):
    instr = lines[0]
    network = {}
    for line in lines[2:]:
        line = [x for x in line.translate(str.maketrans('', '', string.punctuation)).split() if x]
        network[line[0]] = (line[1], line[2])
    return instr, network

def part1(lines):
    """
    >>> part1(t1)
    2
    >>> part1(t2)
    6
    """
    instr, network = parse(lines)
    pos = 'AAA'
    count = 0
    for n in cycle(instr):
        count += 1
        pos = network[pos][0 if n == 'L' else 1]
        if pos == 'ZZZ':
            break
    return count

def loop_size(pos, instr, network):
    count = 0
    for n in cycle(instr):
        count += 1
        pos = network[pos][0 if n == 'L' else 1]
        if pos[2] == 'Z':
            return count

def part2(lines):
    """
    >>> part2(t3)
    6
    """
    instr, network = parse(lines)
    pos = [x for x in network.keys() if x.endswith('Z')]
    counts = [loop_size(p, instr, network) for p in pos]
    return lcm(*counts)

def main():
    puzzle_input = adventofcode.read_input(8)
    adventofcode.answer(1, 18673, part1(puzzle_input))
    adventofcode.answer(2, 17972669116327, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
