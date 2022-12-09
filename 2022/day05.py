#!/usr/bin/env python3
from itertools import groupby

import adventofcode

t1 = [
    '    [D]    ',
    '[N] [C]    ',
    '[Z] [M] [P]',
    ' 1   2   3 ',
    '',
    'move 1 from 2 to 1',
    'move 3 from 1 to 3',
    'move 2 from 2 to 1',
    'move 1 from 1 to 2',
]

def split_on_blank_lines(lines):
    yield from [list(sub) for ele, sub in groupby(lines, key=bool) if ele]

def parse(lines):
    stacks, moves = split_on_blank_lines(lines)

    n = len(stacks[-1].split())
    crates = [[x.strip() for i, x in enumerate(line) if (i - 1) % 4 == 0] for line in stacks[-2::-1]]
    q = [[r[col] for r in crates if col < len(r) and r[col]] for col in range(n)]

    moves = [x.split() for x in moves]
    moves = [[int(y) for i, y in enumerate(r) if i % 2 == 1] for r in moves]
    return q, moves

def apply(stacks, move):
    src = stacks[move[1] - 1]
    dst = stacks[move[2] - 1]
    for _ in range(move[0]):
        dst.append(src.pop())

def apply_9001(stacks, move):
    src = stacks[move[1] - 1]
    dst = stacks[move[2] - 1]
    dst.extend(src[-move[0]:])
    del src[-move[0]:]

def part1(lines):
    """
    >>> part1(t1)
    'CMZ'
    """
    stacks, moves = parse(lines)
    for move in moves:
        apply(stacks, move)
    return ''.join(s.pop() for s in stacks)

def part2(lines):
    """
    >>> part2(t1)
    'MCD'
    """
    stacks, moves = parse(lines)
    for move in moves:
        apply_9001(stacks, move)
    return ''.join(s.pop() for s in stacks)

def main():
    puzzle_input = adventofcode.read_input(5)
    adventofcode.answer(1, 'FWSHSPJWM', part1(puzzle_input))
    adventofcode.answer(2, 'PWPWHGFZS', part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
