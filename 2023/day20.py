#!/usr/bin/env python3
from math import prod

import adventofcode

t1 = [
    'broadcaster -> a, b, c',
    '%a -> b',
    '%b -> c',
    '%c -> inv',
    '&inv -> a',
]

t2 = [
    'broadcaster -> a',
    '%a -> inv, con',
    '&inv -> b',
    '%b -> con',
    '&con -> output',
]

def parse(lines):
    mods = {}
    for line in lines:
        li = line.replace(',', '').split()
        type, name = li[0][0], li[0][1:]
        if type.isalpha():
            type, name = '', li[0]
        mods[name] = (type,) + tuple(li[2:])
    return mods

def init(mods):
    state = {}
    for k, m in mods.items():
        if m[0] == '%':
            state[k] = 0
        if m[0] == '&':
            inputs = {}
            for tk, tv in mods.items():
                if k in tv[1:]:
                    inputs[tk] = 0
            state[k] = inputs
    return state

def push(mods, state, keys=None):
    counts = [0, 0]
    low = ''
    q = [('broadcaster', 0, 'button')]
    while q:
        d, p, f = q.pop(0)
        counts[p] += 1
        if keys and d in keys and p == 0:
            low = d
        m = mods.get(d)
        if m:
            s = state.get(d)
            if m[0] == '':
                for o in m[1:]:
                    q.append((o, p, d))
            if m[0] == '%':
                if p == 0:
                    s = 1 - s
                    state[d] = s
                    for o in m[1:]:
                        q.append((o, s, d))
            if m[0] == '&':
                s[f] = p
                state[d] = s
                for o in m[1:]:
                    q.append((o, 0 if all(v == 1 for v in s.values()) else 1, d))
    return counts, state, low

def part1(lines):
    """
    >>> part1(t1)
    32000000
    >>> part1(t2)
    11687500
    """
    mods = parse(lines)
    state = init(mods)
    totals = [0, 0]
    for _ in range(1000):
        counts, state, _ = push(mods, state)
        totals = [a + b for a, b in zip(counts, totals)]
    return prod(totals)

def digraph(mods):
    # fed this into https://edotor.net
    print('digraph {')
    shapes = {'': 'circle', '%': 'triangle', '&': 'hexagon'}
    for k, v in mods.items():
        print(k, '[shape=', shapes[v[0]], ']')
    for k, v in mods.items():
        print(k, '-> {', ' '.join(v[1:]), '}')
    print('}')

def part2(lines):
    """
    # >>> part2(t1)
    """
    mods = parse(lines)
    state = init(mods)

    # find the node that feeds into rx
    o = [k for k, v in mods.items() if 'rx' in v[1:]]
    # find the list of nodes that feed into that one
    p = [k for k, v in mods.items() if o[0] in v[1:]]

    cycles = {k: 0 for k in p}
    for i in range(10000):
        _, state, low = push(mods, state, cycles.keys())
        if low:
            cycles[low] = i + 1
            p = prod(cycles.values())
            if p:
                return p

def main():
    puzzle_input = adventofcode.read_input(20)
    adventofcode.answer(1, 832957356, part1(puzzle_input))
    adventofcode.answer(2, 240162699605221, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
