#!/usr/bin/env python3

from collections import defaultdict
from random import randint, seed
from heapq import heappush, heappop
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
    grid = defaultdict(lambda: ' ')
    o2pos = explore_to_o2(grid, program)
    # display_dict_as_grid(grid)
    dist = find_distance(grid)
    return dist[o2pos]

def part2(program):
    ship = Ship(program)
    while not ship.o2pos:
        ship.explore_left()
        # print('--', ship.count_of_unknown())
        # ship.diplay_grid()
    un = ship.count_of_unknown()
    while un > 0:
        ship.explore_left()
        un = ship.count_of_unknown()
        # print(f'-- {un}')
        # ship.diplay_grid()
    dist = find_distance(ship.grid, ship.o2pos)
    return max(dist.values())

class Ship:
    def __init__(self, program):
        self.program = program
        self.grid = defaultdict(lambda: ' ', {(0, 0):'.'})
        self.botpos = (0, 0)
        self.o2pos = None
        self.comp = IntComputer(program)
        self.dd = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}

    def run_step(self, d):
        pos = self.botpos
        out = self.comp.run_until_output(d)
        delta = self.dd[d]
        np = (pos[0]+delta[0], pos[1]+delta[1])
        self.grid[np] = {0:'#', 1:'.', 2:'.'}[out]
        if out == 2:
            self.o2pos = np
        if out in [1, 2]:
            self.botpos = np
        return out

    def count_of_unknown(self):
        count = 0
        for k, v in self.grid.items():
            if v == '.':
                adj = [self.grid[a] for a in adjacent(k) if a in self.grid]
                if len(adj) < 4 or ' ' in adj:
                    count += 1
        return count

    def diplay_grid(self):
        m1, m3 = self.grid[self.botpos], self.grid[(0, 0)]
        m2 = self.grid[self.o2pos] if self.o2pos else None
        self.grid[self.botpos] = 'B'
        self.grid[(0, 0)] = '@'
        if self.o2pos:
            self.grid[self.o2pos] = 'O'
        display_dict_as_grid(self.grid)
        self.grid[self.botpos] = m1
        self.grid[(0, 0)] = m3
        if m2:
            self.grid[self.o2pos] = m2

    def explore_randomly(self, howlong=1000):
        d = randint(1, 4)
        for _ in range(howlong):
            out = self.run_step(d)
            if out == 0:
                d = randint(1, 4)
            if out in [1, 2]:
                if randint(1, 5) == 1:
                    d = randint(1, 4)

    def explore_2(self, howlong=1000):
        d = randint(1, 4)
        for _ in range(howlong):
            out = self.run_step(d)
            if out == 0:
                d = (d + randint(0, 1) * 2 - 2) % 4 + 1

    def explore_left(self, howlong=1000):
        d = randint(1, 4)
        for _ in range(howlong):
            out = self.run_step(d)
            if out == 0:
                d = right[d]
            else:
                d = left[d]

# 1 = North
# 2 = South
# 3 = West
# 4 = East

left = {1:3, 2:4, 3:2, 4:1}
right = {1:4, 2:3, 3:1, 4:2}

def explore_to_o2(grid, program):
    comp = IntComputer(program)
    dd = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}
    pos = (0, 0)
    d = randint(1, 4)
    # for _ in range(100000):
    while True:
        out = comp.run_until_output(d)
        delta = dd[d]
        np = (pos[0]+delta[0], pos[1]+delta[1])
        if out == 0:
            grid[np] = '#'
            d = randint(1, 4)
        if out == 1:
            grid[np] = '.'
            pos = np
            if randint(1, 5) == 1:
                d = randint(1, 4)
        if out == 2:
            grid[np] = '&'
            pos = np
            o2pos = pos
            # print(f'=== Found at {pos} ===')
            break
    grid[(0, 0)] = 'B'
    return o2pos

def adjacent(pos):
    for d in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        yield (pos[0]+d[0], pos[1]+d[1])

def find_distance(grid, start=(0, 0)):
    pop = start
    dist = {pop: 0}
    heap = []
    for a in adjacent(pop):
        heappush(heap, a)
    while heap:
        pop = heappop(heap)
        if pop in grid and grid[pop] in ['.', '&', 'B']:
            mad = min(dist[a] for a in adjacent(pop) if a in dist and a in grid and grid[a] in ['.', '&', 'B'])
            if pop not in dist or mad + 1 < dist[pop]:
                dist[pop] = mad + 1
                for a in adjacent(pop):
                    heappush(heap, a)
    return dist

def display_dict_as_grid(panel):
    (minX, maxX), (minY, maxY) = [(min(c), max(c)) for c in zip(*panel)]
    for row in range(minY, maxY+1):
        line = [panel[(x, row)] for x in range(minX, maxX+1)]
        print(''.join(line))

def main():
    seed(100)
    puzzle_input = adventofcode.read_input(15)
    puzzle_input = [int(x) for x in puzzle_input.split(',')]
    adventofcode.answer(1, 296, part1(puzzle_input))
    adventofcode.answer(2, 302, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
