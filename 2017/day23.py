#!/usr/bin/env python

import adventofcode

def parse_input_line(line):
    """
    >>> parse_input_line("set p 316")
    ['set', 'p', '316']
    """
    return line.split()

def run_program(instructions, is_part2):
    reg = {}
    ip = 0
    if is_part2:
        reg["a"] = 1
    count_mul = 0
    while ip >= 0 and ip < len(instructions):
        # if ip != 26:
        #     print ip, reg
        inst = instructions[ip]
        arg1 = reg.get(inst[1], 0) if inst[1].isalpha() else int(inst[1])
        if len(inst) > 2:
            val = reg.get(inst[2], 0) if inst[2].isalpha() else int(inst[2])
        else:
            val = 0
        if inst[0] == "set":
            reg[inst[1]] = val
        elif inst[0] == "add":
            reg[inst[1]] = reg.get(inst[1], 0) + val
        elif inst[0] == "sub":
            reg[inst[1]] = reg.get(inst[1], 0) - val
        elif inst[0] == "mul":
            reg[inst[1]] = reg.get(inst[1], 0) * val
            count_mul += 1
        elif inst[0] == "mod":
            reg[inst[1]] = reg.get(inst[1], 0) % val
        elif inst[0] == "jnz":
            if arg1 != 0:
                ip += val - 1
        elif inst[0] == "jgz":
            if arg1 > 0:
                ip += val - 1
        else:
            raise "unknown op"
        ip += 1
    return (count_mul, reg["h"])

def part1(instructions):
    return run_program(instructions, False)[0]

def part2(instructions):
    return run_program(instructions, True)[1]

def main():
    puzzle_input = adventofcode.read_input(23)
    instructions = [parse_input_line(x) for x in puzzle_input]
    adventofcode.answer(1, 6241, part1(instructions))
    #adventofcode.answer(2, 0, part2(instructions))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
