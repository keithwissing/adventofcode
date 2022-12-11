#!/usr/bin/env python3
import re
from functools import reduce
from itertools import groupby

import adventofcode

t1 = [
    'Monkey 0:',
    '  Starting items: 79, 98',
    '  Operation: new = old * 19',
    '  Test: divisible by 23',
    '    If true: throw to monkey 2',
    '    If false: throw to monkey 3',
    '',
    'Monkey 1:',
    '  Starting items: 54, 65, 75, 74',
    '  Operation: new = old + 6',
    '  Test: divisible by 19',
    '    If true: throw to monkey 2',
    '    If false: throw to monkey 0',
    '',
    'Monkey 2:',
    '  Starting items: 79, 60, 97',
    '  Operation: new = old * old',
    '  Test: divisible by 13',
    '    If true: throw to monkey 1',
    '    If false: throw to monkey 3',
    '',
    'Monkey 3:',
    '  Starting items: 74',
    '  Operation: new = old + 3',
    '  Test: divisible by 17',
    '    If true: throw to monkey 0',
    '    If false: throw to monkey 1',
]

def split_on_blank_lines(lines):
    yield from [list(sub) for ele, sub in groupby(lines, key=bool) if ele]

class Monkey:
    def __init__(self, lines):
        self.items = [int(x) for x in re.sub(r"[^0-9 ]", "", lines[1]).split()]
        self.operator = lines[2].split()[4]
        self.value = lines[2].split()[5]
        self.test = int(lines[3].split()[3])
        self.throw = [int(lines[4].split()[5]), int(lines[5].split()[5])]
        self.inspections = 0

def parse(lines):
    return list(Monkey(m) for m in split_on_blank_lines(lines))

def run_round(monkeys, relief):
    for m in monkeys:
        m.inspections += len(m.items)
        for item in m.items:
            v = item if m.value == 'old' else int(m.value)
            nv = item + v if m.operator == '+' else item * v
            if relief == 3:
                nv = nv // relief
            else:
                nv = nv % relief
            to = m.throw[0 if nv % m.test == 0 else 1]
            monkeys[to].items.append(nv)
        m.items = []

def print_holding(monkeys):
    for i, m in enumerate(monkeys):
        print(f'Monkey {i}: {m.items}')

def part1(lines):
    """
    >>> part1(t1)
    10605
    """
    monkeys = parse(lines)
    for _ in range(20):
        run_round(monkeys, 3)
    inspections = sorted([m.inspections for m in monkeys])
    return inspections[-1] * inspections[-2]

def part2(lines):
    """
    >>> part2(t1)
    2713310158
    """
    monkeys = parse(lines)
    a = set(m.test for m in monkeys)
    relief = reduce(lambda x, y: x * y, a)
    for r in range(10000):
        run_round(monkeys, relief)
    inspections = sorted([m.inspections for m in monkeys])
    return inspections[-1] * inspections[-2]

def main():
    puzzle_input = adventofcode.read_input(11)
    adventofcode.answer(1, 50172, part1(puzzle_input))
    adventofcode.answer(2, 11614682178, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
