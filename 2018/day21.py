#!/usr/bin/env python

import adventofcode

def part1(ip, program):
    a1, a2 = 0, 0
    state = [0] * 6
    seen, last = set(), 0
    len_program = len(program)
    while 0 <= state[ip] < len_program:
        instruction = program[state[ip]]
        state[instruction[3]] = calc(instruction[0], state, instruction)
        if state[ip] == 28:
            if not seen:
                a1 = state[2]
            if state[2] in seen:
                a2 = last
                break
            seen.add(state[2])
            last = state[2]
        state[ip] += 1
    return a1, a2

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
    puzzle_input = adventofcode.read_input(21)
    ip, program = parse_input(puzzle_input)
    a1, a2 = part1(ip, program)
    adventofcode.answer(1, 12980435, a1)
    adventofcode.answer(2, 14431711, a2)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
