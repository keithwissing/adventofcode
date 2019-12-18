#!/usr/bin/env python3

from itertools import permutations
import adventofcode
from intcomputer import IntComputer

def try_permutation(program, settings):
    signal = 0
    for phase in settings:
        signal = IntComputer(program, [phase, signal]).run_program()[0]
    return signal

def try_loop_perm(program, settings):
    amps = [IntComputer(program, settings[n]) for n in range(5)]
    ampout = [0 for _ in range(5)]
    signal = 0
    amp = 0
    while -1 not in [amps[n].ip for n in range(5)]:
        signal = amps[amp].run_until_output(amps[amp].inputs + [signal])
        ampout[amp] = signal
        amp = (amp + 1) % 5
    return ampout[4]

def test1(program, perm):
    """
    >>> test1([3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0], [4,3,2,1,0])
    43210
    >>> test1([3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0], [0,1,2,3,4])
    54321
    >>> test1([3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0], [1,0,4,3,2])
    65210
    """
    return try_permutation(program, perm)

def test2(program, perm):
    """
    >>> test2([3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5], [9,8,7,6,5])
    139629729
    >>> test2([3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10], [9,7,8,5,6])
    18216
    """
    return try_loop_perm(program, perm)

def part1(program):
    return max(try_permutation(program, settings) for settings in permutations(range(5)))

def part2(program):
    return max(try_loop_perm(program, settings) for settings in permutations(range(5, 10)))

def main():
    puzzle_input = adventofcode.read_input(7)
    puzzle_input = [int(x) for x in puzzle_input.split(',')]
    adventofcode.answer(1, 30940, part1(puzzle_input))
    adventofcode.answer(2, 76211147, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
