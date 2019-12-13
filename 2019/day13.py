#!/usr/bin/env python3

from collections import defaultdict, Counter
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

    def run_until_output(self, inputs=None):
        self.inputs = [inputs]
        self.outputs = []
        while self.ip >= 0 and len(self.outputs) < 3:
            self.ip = self.step()
        return self.outputs if self.outputs else []

def part1(program):
    comp = IntComputer(program)
    out = comp.run_until_output()
    grid = defaultdict(lambda: 0)
    while len(out) == 3:
        x, y, tid = out
        grid[(x, y)] = tid
        out = comp.run_until_output()
    c = Counter(grid.values())
    return c[2]

def part2(program):
    program = program[:]
    program[0] = 2
    comp = IntComputer(program)
    grid = defaultdict(lambda: 0)
    ball, paddle = None, None
    score = 0
    out = comp.run_until_output(0)
    while len(out) == 3:
        x, y, tid = out
        if x == -1:
            score = tid
        else:
            grid[(x, y)] = tid
            if tid == 4:
                ball = x
            if tid == 3:
                paddle = x
        # print(f'score={score}')
        # display_dict_as_grid(grid)
        v = get_input(ball, paddle)
        out = comp.run_until_output(v)
    return score

def get_input(ball, paddle):
    if ball and paddle:
        if ball < paddle:
            return -1
        if ball > paddle:
            return 1
    return 0

def display_dict_as_grid(panel):
    disp = [' ', '#', '%', '-', 'o']
    (minX, maxX), (minY, maxY) = [(min(c), max(c)) for c in zip(*panel)]
    for row in range(minY, maxY+1):
        line = [panel[(x, row)] for x in range(minX, maxX+1)]
        line = [disp[x] for x in line]
        print(''.join(line))

def main():
    puzzle_input = adventofcode.read_input(13)
    puzzle_input = [int(x) for x in puzzle_input.split(',')]
    adventofcode.answer(1, 357, part1(puzzle_input))
    adventofcode.answer(2, 17468, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
