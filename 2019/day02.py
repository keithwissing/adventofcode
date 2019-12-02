#!/usr/bin/env python3

import adventofcode

def step(mem, ip):
    if mem[ip] == 1:
        mem[mem[ip+3]] = mem[mem[ip+1]] + mem[mem[ip+2]]
    elif mem[ip] == 2:
        mem[mem[ip+3]] = mem[mem[ip+1]] * mem[mem[ip+2]]
    elif mem[ip] == 99:
        return (False, mem)
    else:
        raise Exception('error')
    return (True, mem)

def runstring(mem):
    """
    >>> runstring('2,4,4,5,99,0')
    [2, 4, 4, 5, 99, 9801]
    """
    mem = [int(x) for x in mem.split(',')]
    run(mem)
    return mem

def run(mem):
    ip = 0
    (con, mem) = step(mem, ip)
    while con:
        ip += 4
        (con, mem) = step(mem, ip)
    return mem

def run_nv(mem, noun, verb):
    mem[1] = noun
    mem[2] = verb
    run(mem)
    return mem[0]

def part1(mem):
    """
    >> part1(0)
    0
    """
    return run_nv(mem, 12, 2)

def part2(mem):
    for n in range(0, 100):
        for v in range(0, 100):
            try:
                r = run_nv(mem[:], n, v)
                if r == 19690720:
                    return n*100+v
            except:
                pass

def main():
    puzzle_input = adventofcode.read_input(2)
    puzzle_input = [int(x) for x in puzzle_input.split(',')]
    adventofcode.answer(1, 5305097, part1(puzzle_input[:]))
    adventofcode.answer(2, 4925, part2(puzzle_input[:]))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
