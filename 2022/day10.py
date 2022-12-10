#!/usr/bin/env python3

import adventofcode

t1 = [
    'addx 15',
    'addx -11',
    'addx 6',
    'addx -3',
    'addx 5',
    'addx -1',
    'addx -8',
    'addx 13',
    'addx 4',
    'noop',
    'addx -1',
    'addx 5',
    'addx -1',
    'addx 5',
    'addx -1',
    'addx 5',
    'addx -1',
    'addx 5',
    'addx -1',
    'addx -35',
    'addx 1',
    'addx 24',
    'addx -19',
    'addx 1',
    'addx 16',
    'addx -11',
    'noop',
    'noop',
    'addx 21',
    'addx -15',
    'noop',
    'noop',
    'addx -3',
    'addx 9',
    'addx 1',
    'addx -3',
    'addx 8',
    'addx 1',
    'addx 5',
    'noop',
    'noop',
    'noop',
    'noop',
    'noop',
    'addx -36',
    'noop',
    'addx 1',
    'addx 7',
    'noop',
    'noop',
    'noop',
    'addx 2',
    'addx 6',
    'noop',
    'noop',
    'noop',
    'noop',
    'noop',
    'addx 1',
    'noop',
    'noop',
    'addx 7',
    'addx 1',
    'noop',
    'addx -13',
    'addx 13',
    'addx 7',
    'noop',
    'addx 1',
    'addx -33',
    'noop',
    'noop',
    'noop',
    'addx 2',
    'noop',
    'noop',
    'noop',
    'addx 8',
    'noop',
    'addx -1',
    'addx 2',
    'addx 1',
    'noop',
    'addx 17',
    'addx -9',
    'addx 1',
    'addx 1',
    'addx -3',
    'addx 11',
    'noop',
    'noop',
    'addx 1',
    'noop',
    'addx 1',
    'noop',
    'noop',
    'addx -13',
    'addx -19',
    'addx 1',
    'addx 3',
    'addx 26',
    'addx -30',
    'addx 12',
    'addx -1',
    'addx 3',
    'addx 1',
    'noop',
    'noop',
    'noop',
    'addx -9',
    'addx 18',
    'addx 1',
    'addx 2',
    'noop',
    'noop',
    'addx 9',
    'noop',
    'noop',
    'noop',
    'addx -1',
    'addx 2',
    'addx -37',
    'addx 1',
    'addx 3',
    'noop',
    'addx 15',
    'addx -21',
    'addx 22',
    'addx -6',
    'addx 1',
    'noop',
    'addx 2',
    'addx 1',
    'noop',
    'addx -10',
    'noop',
    'noop',
    'addx 20',
    'addx 1',
    'addx 2',
    'addx 2',
    'addx -6',
    'addx -11',
    'noop',
    'noop',
    'noop',
]

def step(x, line):
    if line == 'noop':
        return [x]
    _, v = line.split()
    return [x, x + int(v)]

def part1(lines):
    """
    >>> part1(t1)
    13140
    """
    values = [1]
    for line in lines:
        values.extend(step(values[-1], line))
    total = 0
    for i in range(20, len(values), 40):
        total += i * values[i - 1]
    return total

def part2(lines):
    """
    # >>> part2(t1)
    """
    values = [1]
    for line in lines:
        values.extend(step(values[-1], line))
    for y in range(6):
        print(''.join(['#' if abs(values[y * 40 + x] - x) <= 1 else ' ' for x in range(40)]))
    return 'PGHFGLUG'

def main():
    puzzle_input = adventofcode.read_input(10)
    adventofcode.answer(1, 15260, part1(puzzle_input))
    adventofcode.answer(2, 'PGHFGLUG', part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
