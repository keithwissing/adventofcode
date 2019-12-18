#!/usr/bin/env python3

from collections import defaultdict, Counter
import adventofcode
from intcomputer import IntComputer

def part1(program):
    comp = IntComputer(program)
    out = comp.run_until_outputs()
    grid = defaultdict(lambda: 0)
    while len(out) == 3:
        x, y, tid = out
        grid[(x, y)] = tid
        out = comp.run_until_outputs()
    c = Counter(grid.values())
    return c[2]

def part2(program):
    program = program[:]
    program[0] = 2
    comp = IntComputer(program)
    grid = defaultdict(lambda: 0)
    ball, paddle = None, None
    score = 0
    out = comp.run_until_outputs(0)
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
        out = comp.run_until_outputs(v)
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
