#!/usr/bin/env python3

import math
import re
import adventofcode

t1 = [
    'class: 1-3 or 5-7',
    'row: 6-11 or 33-44',
    'seat: 13-40 or 45-50',
    '',
    'your ticket:',
    '7,1,14',
    '',
    'nearby tickets:',
    '7,3,47',
    '40,4,50',
    '55,2,20',
    '38,6,12',
]

t2 = [
    'class: 0-1 or 4-19',
    'row: 0-5 or 8-19',
    'seat: 0-13 or 16-19',
    '',
    'your ticket:',
    '11,12,13',
    '',
    'nearby tickets:',
    '3,9,18',
    '15,1,5',
    '5,14,9',
]

def parse(lines):
    s = 1
    fields = {}
    near = []
    for line in lines:
        if not line:
            s += 1
        elif s == 1:
            vs = re.match(r'^(.+): (\d+)-(\d+) or (\d+)-(\d+)$', line)
            fields[vs[1]] = ((int(vs[2]), int(vs[3])), (int(vs[4]), int(vs[5])))
        elif s == 2:
            if line[:4] != 'your':
                yours = [int(x) for x in line.split(',')]
        elif s == 3:
            if line[:4] != 'near':
                near.append([int(x) for x in line.split(',')])
    return (fields, yours, near)

def part1(lines):
    """
    >>> part1(t1)
    71
    """
    fields, _, near = parse(lines)
    tot = 0
    for n in near:
        for v in n:
            ok = False
            for f in fields.values():
                if f[0][0] <= v <= f[0][1] or f[1][0] <= v <= f[1][1]:
                    ok = True
            if not ok:
                tot += v
    return tot

def valid_tickets(fields, near):
    for n in near:
        okt = True
        for v in n:
            ok = False
            for f in fields.values():
                if f[0][0] <= v <= f[0][1] or f[1][0] <= v <= f[1][1]:
                    ok = True
            if not ok:
                okt = False
        if okt:
            yield n

def column_possibilities(fields, vts):
    for col in zip(*vts):
        poss = []
        for k, f in fields.items():
            ok = True
            for v in col:
                if not f[0][0] <= v <= f[0][1] and not f[1][0] <= v <= f[1][1]:
                    ok = False
            if ok:
                poss.append(k)
        yield poss

def figure_labels(cps):
    labels = [''] * len(cps)
    while nl := [i for i, v in enumerate(cps) if len(v) == 1]:
        n = nl[0]
        labels[n] = cps[n][0]
        for p in cps:
            if labels[n] in p:
                p.remove(labels[n])
    return labels

def part2(lines, return_labels=False):
    """
    >>> part2(t1, True)
    ['row', 'class', 'seat']
    >>> part2(t2, True)
    ['row', 'class', 'seat']
    """
    fields, yours, near = parse(lines)
    vts = valid_tickets(fields, near)
    cps = list(column_possibilities(fields, vts))
    labels = figure_labels(cps)
    if return_labels:
        return labels
    return math.prod(yours[i] for i, l in enumerate(labels) if l[:9] == 'departure')

def main():
    puzzle_input = adventofcode.read_input(16)
    adventofcode.answer(1, 23954, part1(puzzle_input))
    adventofcode.answer(2, 453459307723, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
