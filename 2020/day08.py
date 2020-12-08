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
        inst = lines[ip]
        if inst[:3] == 'nop':
            ip += 1
        if inst[:3] == 'acc':
            ip += 1
            acc += int(inst[4:])
        if inst[:3] == 'jmp':
            ip += int(inst[4:])

def part1(lines):
    """
    >>> part1(t1)
    5
    """
    ip = 0
    acc = 0
    been = [False] * len(lines)
    while True:
        if been[ip]:
            break
        been[ip] = True
        inst = lines[ip]
        if inst[:3] == 'nop':
            ip += 1
        if inst[:3] == 'acc':
            ip += 1
            acc += int(inst[4:])
        if inst[:3] == 'jmp':
            ip += int(inst[4:])
    return acc

def part2(lines):
    """
    >>> part2(t1)
    8
    """
    for t in range(0, len(lines)):
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

def main():
    puzzle_input = adventofcode.read_input(8)
    adventofcode.answer(1, 1744, part1(puzzle_input))
    adventofcode.answer(2, 1174, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
