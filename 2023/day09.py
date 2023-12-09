#!/usr/bin/env python3

import adventofcode

t1 = [
    '0 3 6 9 12 15',
    '1 3 6 10 15 21',
    '10 13 16 21 30 45',
]

def next_in_list(line):
    if all(x == 0 for x in line):
        return 0
    diffs = [line[i + 1] - line[i] for i in range(len(line) - 1)]
    nil = next_in_list(diffs)
    return line[-1] + nil

def find_next(line):
    """
    >>> find_next('0 3 6 9 12 15')
    18
    """
    return next_in_list([int(x) for x in line.split()])

def part1(lines):
    """
    >>> part1(t1)
    114
    """
    return sum(find_next(line) for line in lines)

def prev_in_list(line):
    if all(x == 0 for x in line):
        return 0
    diffs = [line[i + 1] - line[i] for i in range(len(line) - 1)]
    nil = prev_in_list(diffs)
    return line[0] - nil

def part2(lines):
    """
    >>> part2(t1)
    2
    """
    return sum(prev_in_list([int(x) for x in line.split()]) for line in lines)

def main():
    puzzle_input = adventofcode.read_input(9)
    adventofcode.answer(1, 1647269739, part1(puzzle_input))
    adventofcode.answer(2, 864, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
