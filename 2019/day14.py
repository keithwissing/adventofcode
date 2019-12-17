#!/usr/bin/env python3

from collections import defaultdict
import adventofcode

testdata1 = [
    '10 ORE => 10 A',
    '1 ORE => 1 B',
    '7 A, 1 B => 1 C',
    '7 A, 1 C => 1 D',
    '7 A, 1 D => 1 E',
    '7 A, 1 E => 1 FUEL']

testdata2 = [
    '9 ORE => 2 A',
    '8 ORE => 3 B',
    '7 ORE => 5 C',
    '3 A, 4 B => 1 AB',
    '5 B, 7 C => 1 BC',
    '4 C, 1 A => 1 CA',
    '2 AB, 3 BC, 4 CA => 1 FUEL']

testdata3 = [
    '157 ORE => 5 NZVS',
    '165 ORE => 6 DCFZ',
    '44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL',
    '12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ',
    '179 ORE => 7 PSHF',
    '177 ORE => 5 HKGWZ',
    '7 DCFZ, 7 PSHF => 2 XJWVT',
    '165 ORE => 2 GPVTF',
    '3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT']

testdata4 = [
    '2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG',
    '17 NVRVD, 3 JNWZP => 8 VPVL',
    '53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL',
    '22 VJHF, 37 MNCFX => 5 FWMGM',
    '139 ORE => 4 NVRVD',
    '144 ORE => 7 JNWZP',
    '5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC',
    '5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV',
    '145 ORE => 6 MNCFX',
    '1 NVRVD => 8 CXFTF',
    '1 VJHF, 6 MNCFX => 4 RFSQX',
    '176 ORE => 6 VJHF']

def test1(pi):
    """
    >>> test1(testdata1)
    31
    >>> test1(testdata2)
    165
    >>> test1(testdata3)
    13312
    >>> test1(testdata4)
    180697
    """
    reactions = parse(pi)
    return part1(reactions)

def make_fuel(reactions, q):
    inv = defaultdict(lambda: 0)
    inv['FUEL'] = -q
    more = True
    while more:
        more = False
        for k, v in list(inv.items()):
            if k != 'ORE':
                if v < 0:
                    r = reactions[k]
                    d = (-v + r[0] - 1) // r[0]
                    for i, q in r[1]:
                        inv[i] -= q*d
                    inv[k] += r[0]*d
                    more = True
    return -inv['ORE']

def part1(reactions):
    return make_fuel(reactions, 1)

def test2(pi):
    """
    >>> test2(testdata3)
    82892753
    >>> test2(testdata4)
    5586022
    """
    reactions = parse(pi)
    return part2(reactions)

def part2(reactions):
    tq = 1000000
    sv = tq // 10
    while True:
        r = make_fuel(reactions, tq)
        if r < 1000000000000:
            tq += sv
        elif r > 1000000000000:
            tq -= sv
            sv //= 10
            if sv == 0:
                return tq

def parse(lines):
    ret = {}
    for line in lines:
        sides = line.split('=>')
        dq, d = sides[1].split()
        il = sides[0].split(',')
        il = [i.split() for i in il]
        il = [(i, int(q)) for q, i in il]
        ret[d] = [int(dq), il]
    return ret

def main():
    puzzle_input = adventofcode.read_input(14)
    puzzle_input = parse(puzzle_input)
    adventofcode.answer(1, 532506, part1(puzzle_input))
    adventofcode.answer(2, 2595245, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
