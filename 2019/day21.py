#!/usr/bin/env python3

import adventofcode
from intcomputer import IntComputer

def part1(program):
    comp = IntComputer(program)
    inputs = """\
NOT A J
NOT B T
OR T J
NOT C T
OR T J
AND D J
WALK
"""
    comp.inputs.extend([ord(c) for c in inputs])
    out = comp.run_program()
    # print(''.join([chr(x) for x in out[:-1]]))
    return out[-1]

def part2(program):
    comp = IntComputer(program)
    inputs = """\
NOT A J
NOT B T
OR T J
NOT C T
OR T J
AND D J
AND H J
NOT A T
OR T J
RUN
"""
    comp.inputs.extend([ord(c) for c in inputs])
    out = comp.run_program()
    # print(''.join([chr(x) for x in out[:-1]]))
    return out[-1]

def main():
    puzzle_input = adventofcode.read_input(21)
    puzzle_input = [int(x) for x in puzzle_input.split(',')]
    adventofcode.answer(1, 19361414, part1(puzzle_input))
    adventofcode.answer(2, 1139205618, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
