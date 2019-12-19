#!/usr/bin/env python3

from operator import add
from collections import defaultdict
from itertools import product
import adventofcode
from intcomputer import IntComputer

def read_into_grid(comp):
    grid = {}
    pos = (0, 0)
    out = comp.run_until_output()
    while out > 0:
        if out == 10:
            pos = (0, pos[1]+1)
        else:
            grid[pos] = chr(out)
            pos = (pos[0]+1, pos[1])
        out = comp.run_until_output()
    return grid

def part1(program):
    comp = IntComputer(program)
    grid = read_into_grid(comp)
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
    # clockwise, starting up, negative y is up
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
                pos = tuple(map(add, pos, delta))
            steps.append(turn)
            steps.append(str(fwd))
            grid[pos] = 'O'
    print(','.join(steps))
    assert ','.join(steps) == 'L,6,R,8,R,12,L,6,L,8,L,10,L,8,R,12,L,6,R,8,R,12,L,6,L,8,L,8,L,10,L,6,L,6,L,10,L,8,R,12,L,8,L,10,L,6,L,6,L,10,L,8,R,12,L,6,R,8,R,12,L,6,L,8,L,8,L,10,L,6,L,6,L,10,L,8,R,12'
    # display_dict_as_grid(grid)

def find_forward(grid, pos, bd):
    delta = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}[bd]
    tot = 0
    pos = tuple(map(add, pos, delta))
    while grid[pos] == '#':
        tot += 1
        pos = tuple(map(add, pos, delta))
    return tot

def find_turn(grid, pos, bd):
    adj = [grid[p] for p in adjacent(pos)]
    if adj[(bd-1)%4] == '#':
        return 'L'
    if adj[(bd+1)%4] == '#':
        return 'R'
    return ''
    # c = [(3, 1), (0, 2), (1, 3), (2, 0)][bd]
    # return 'L' if adj[c[0]] == '#' else 'R' if adj[c[1]] == '#' else ''

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
        comp.inputs.extend([ord(c) for c in line] + [10])
    out = comp.run_program()
    # print(''.join([chr(x) for x in out[:-1]]))
    return out[-1]

def main():
    puzzle_input = adventofcode.read_input(17)
    puzzle_input = [int(x) for x in puzzle_input.split(',')]
    adventofcode.answer(1, 7780, part1(puzzle_input))
    adventofcode.answer(2, 1075882, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
