#!/usr/bin/env python

import adventofcode
from collections import namedtuple

Instruction = namedtuple('Instruction', 'register op arg check compare val')

def parse_input_line(line):
    """
    >>> parse_input_line("b inc 5 if a > 1")
    Instruction(register='b', op='inc', arg=5, check='a', compare='>', val=1)
    """
    a = line.split()
    return Instruction(a[0], a[1], int(a[2]), a[4], a[5], int(a[6]))

def run_program(instructions):
    registers = {}
    mv = 0
    for instr in instructions:
        cr = instr.check
        co = instr.compare
        cv = instr.val
        rv = registers.get(cr, 0)
        if co == '>':
            res = rv > cv
        elif co == '>=':
            res = rv >= cv
        elif co == '<':
            res = rv < cv
        elif co == '<=':
            res = rv <= cv
        elif co == '==':
            res = rv == cv
        elif co == '!=':
            res = rv != cv
        if res:
            ov = registers.get(instr.register, 0)
            if instr.op == 'inc':
                nv = ov + instr.arg
            elif instr.op == 'dec':
                nv = ov - instr.arg
            registers[instr.register] = nv
            mv = max(mv, nv)
    return (registers, mv)

def part1(instructions):
    registers, _ = run_program(instructions)
    return max(registers.values())

def part2(instructions):
    _, mv = run_program(instructions)
    return mv

def main():
    puzzle_input = adventofcode.read_input(8)
    instructions = [parse_input_line(x) for x in puzzle_input]
    adventofcode.answer(1, 6343, part1(instructions))
    adventofcode.answer(2, 7184, part2(instructions))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
