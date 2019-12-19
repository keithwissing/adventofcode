#!/usr/bin/env python3

from itertools import product
import adventofcode
from intcomputer import IntComputer

def part1(program):
    return sum(IntComputer(program).run_until_output([x, y]) for x, y in product(range(50), range(50)))

def probe(program, x, y):
    return IntComputer(program).run_until_output([x, y])

def check(program, x, y):
    return [probe(program, a, b) for a, b in [(x+99, y), (x, y+99)]]
    # return [probe(program, a, b) for a, b in [(x, y), (x+99, y), (x, y+99), (x+99, y+99)]]

def part2_manual(program):
    x = 695
    y = 903
    print(probe(program, x, y), probe(program, x+99, y))
    print(probe(program, x, y+99), probe(program, x+99, y+99))
    return x * 10000 + y

def move(program, x, y, stepf):
    last = (x, y)
    out = check(program, x, y)
    while all(v == 1 for v in out):
        last = (x, y)
        x, y = stepf(x, y)
        out = check(program, x, y)
    return last

def part2(program):
    x, y = 4000, 5000 # this starting position may not work for other inputs
    # jump, jd = 10**3, 10
    jump, jd = 3**5, 3 # this is faster
    while jump > 0:
        if any(v != 1 for v in check(program, x, y)):
            raise Exception('Lost it')
        lx, ly = x, y
        x, y = move(program, x, y, lambda x, y: (x, y-jump))
        x, y = move(program, x, y, lambda x, y: (x-jump, y))
        x, y = move(program, x, y, lambda x, y: (x-jump, y-jump))
        if lx == x and ly == y:
            jump = jump // jd
    # print(f'({x}, {y}) = {check(program, x, y)}')
    return x * 10000 + y

def main():
    puzzle_input = adventofcode.read_input(19)
    puzzle_input = [int(x) for x in puzzle_input.split(',')]
    adventofcode.answer(1, 229, part1(puzzle_input))
    # adventofcode.answer(2, 6950903, part2_manual(puzzle_input))
    adventofcode.answer(2, 6950903, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
