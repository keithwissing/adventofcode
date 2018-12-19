#!/usr/bin/env python

import adventofcode

test_program = [
    ['seti', 5, 0, 1],
    ['seti', 6, 0, 2],
    ['addi', 0, 1, 0],
    ['addr', 1, 2, 3],
    ['setr', 1, 0, 0],
    ['seti', 8, 0, 4],
    ['seti', 9, 0, 5]]

def part1(ip, program):
    """
    #>>> part1(0, test_program)
    7
    """
    state = [0] * 6
    state[0] = 0
    while 0 <= state[ip] < len(program):
        instruction = program[state[ip]]
        state[instruction[3]] = calc(instruction[0], state, instruction)
        state[ip] += 1
    return state[0]

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
    ip = int(puzzle_input[0][4:])
    program = []
    for line in puzzle_input[1:]:
        parts = line.split()
        program.append([parts[0], int(parts[1]), int(parts[2]), int(parts[3])])
    return ip, program

def main():
    puzzle_input = adventofcode.read_input(19)
    ip, program = parse_input(puzzle_input)
    adventofcode.answer(1, 1968, part1(ip, program))
    #adventofcode.answer(2, 0, part2(puzzle_input, 50, 1000000000))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
