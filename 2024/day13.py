#!/usr/bin/env python3
from itertools import product

import adventofcode

t1 = [
    'Button A: X+94, Y+34',
    'Button B: X+22, Y+67',
    'Prize: X=8400, Y=5400',
    '',
    'Button A: X+26, Y+66',
    'Button B: X+67, Y+21',
    'Prize: X=12748, Y=12176',
    '',
    'Button A: X+17, Y+86',
    'Button B: X+84, Y+37',
    'Prize: X=7870, Y=6450',
    '',
    'Button A: X+69, Y+23',
    'Button B: X+27, Y+71',
    'Prize: X=18641, Y=10279',
]

def parse(lines):
    machines = []
    for line in lines:
        numbers = tuple(int(x) for x in ''.join(filter(lambda i: i.isdigit() or i == ' ', line)).split())
        if 'A:' in line:
            a = numbers
        if 'B:' in line:
            b = numbers
        if 'Prize:' in line:
            machines.append((a, b, numbers))
    return machines

def calc_brute_force(machine):
    a, b, p = machine
    wins = []
    for pa, pb in product(range(100), range(100)):
        if a[0] * pa + b[0] * pb == p[0] and a[1] * pa + b[1] * pb == p[1]:
            wins.append((pa, pb))
    return min(pa * 3 + pb for pa, pb in wins) if wins else 0

def calc(machine, add=0):
    a, b, p = machine
    p = (p[0] + add, p[1] + add)
    pa = (b[0] * p[1] - b[1] * p[0]) // (a[1] * b[0] - a[0] * b[1])
    pb = (a[0] * p[1] - a[1] * p[0]) // (b[1] * a[0] - b[0] * a[1])
    return pa * 3 + pb if a[0] * pa + b[0] * pb == p[0] and a[1] * pa + b[1] * pb == p[1] else 0

def part1(lines):
    """
    >>> part1(t1)
    480
    """
    machines = parse(lines)
    return sum(calc(m) for m in machines)

def part2(lines):
    """
    >>> part2(t1)
    875318608908
    """
    machines = parse(lines)
    return sum(calc(m, 10000000000000) for m in machines)

def main():
    puzzle_input = adventofcode.read_input(13)
    adventofcode.answer(1, 33209, part1(puzzle_input))
    adventofcode.answer(2, 83102355665474, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
