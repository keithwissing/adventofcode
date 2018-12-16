#!/usr/bin/env python

import adventofcode

all_ops = ['addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori', 'setr', 'seti', 'gtir', 'gtri', 'gtrr', 'eqir', 'eqri', 'eqrr']

def part1(samples):
    """
    >>> part1([([3, 2, 1, 1], [9, 2, 1, 2], [3, 2, 2, 1])])
    1
    """
    total = 0
    for (before, instruction, after) in samples:
        possibles = sum([1 for op in all_ops if after[instruction[3]] == calc(op, before, instruction)])
        if possibles >= 3:
            total += 1
    return total

def part2(samples, program):
    possible = {opc: set(all_ops) for opc in range(16)}

    for (before, instruction, after) in samples:
        for op in all_ops:
            if after[instruction[3]] != calc(op, before, instruction):
                possible[instruction[0]].discard(op)

    reduce_possibles(possible)

    opc2op = {k:list(v)[0] for k, v in possible.iteritems() if len(v) == 1}

    state = [0, 0, 0, 0]
    for instruction in program:
        state[instruction[3]] = calc(opc2op[instruction[0]], state, instruction)
    return state[0]

def reduce_possibles(possible):
    for _ in range(16):
        for k, v in possible.iteritems():
            if len(v) == 1:
                op = list(v)[0]
                for k2, v2 in possible.iteritems():
                    if k != k2:
                        v2.discard(op)

def calc(op, before, instruction):
    if op == 'addr':
        t = before[instruction[1]] + before[instruction[2]]
    elif op == 'addi':
        t = before[instruction[1]] + instruction[2]
    elif op == 'mulr':
        t = before[instruction[1]] * before[instruction[2]]
    elif op == 'muli':
        t = before[instruction[1]] * instruction[2]
    elif op == 'banr':
        t = before[instruction[1]] & before[instruction[2]]
    elif op == 'bani':
        t = before[instruction[1]] & instruction[2]
    elif op == 'borr':
        t = before[instruction[1]] | before[instruction[2]]
    elif op == 'bori':
        t = before[instruction[1]] | instruction[2]
    elif op == 'setr':
        t = before[instruction[1]]
    elif op == 'seti':
        t = instruction[1]
    elif op == 'gtir':
        t = 1 if instruction[1] > before[instruction[2]] else 0
    elif op == 'gtri':
        t = 1 if before[instruction[1]] > instruction[2] else 0
    elif op == 'gtrr':
        t = 1 if before[instruction[1]] > before[instruction[2]] else 0
    elif op == 'eqir':
        t = 1 if instruction[1] == before[instruction[2]] else 0
    elif op == 'eqri':
        t = 1 if before[instruction[1]] == instruction[2] else 0
    elif op == 'eqrr':
        t = 1 if before[instruction[1]] == before[instruction[2]] else 0
    return t

def parse_input(puzzle_input):
    section = 1
    last_was_blank = False
    samples = []
    program = []
    for line in puzzle_input:
        if section == 1:
            if 'Before' in line:
                before = [int(x) for x in line[9:].replace(',', '').replace(']', '').split()]
            if 'After' in line:
                after = [int(x) for x in line[9:].replace(',', '').replace(']', '').split()]
            if len(line.split()) == 4:
                instruction = [int(x) for x in line.split()]
            if line == '':
                if last_was_blank:
                    section = 2
                else:
                    last_was_blank = True
                    samples.append((before, instruction, after))
            else:
                last_was_blank = False
        else:
            if line != '':
                instruction = [int(x) for x in line.split()]
                program.append(instruction)
    return samples, program

def main():
    puzzle_input = adventofcode.read_input(16)
    samples, program = parse_input(puzzle_input)
    adventofcode.answer(1, 651, part1(samples))
    adventofcode.answer(2, 706, part2(samples, program))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
