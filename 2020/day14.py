#!/usr/bin/env python3

import re
import adventofcode

t1 = [
    'mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X',
    'mem[8] = 11',
    'mem[7] = 101',
    'mem[8] = 0',
]

def apply_mask(val, mask):
    """
    >>> apply_mask(11, 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X')
    73
    >>> apply_mask(101, 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X')
    101
    >>> apply_mask(0, 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X')
    64
    """
    am = int(mask.replace('X', '1'), 2)
    om = int(mask.replace('X', '0'), 2)
    return val & am | om

def part1(lines):
    """
    >>> part1(t1)
    165
    """
    mem = {}
    for line in lines:
        if line[:4] == 'mask':
            mask = line[7:]
        if line[:3] == 'mem':
            p = re.match(r'mem\[(\d+)\] = (\d+)', line)
            addr = int(p[1])
            val = int(p[2])
            mem[addr] = apply_mask(val, mask)
    return sum(mem.values())

t2 = [
    'mask = 000000000000000000000000000000X1001X',
    'mem[42] = 100',
    'mask = 00000000000000000000000000000000X0XX',
    'mem[26] = 1',
]

def addresses(addr, mask):
    """
    >>> list(addresses(0, 'X1X1'))
    [5, 7, 13, 15]
    """
    ainb = str(bin(addr)[2:]).zfill(36)
    c = [a if m == '0' else m for m, a in zip(mask, ainb)]
    xs = [i for i, x in enumerate(c) if x == 'X']
    xs.reverse() # technically doesn't matter but it feels better
    for perm in range(0, 2 ** len(xs)):
        for e, idx in enumerate(xs):
            c[idx] = '1' if 2 ** e & perm else '0'
        yield int(''.join(c), 2)

def part2(lines):
    """
    >>> part2(t2)
    208
    """
    mem = {}
    for line in lines:
        if line[:4] == 'mask':
            mask = line[7:]
        if line[:3] == 'mem':
            p = re.match(r'mem\[(\d+)\] = (\d+)', line)
            addr = int(p[1])
            val = int(p[2])
            for c in addresses(addr, mask):
                mem[c] = val
    return sum(mem.values())

def main():
    puzzle_input = adventofcode.read_input(14)
    adventofcode.answer(1, 7611244640053, part1(puzzle_input))
    adventofcode.answer(2, 3705162613854, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
