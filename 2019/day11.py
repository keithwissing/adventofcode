#!/usr/bin/env python3

from collections import defaultdict
import adventofcode
from intcomputer import IntComputer

def run_bot(program, init_val):
    comp = IntComputer(program)
    panel = defaultdict(lambda: 0)
    botpos = (0, 0)
    botdir = 0
    color = comp.run_until_output(init_val)
    turn = comp.run_until_output()
    while color != -1 and turn != -1:
        panel[botpos] = color
        botdir = (botdir + turn*2 - 1) % 4
        change = {0 : (0, 1), 1 : (1, 0), 2 : (0, -1), 3 : (-1, 0)}[botdir]
        botpos = (botpos[0] + change[0], botpos[1] + change[1])
        color = comp.run_until_output(panel[botpos])
        turn = comp.run_until_output()
    return panel

def part1(program):
    return len(run_bot(program, 0))

def part2(program):
    panel = run_bot(program, 1)
    display_dict_as_grid(panel)
    return 'PGUEHCJH'

def display_dict_as_grid(panel):
    (minX, maxX), (minY, maxY) = [(min(c), max(c)) for c in zip(*panel)]
    for row in range(maxY, minY-1, -1):
        line = [panel[(x, row)] for x in range(minX, maxX+1)]
        line = ['#' if x == 1 else ' ' for x in line]
        print(''.join(line))

def main():
    puzzle_input = adventofcode.read_input(11)
    puzzle_input = [int(x) for x in puzzle_input.split(',')]
    adventofcode.answer(1, 1709, part1(puzzle_input))
    adventofcode.answer(2, 'PGUEHCJH', part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
