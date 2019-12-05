#!/usr/bin/env python3

import adventofcode

def split_code(code):
    """
    >>> split_code(1103)
    ('0011', 3)
    """
    opcode = int(str(code)[-2:])
    modes = ('0000'+str(code)[:-2])[-4:]
    return (modes, opcode)

inputs = []
outputs = []

def step(mem, ip):
    (modes, opcode) = split_code(mem[ip])
    if opcode == 99:
        return -1
    if opcode == 3: # input
        mem[mem[ip+1]] = inputs.pop()
        return ip + 2
    p1 = mem[mem[ip+1]] if modes[3] == '0' else mem[ip+1]
    if opcode == 4: # output
        outputs.append(p1)
        return ip + 2
    p2 = mem[mem[ip+2]] if modes[2] == '0' else mem[ip+2]
    if opcode == 5: # jump-if-true
        return p2 if p1 != 0 else ip + 3
    if opcode == 6: # jump-if-false
        return p2 if p1 == 0 else ip + 3
    if opcode == 1: # add
        mem[mem[ip+3]] = p1 + p2
        return ip + 4
    if opcode == 2: # multiply
        mem[mem[ip+3]] = p1 * p2
        return ip + 4
    if opcode == 7: # less than
        mem[mem[ip+3]] = 1 if p1 < p2 else 0
        return ip + 4
    if opcode == 8: # equals
        mem[mem[ip+3]] = 1 if p1 == p2 else 0
        return ip + 4
    raise Exception('invalid opcode')

def run_program(mem):
    memcopy = mem[:]
    ip = 0
    while ip >= 0:
        ip = step(memcopy, ip)

def part1(mem):
    inputs.append(1)
    outputs.clear()
    run_program(mem)
    return outputs[-1]

def part2(mem):
    inputs.append(5)
    outputs.clear()
    run_program(mem)
    return outputs[0]

def main():
    puzzle_input = adventofcode.read_input(5)
    puzzle_input = [int(x) for x in puzzle_input.split(',')]
    adventofcode.answer(1, 8332629, part1(puzzle_input))
    adventofcode.answer(2, 8805067, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
