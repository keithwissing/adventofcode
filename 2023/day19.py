#!/usr/bin/env python3
from itertools import product
from math import prod
from string import digits

import adventofcode

t1 = [
    'px{a<2006:qkq,m>2090:A,rfg}',
    'pv{a>1716:R,A}',
    'lnx{m>1548:A,A}',
    'rfg{s<537:gd,x>2440:R,A}',
    'qs{s>3448:A,lnx}',
    'qkq{x<1416:A,crn}',
    'crn{x>2662:A,R}',
    'in{s<1351:px,qqz}',
    'qqz{s>2770:qs,m<1801:hdj,R}',
    'gd{a>3333:R,R}',
    'hdj{m>838:A,pv}',
    '',
    '{x=787,m=2655,a=1222,s=2876}',
    '{x=1679,m=44,a=2067,s=496}',
    '{x=2036,m=264,a=79,s=2244}',
    '{x=2461,m=1339,a=466,s=291}',
    '{x=2127,m=1623,a=2188,s=1013}',
]

def parse(lines):
    rules = {}
    parts = []
    section = 0
    for line in lines:
        if not line:
            section += 1
        elif section == 0:
            rn, w = line.replace('{', ' ').replace('}', '').split()
            rl = w.split(',')
            pr = []
            for r in rl:
                if ':' in r:
                    i = 'xmas'.index(r[0])
                    o = r[1]
                    c, d = r[2:].split(':')
                    pr.append((i, o, int(c), d))
                else:
                    pr.append((r,))
            rules[rn] = pr
        elif section == 1:
            line = [c if c in digits else ' ' for c in line]
            line = ''.join(line)
            x, m, a, s = [int(x) for x in line.split()]
            parts.append((x, m, a, s))
    return rules, parts

def flow(rules, part):
    f = 'in'
    while True:
        rl = rules[f]
        for r in rl:
            if len(r) == 1:
                f = r[0]
                break
            else:
                i, o, c, d = r
                v = part[i]
                if o == '<' and v < int(c):
                    f = d
                    break
                if o == '>' and v > int(c):
                    f = d
                    break
        if f == 'A':
            return True
        if f == 'R':
            return False

def part1(lines):
    """
    >>> part1(t1)
    19114
    """
    rules, parts = parse(lines)
    total = 0
    for part in parts:
        if flow(rules, part):
            total += sum(part)
    return total

def part2_infinite_time(rules):
    total = 0
    # Haha! This will run forever
    for x, m, a, s in product(range(1, 4001), range(1, 4001), range(1, 4001), range(1, 4001)):
        if a == 1 and s == 1:
            print((x, m, a, s))
        if flow(rules, (x, m, a, s)):
            total += 1
    return total

def part2(lines):
    """
    # >>> part2(t1)
    167409079868000
    """
    rules, _ = parse(lines)

    bps = [[] for _ in range(4)]
    for rule in rules.values():
        for r in rule:
            if len(r) == 1:
                continue
            bps[r[0]].append(r[2] + (1 if r[1] == '>' else 0))

    bps = [[1] + sorted(i) + [4001] for i in bps]
    # print('\n'.join(str(b) for b in bps))
    # print([len(b) for b in bps])

    # This still checks 7*10^9 parts and takes 3 hours 45 minutes to run, but it does complete eventually

    total = 0
    for xi, x in enumerate(bps[0][:-1]):
        for mi, m in enumerate(bps[1][:-1]):
            for ai, a in enumerate(bps[2][:-1]):
                for si, s in enumerate(bps[3][:-1]):
                    if flow(rules, (x, m, a, s)):
                        bs = prod([(bps[0][xi + 1] - bps[0][xi]),
                                   (bps[1][mi + 1] - bps[1][mi]),
                                   (bps[2][ai + 1] - bps[2][ai]),
                                   (bps[3][si + 1] - bps[3][si])])
                        total += bs
        print(f'({x}, {m}, {a}, {s}) {total = }')  # give us some reassurance that things are still progressing
    return total

def main():
    puzzle_input = adventofcode.read_input(19)
    adventofcode.answer(1, 421983, part1(puzzle_input))
    adventofcode.answer(0, 167409079868000, part2(t1))
    adventofcode.answer(2, 129249871135292, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
