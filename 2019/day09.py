#!/usr/bin/env python3

import adventofcode
from intcomputer import IntComputer

def test1(program):
    """
    >>> test1([104,1125899906842624,99])
    [1125899906842624]
    >>> test1([1102,34915192,34915192,7,4,7,99,0])
    [1219070632396864]
    >>> test1([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99])
    [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
    """
    comp = IntComputer(program)
    return comp.run_program()

def part1(program):
    comp = IntComputer(program, 1)
    return comp.run_program()[0]

def part2(program):
    comp = IntComputer(program, 2)
    return comp.run_program()[0]

def main():
    puzzle_input = adventofcode.read_input(9)
    puzzle_input = [int(x) for x in puzzle_input.split(',')]
    adventofcode.answer(1, 3241900951, part1(puzzle_input))
    adventofcode.answer(2, 83089, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
