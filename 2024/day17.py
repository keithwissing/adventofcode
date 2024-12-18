#!/usr/bin/env python3

import adventofcode

t1 = [
    'Register A: 729',
    'Register B: 0',
    'Register C: 0',
    '',
    'Program: 0,1,5,4,3,0',
]

def run(a, b, c, program):
    ip = 0
    out = []
    while ip < len(program):
        op = program[ip]
        lit = program[ip + 1]
        comb = lit if lit < 4 else a if lit == 4 else b if lit == 5 else c if lit == 6 else None
        if op == 0:
            a = a // (2 ** comb)
        elif op == 1:
            b = b ^ lit
        elif op == 2:
            b = comb % 8
        elif op == 3:
            if a != 0:
                ip = lit - 2
        elif op == 4:
            b = b ^ c
        elif op == 5:
            out.append(comb % 8)
        elif op == 6:
            b = a // (2 ** comb)
        elif op == 7:
            c = a // (2 ** comb)
        ip += 2
    return out

def part1(lines):
    """
    >>> part1(t1)
    '4,6,3,5,6,3,5,2,1,0'
    """
    a = int(lines[0].split()[2])
    b = int(lines[1].split()[2])
    c = int(lines[2].split()[2])
    program = [int(x) for x in lines[4].split()[1].split(',')]
    out = run(a, b, c, program)
    return ','.join(str(x) for x in out)

def main():
    puzzle_input = adventofcode.read_input(17)
    adventofcode.answer(1, '1,0,2,0,5,7,2,1,3', part1(puzzle_input))
    # adventofcode.answer(2, 0, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
