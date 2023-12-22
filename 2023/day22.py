#!/usr/bin/env python3
from itertools import product

import adventofcode

t1 = [
    '1,0,1~1,2,1',
    '0,0,2~2,0,2',
    '0,2,3~2,2,3',
    '0,0,4~0,2,4',
    '2,0,5~2,2,5',
    '0,1,6~2,1,6',
    '1,1,8~1,1,9',
]

def parse(lines):
    blocks = []
    for line in lines:
        a, b, c, d, e, f = [int(x) for x in line.replace(',', ' ').replace('~', ' ').split()]
        blocks.append(((a, b, c), (d, e, f)))
    return blocks

def drop(block):
    return set((x, y, z - 1) for x, y, z in block)

def supports(blocks, i):
    s = blocks[i]
    dropped = drop(s)
    if any(z == 0 for _, _, z in dropped):
        return set(p for p in dropped if p[2] == 0)
    others = set(p for j, b in blocks.items() for p in b if j != i)
    return dropped.intersection(others)

def is_supported(blocks, i):
    return len(supports(blocks, i)) > 0

def supported_by(blocks, i):
    s = supports(blocks, i)
    ret = set()
    if any(z == 0 for _, _, z in s):
        ret.add(-1)
    ret.update(set(k for k, v in blocks.items() if k != i and len(s.intersection(v)) > 0))
    return ret

def settle(blocks):
    more = True
    while more:
        more = False
        for i, b in blocks.items():
            while not is_supported(blocks, i):
                blocks[i] = drop(blocks[i])
                more = True
    return blocks

def part1(lines):
    """
    # >>> part1(t1)
    5
    """
    blocks, holds, sup = method_name(lines)
    safe = 0
    for k in blocks.keys():
        if all(len(sup[o]) > 1 for o in holds[k]):
            safe += 1
    return safe

def method_name(lines):
    lines = parse(lines)
    blocks = {}
    for i, block in enumerate(lines):
        o = set((x, y, z) for x, y, z in product(
            range(block[0][0], block[1][0] + 1),
            range(block[0][1], block[1][1] + 1),
            range(block[0][2], block[1][2] + 1),
        ))
        blocks[i] = o
    blocks = settle(blocks)
    sup = {}
    holds = {k: set() for k in blocks.keys()}
    for k in blocks.keys():
        by = supported_by(blocks, k)
        sup[k] = by
        for i in by:
            if i >= 0:
                holds[i].add(k)
    return blocks, holds, sup

def part2(lines):
    """
    >>> part2(t1)
    7
    """
    blocks, holds, sup = method_name(lines)
    total = 0
    for k in blocks.keys():
        s = {k: set(v) for k, v in sup.items()}
        q = [k]
        while q:
            r = q.pop(0)
            for k2, v2 in s.items():
                if r in v2:
                    v2.remove(r)
                    if not v2:
                        q.append(k2)
        total += sum(len(j) == 0 for j in s.values())
    return total

def main():
    puzzle_input = adventofcode.read_input(22)
    # adventofcode.answer(0, 5, part1(t1))
    adventofcode.answer(1, 405, part1(puzzle_input))
    adventofcode.answer(2, 61297, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
