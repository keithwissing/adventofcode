#!/usr/bin/env python3

import adventofcode

t1 = [
    'kh-tc',
    'qp-kh',
    'de-cg',
    'ka-co',
    'yn-aq',
    'qp-ub',
    'cg-tb',
    'vc-aq',
    'tb-ka',
    'wh-tc',
    'yn-cg',
    'kh-ub',
    'ta-co',
    'de-co',
    'tc-td',
    'tb-wq',
    'wh-td',
    'ta-ka',
    'td-qp',
    'aq-cg',
    'wq-ub',
    'ub-vc',
    'de-ta',
    'wq-aq',
    'wq-vc',
    'wh-yn',
    'ka-de',
    'kh-ta',
    'co-tc',
    'wh-qp',
    'tb-vc',
    'td-yn',
]

def find_connections(lines):
    connections = {}
    for l in lines:
        if l[0] in connections:
            connections[l[0]].add(l[1])
        else:
            connections[l[0]] = {l[1]}
        if l[1] in connections:
            connections[l[1]].add(l[0])
        else:
            connections[l[1]] = {l[0]}
    return connections

def part1(lines):
    """
    >>> part1(t1)
    7
    """
    lines = [l.split('-') for l in lines]
    connections = find_connections(lines)
    computers = set(connections.keys())

    ts = set(c for c in computers if c[0] == 't')

    lans = set()
    for s in ts:
        c1 = connections[s]
        for s2 in c1:
            c2 = connections[s2]
            for s3 in c2:
                if s in connections[s3]:
                    lan = tuple(sorted([s, s2, s3]))
                    lans.add(lan)
    return len(lans)

def part2(lines):
    """
    >>> part2(t1)
    'co,de,ka,ta'
    """
    lines = [l.split('-') for l in lines]
    connections = find_connections(lines)
    computers = set(connections.keys())

    large = set()
    for c in computers:
        party = {c}
        for q in computers:
            if all(q in connections[t] for t in party):
                party.add(q)
        if len(party) > len(large):
            large = party

    return ','.join(sorted(list(large)))

def main():
    puzzle_input = adventofcode.read_input(23)
    adventofcode.answer(1, 1419, part1(puzzle_input))
    adventofcode.answer(2, 'af,aq,ck,ee,fb,it,kg,of,ol,rt,sc,vk,zh', part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
