#!/usr/bin/env python3

import adventofcode

t1 = [
    '190: 10 19',
    '3267: 81 40 27',
    '83: 17 5',
    '156: 15 6',
    '7290: 6 8 6 15',
    '161011: 16 10 13',
    '192: 17 8 14',
    '21037: 9 7 18 13',
    '292: 11 6 16 20',
]

def test(line):
    state = 0
    while state & 1 << len(line) - 2 == 0:
        acc = line[1]
        for pos in range(len(line) - 2):
            if state & 1 << pos:
                acc *= line[2 + pos]
            else:
                acc += line[2 + pos]
        if acc == line[0]:
            return True
        state += 1
    return False

def part1(lines):
    """
    >>> part1(t1)
    3749
    """
    rows = [[int(x) for x in l.replace(':', '').split()] for l in lines]
    return sum(row[0] for row in rows if test(row))

def test2(line):
    state = [0] * (len(line) - 2)
    while True:
        acc = line[1]
        for pos in range(len(line) - 2):
            if state[pos] == 0:
                acc += line[2 + pos]
            elif state[pos] == 1:
                acc *= line[2 + pos]
            else:
                acc = int(str(acc) + str(line[2 + pos]))
        if acc == line[0]:
            return True
        for pos in range(len(line) - 2):
            state[pos] = (state[pos] + 1) % 3
            if state[pos] != 0:
                break
        if all(s == 0 for s in state):
            break
    return False

def part2(lines):
    """
    >>> part2(t1)
    11387
    """
    rows = [[int(x) for x in l.replace(':', '').split()] for l in lines]
    return sum(row[0] for row in rows if test2(row))

def main():
    puzzle_input = adventofcode.read_input(7)
    adventofcode.answer(1, 1038838357795, part1(puzzle_input))
    adventofcode.answer(2, 254136560217241, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
