#!/usr/bin/env python3

import adventofcode

t1 = [
    'root: pppw + sjmn',
    'dbpl: 5',
    'cczh: sllz + lgvd',
    'zczc: 2',
    'ptdq: humn - dvpt',
    'dvpt: 3',
    'lfqf: 4',
    'humn: 5',
    'ljgn: 2',
    'sjmn: drzm * dbpl',
    'sllz: 4',
    'pppw: cczh / lfqf',
    'lgvd: ljgn * ptdq',
    'drzm: hmdt - zczc',
    'hmdt: 32',
]

def parse(lines):
    monkeys = {}
    for line in lines:
        a, b = line.split(':')
        monkeys[a] = b.strip()
    for k, v in monkeys.items():
        if isinstance(v, str) and v.isdigit():
            monkeys[k] = int(v)
    return monkeys

def part1(lines):
    """
    >>> part1(t1)
    152
    """
    monkeys = parse(lines)
    while isinstance(monkeys['root'], str):
        for k, v in monkeys.items():
            if isinstance(v, str):
                i = v.split()
                a = monkeys[i[0]]
                b = monkeys[i[2]]
                if isinstance(a, int) and isinstance(b, int):
                    c = eval(str(a) + i[1] + str(b))
                    monkeys[k] = int(c)

    return monkeys['root']

def part2(lines):
    """
    >>> part2(t1)
    301
    """
    monkeys = parse(lines)
    monkeys['humn'] = 'humn ? humn'

    t = monkeys['root'].split()
    monkeys['root'] = f'{t[0]} = {t[2]}'

    forward(monkeys)

    vals = {}
    t = monkeys['root'].split()
    if isinstance(monkeys[t[0]], int):
        vals[t[2]] = monkeys[t[0]]
    if isinstance(monkeys[t[2]], int):
        vals[t[0]] = monkeys[t[2]]

    while 'humn' not in vals:
        for k, v in vals.copy().items():
            t = monkeys[k].split()
            for x in [0, 2]:
                if isinstance(monkeys[t[x]], int):
                    t[x] = monkeys[t[x]]
                if t[x] in vals:
                    t[x] = vals[t[x]]
            if isinstance(t[0], str) and t[1] == '/':
                vals[t[0]] = v * t[2]
            if isinstance(t[2], str) and t[1] == '/':
                vals[t[2]] = t[0] // v
            if isinstance(t[0], str) and t[1] == '+':
                vals[t[0]] = v - t[2]
            if isinstance(t[2], str) and t[1] == '+':
                vals[t[2]] = v - t[0]
            if isinstance(t[0], str) and t[1] == '*':
                vals[t[0]] = v // t[2]
            if isinstance(t[2], str) and t[1] == '*':
                vals[t[2]] = v // t[0]
            if isinstance(t[0], str) and t[1] == '-':
                vals[t[0]] = v + t[2]
            if isinstance(t[2], str) and t[1] == '-':
                vals[t[2]] = t[0] - v

    return vals['humn']

def forward(monkeys):
    more = True
    while more:
        more = False
        for k, v in monkeys.items():
            if isinstance(v, str):
                i = v.split()
                a = monkeys[i[0]]
                b = monkeys[i[2]]
                if isinstance(a, int) and isinstance(b, int):
                    c = eval(str(a) + i[1] + str(b))
                    monkeys[k] = int(c)
                    more = True

def main():
    puzzle_input = adventofcode.read_input(21)
    adventofcode.answer(1, 56490240862410, part1(puzzle_input))
    adventofcode.answer(2, 3403989691757, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
