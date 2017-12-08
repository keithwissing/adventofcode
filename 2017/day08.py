#!/usr/bin/env python

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
    puzzle_input = [line.rstrip('\n') for line in open("day08_input.txt")]
    instructions = [parse_input_line(x) for x in puzzle_input]
    print "Part 1 Answer", part1(instructions)
    print "Part 2 Answer", part2(instructions)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
