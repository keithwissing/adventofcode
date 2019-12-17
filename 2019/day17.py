#!/usr/bin/env python3

from collections import defaultdict
from itertools import product
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
        while self.ip >= 0 and not self.outputs:
            self.ip = self.step()
        return self.outputs[0] if self.outputs else -1

def part1(program):
    comp = IntComputer(program)
    out = comp.run_until_output()
    grid = {}
    pos = (0, 0)
    while out > 0:
        if out == 10:
            pos = (0, pos[1]+1)
        else:
            grid[pos] = chr(out)
            pos = (pos[0]+1, pos[1])
        out = comp.run_until_output()
    # display_dict_as_grid(grid)
    (minX, maxX), (minY, maxY) = [(min(c), max(c)) for c in zip(*grid)]
    total = 0
    for x, y in product(range(minX+1, maxX), range(minY+1, maxY)):
        pos = (x, y)
        if grid[pos] == '#':
            if all(grid[c] == '#' for c in adjacent(pos)):
                total += x * y
    stuff(grid)
    return total

def adjacent(pos):
    # for d in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
    for d in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        yield (pos[0]+d[0], pos[1]+d[1])

def display_dict_as_grid(panel):
    (minX, maxX), (minY, maxY) = [(min(c), max(c)) for c in zip(*panel)]
    for row in range(minY, maxY+1):
        line = [panel[(x, row)] for x in range(minX, maxX+1)]
        # print(line)
        print(''.join(line))

def stuff(grid):
    grid = defaultdict(lambda: ' ', grid)
    for p in grid:
        if grid[p] in ['<', '^', '>', 'v']:
            pos = p
    bd = {'^': 0, '>': 1, 'v': 2, '<': 3}[grid[pos]]
    # print(f'pos {pos} dir {bd}')
    steps = []
    turn = 'S'
    while turn != '':
        turn = find_turn(grid, pos, bd)
        if turn:
            bd = (bd + (-1 if turn == 'L' else 1)) % 4
            fwd = find_forward(grid, pos, bd)
            delta = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}[bd]
            for _ in range(fwd):
                pos = (pos[0]+delta[0], pos[1]+delta[1])
            steps.append(turn)
            steps.append(str(fwd))
            grid[pos] = 'O'
    print(','.join(steps))
    # display_dict_as_grid(grid)

def find_forward(grid, pos, bd):
    delta = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}[bd]
    tot = 0
    pos = (pos[0]+delta[0], pos[1]+delta[1])
    while grid[pos] == '#':
        tot += 1
        pos = (pos[0]+delta[0], pos[1]+delta[1])
    return tot

def find_turn(grid, pos, bd):
    adj = [grid[p] for p in adjacent(pos)]
    if bd == 0:
        if adj[1] == '#':
            return 'R'
        if adj[3] == '#':
            return 'L'
    if bd == 2:
        if adj[1] == '#':
            return 'L'
        if adj[3] == '#':
            return 'R'
    if bd == 1:
        if adj[0] == '#':
            return 'L'
        if adj[2] == '#':
            return 'R'
    if bd == 3:
        if adj[0] == '#':
            return 'R'
        if adj[2] == '#':
            return 'L'
    return ''

def part2(program):
    comp = IntComputer(program)
    comp.mem[0] = 2
# A L,6, R,8, R,12, L,6, L,8,
# B L,10, L,8, R,12,
# A L,6, R,8, R,12, L,6, L,8,
# C L,8, L,10, L,6, L,6,
# B L,10, L,8, R,12,
# C L,8, L,10, L,6, L,6,
# B L,10, L,8, R,12,
# A L,6, R,8, R,12, L,6, L,8,
# C L,8, L,10, L,6, L,6,
# B L,10, L,8, R,12,
    movement = [ # broke things up manually
        'A,B,A,C,B,C,B,A,C,B',
        'L,6,R,8,R,12,L,6,L,8',
        'L,10,L,8,R,12',
        'L,8,L,10,L,6,L,6',
        'n'
    ]
    for line in movement:
        line = [ord(c) for c in line]
        line.append(10)
        for i in line:
            comp.inputs.append(i)
    comp.run_program()
    # print(comp.outputs)
    return comp.outputs[-1]

def main():
    puzzle_input = adventofcode.read_input(17)
    puzzle_input = [int(x) for x in puzzle_input.split(',')]
    adventofcode.answer(1, 7780, part1(puzzle_input))
    adventofcode.answer(2, 1075882, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
