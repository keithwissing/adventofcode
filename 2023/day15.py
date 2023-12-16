#!/usr/bin/env python3
import re

import adventofcode

t1 = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'

def hash(line):
    """
    >>> hash('HASH')
    52
    """
    val = 0
    for c in line:
        val = (val + ord(c)) * 17 % 256
    return val

def part1(lines):
    """
    >>> part1(t1)
    1320
    """
    total = 0
    for i in lines.split(','):
        total += hash(i)
    return total

def part2(lines):
    """
    >>> part2(t1)
    145
    """
    boxes = [[] for _ in range(256)]
    for i in lines.split(','):
        label, op, f = re.fullmatch(r'(\w+)([-=])(\d*)', i).groups()
        bi = hash(label)
        if op == '=':
            found = False
            for li, v in enumerate(boxes[bi]):
                if v[0] == label:
                    v[1] = f
                    found = True
            if not found:
                boxes[bi].append([label, f])
        if op == '-':
            for li, v in enumerate(boxes[bi]):
                if v[0] == label:
                    boxes[bi].pop(li)
    total = 0
    for i, box in enumerate(boxes):
        for li, v in enumerate(box):
            fp = (i + 1) * (li + 1) * int(v[1])
            total += fp
    return total

def main():
    puzzle_input = adventofcode.read_input(15)
    adventofcode.answer(1, 510388, part1(puzzle_input))
    adventofcode.answer(2, 291774, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
