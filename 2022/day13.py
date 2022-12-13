#!/usr/bin/env python3
from functools import cmp_to_key
from itertools import groupby

import adventofcode

t1 = [
    '[1,1,3,1,1]',
    '[1,1,5,1,1]',
    '',
    '[[1],[2,3,4]]',
    '[[1],4]',
    '',
    '[9]',
    '[[8,7,6]]',
    '',
    '[[4,4],4,4]',
    '[[4,4],4,4,4]',
    '',
    '[7,7,7,7]',
    '[7,7,7]',
    '',
    '[]',
    '[3]',
    '',
    '[[[]]]',
    '[[]]',
    '',
    '[1,[2,[3,[4,[5,6,7]]]],8,9]',
    '[1,[2,[3,[4,[5,6,0]]]],8,9]',
]

def split_on_blank_lines(lines):
    yield from [list(sub) for ele, sub in groupby(lines, key=bool) if ele]

def compare(l, r):
    if isinstance(l, int) and isinstance(r, int):
        if int(l) > int(r):
            return False
        if int(l) < int(r):
            return True
        return 'continue'
    if isinstance(l, list) and isinstance(r, list):
        pos = 0
        while True:
            if pos == len(l) and pos == len(r):
                return 'continue'
            if pos >= len(l):
                return True
            if pos >= len(r):
                return False
            c = compare(l[pos], r[pos])
            if c == 'continue':
                pos += 1
            else:
                return c
    if isinstance(l, int):
        l = [l]
    if isinstance(r, int):
        r = [r]
    return compare(l, r)

def correct_order(pair):
    v = [eval(x) for x in pair]
    return compare(v[0], v[1])

def part1(lines):
    """
    >>> part1(t1)
    13
    """
    total = 0
    for i, pair in enumerate(split_on_blank_lines(lines)):
        if correct_order(pair):
            total += i + 1
    return total

def comparer(l, r):
    return -1 if compare(l, r) else 1

def part2(lines):
    """
    >>> part2(t1)
    140
    """
    packets = [[[6]], [[2]]]
    for pair in split_on_blank_lines(lines):
        packets.extend([eval(x) for x in pair])
    packets.sort(key=cmp_to_key(comparer))
    # bubble(packets)
    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)

def bubble(packets):
    cont = True
    while cont:
        cont = False
        for i in range(len(packets) - 1):
            if not compare(packets[i], packets[i + 1]):
                packets[i], packets[i + 1] = packets[i + 1], packets[i]
                cont = True

def main():
    puzzle_input = adventofcode.read_input(13)
    adventofcode.answer(1, 5605, part1(puzzle_input))
    adventofcode.answer(2, 24969, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
