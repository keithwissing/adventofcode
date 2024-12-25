#!/usr/bin/env python3

import adventofcode

t1 = [
    'x00: 1',
    'x01: 1',
    'x02: 1',
    'y00: 0',
    'y01: 1',
    'y02: 0',
    '',
    'x00 AND y00 -> z00',
    'x01 XOR y01 -> z01',
    'x02 OR y02 -> z02',
]

t2 = [
    'x00: 1',
    'x01: 0',
    'x02: 1',
    'x03: 1',
    'x04: 0',
    'y00: 1',
    'y01: 1',
    'y02: 1',
    'y03: 1',
    'y04: 1',
    '',
    'ntg XOR fgs -> mjb',
    'y02 OR x01 -> tnw',
    'kwq OR kpj -> z05',
    'x00 OR x03 -> fst',
    'tgd XOR rvg -> z01',
    'vdt OR tnw -> bfw',
    'bfw AND frj -> z10',
    'ffh OR nrd -> bqk',
    'y00 AND y03 -> djm',
    'y03 OR y00 -> psh',
    'bqk OR frj -> z08',
    'tnw OR fst -> frj',
    'gnj AND tgd -> z11',
    'bfw XOR mjb -> z00',
    'x03 OR x00 -> vdt',
    'gnj AND wpb -> z02',
    'x04 AND y00 -> kjc',
    'djm OR pbm -> qhw',
    'nrd AND vdt -> hwm',
    'kjc AND fst -> rvg',
    'y04 OR y02 -> fgs',
    'y01 AND x02 -> pbm',
    'ntg OR kjc -> kwq',
    'psh XOR fgs -> tgd',
    'qhw XOR tgd -> z09',
    'pbm OR djm -> kpj',
    'x03 XOR y03 -> ffh',
    'x00 XOR y04 -> ntg',
    'bfw OR bqk -> z06',
    'nrd XOR fgs -> wpb',
    'frj XOR qhw -> z04',
    'bqk OR frj -> z07',
    'y03 OR x01 -> nrd',
    'hwm AND bqk -> z03',
    'tgd XOR rvg -> z12',
    'tnw OR pbm -> gnj',
]

def parse(lines):
    values = {}
    gates = []
    for l in lines:
        if ':' in l:
            values[l[:3]] = int(l[4:])
        if '->' in l:
            gates.append(l.replace('->', '').split())
    return values, gates

def part1(lines):
    """
    >>> part1(t1)
    4

    >>> part1(t2)
    2024
    """
    values, gates = parse(lines)

    while gates:
        waiting = []
        for g in gates:
            r1, op, r2, d = g
            if r1 in values and r2 in values:
                if op == 'AND':
                    values[d] = values[r1] & values[r2]
                if op == 'OR':
                    values[d] = values[r1] | values[r2]
                if op == 'XOR':
                    values[d] = values[r1] ^ values[r2]
            else:
                waiting.append(g)
        gates = waiting

    acc = 0
    v = 0
    while True:
        r = f'z{v:02}'
        if r not in values:
            break
        acc |= values[r] << v
        v += 1
    return acc

def part2(lines):
    """
    # >>> part2(t1)
    """

def main():
    puzzle_input = adventofcode.read_input(24)
    adventofcode.answer(1, 47666458872582, part1(puzzle_input))
    # adventofcode.answer(2, 0, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
