#!/usr/bin/env python3

from itertools import cycle
import adventofcode
from intcomputer2 import IntComputer

def part1(program):
    comps = []
    queues = [[x, -1, -1] for x in range(50)]
    for x in range(50):
        comps.append(IntComputer(program))
    for x in cycle(range(50)):
        if not queues[x]:
            queues[x].extend([-1]*2)
        # print(queues[x])
        out = comps[x].run_until_outputs_or_no_input(queues[x])
        # print(out)
        if out:
            if out[0] == 255:
                return out[2]
            queues[out[0]].extend(out[1:])

def part2(program):
    comps = []
    queue = [[x, x, -1, -1] for x in range(50)]
    nat = [-1, -1]
    lasty = -2
    for x in range(50):
        comps.append(IntComputer(program))
    while True:
        if not queue:
            if not flag:
                flag = True
                queue = [[x, -1, -1] for x in range(50)]
            else:
                # print(f'NAT insert {nat}, {lasty}')
                queue = [[0]+nat[:]]
                flag = False
                if nat[1] == lasty:
                    return lasty
                lasty = nat[1]
        pro = queue.pop(0)
        x, inp = pro[0], pro[1:]
        # print(f'run {x} q {inp}')
        out = comps[x].run_until_outputs_or_no_input(inp)
        # print(f'out {out}')
        if out:
            flag = False
            if out[0] == 255:
                nat = out[1:]
                # print(f'NAT = {nat}')
            else:
                queue.append(out)

def main():
    puzzle_input = adventofcode.read_input(23)
    puzzle_input = [int(x) for x in puzzle_input.split(',')]
    adventofcode.answer(1, 18982, part1(puzzle_input))
    adventofcode.answer(2, 11088, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
