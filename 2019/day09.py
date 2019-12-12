#!/usr/bin/env python3

from collections import defaultdict
import adventofcode

def split_code(code):
    """
    >>> split_code(1103)
    ('0011', 3)
    """
    opcode = code % 100
    modes = str(code // 100).zfill(4)
    return (modes, opcode)

class IntComputer:
    def __init__(self, mem, inputs=None):
        self.ip = 0
        self.rbase = 0
        self.mem = defaultdict(lambda: 0, {k:v for k, v in enumerate(mem)})
        self.inputs = [] if not inputs else inputs[:] if isinstance(inputs, list) else [inputs]
        self.outputs = []

    def get_param(self, n, modes):
        if modes[4-n] == '0':
            return self.mem[self.mem[self.ip+n]]
        if modes[4-n] == '1':
            return self.mem[self.ip+n]
        if modes[4-n] == '2':
            return self.mem[self.rbase+self.mem[self.ip+n]]
        raise Exception('invalid read param mode')

    def write(self, n, modes, value):
        if modes[4-n] == '0':
            self.mem[self.mem[self.ip+n]] = value
        elif modes[4-n] == '2':
            self.mem[self.rbase+self.mem[self.ip+n]] = value
        else:
            raise Exception('invalid write param mode')

    def step(self):
        ip = self.ip
        (modes, opcode) = split_code(self.mem[self.ip])
        if opcode == 99:
            return -1
        if opcode == 3: # input
            self.write(1, modes, self.inputs.pop(0))
            return ip + 2
        p1 = self.get_param(1, modes)
        if opcode == 4: # output
            self.outputs.append(p1)
            return ip + 2
        if opcode == 9: # relative base adjust
            self.rbase += p1
            return ip + 2
        p2 = self.get_param(2, modes)
        if opcode == 5: # jump-if-true
            return p2 if p1 != 0 else ip + 3
        if opcode == 6: # jump-if-false
            return p2 if p1 == 0 else ip + 3
        if opcode == 1: # add
            self.write(3, modes, p1 + p2)
            return ip + 4
        if opcode == 2: # multiply
            self.write(3, modes, p1 * p2)
            return ip + 4
        if opcode == 7: # less than
            self.write(3, modes, 1 if p1 < p2 else 0)
            return ip + 4
        if opcode == 8: # equals
            self.write(3, modes, 1 if p1 == p2 else 0)
            return ip + 4
        raise Exception(f'invalid opcode {opcode} at {ip}')

    def run_program(self):
        while self.ip >= 0:
            self.ip = self.step()
        return self.outputs

    def run_until_output(self):
        self.outputs = []
        while self.ip >= 0 and not self.outputs:
            self.ip = self.step()
        return self.outputs[0] if self.outputs else 0

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
