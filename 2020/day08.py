#!/usr/bin/env python3

import adventofcode

t1 = [
    'nop +0',
    'acc +1',
    'jmp +4',
    'acc +3',
    'jmp -3',
    'acc -99',
    'acc +1',
    'jmp -4',
    'acc +6',
]

def run(lines):
    ip = 0
    acc = 0
    been = [False] * len(lines)
    while True:
        if ip < 0:
            return (0, False)
        if ip >= len(lines):
            return (acc, True)
        if been[ip]:
            return (acc, False)
        been[ip] = True
        instruction = lines[ip]
        op, arg = instruction[:3], int(instruction[4:])
        if op == 'nop':
            ip += 1
        if op == 'acc':
            ip += 1
            acc += arg
        if op == 'jmp':
            ip += arg

def part1(lines):
    """
    >>> part1(t1)
    5
    """
    acc, _ = run(lines)
    return acc

def part2(lines):
    """
    >>> part2(t1)
    8
    """
    for t, _ in enumerate(lines):
        if lines[t][:3] == 'acc':
            continue
        copy = lines[:]
        if copy[t][:3] == 'nop':
            copy[t] = 'jmp' + copy[t][3:]
        elif copy[t][:3] == 'jmp':
            copy[t] = 'nop' + copy[t][3:]
        acc, completed = run(copy)
        if completed:
            return acc
    raise 'Failed'

def main():
    puzzle_input = adventofcode.read_input(8)
    adventofcode.answer(1, 1744, part1(puzzle_input))
    adventofcode.answer(2, 1174, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
