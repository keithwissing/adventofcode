#!/usr/bin/env python3

from collections import Counter
import adventofcode

t1 = [
    'NNCB',
    '',
    'CH -> B',
    'HH -> N',
    'CB -> H',
    'NH -> C',
    'HB -> C',
    'HC -> B',
    'HN -> C',
    'NN -> C',
    'BH -> H',
    'NC -> B',
    'NB -> B',
    'BN -> B',
    'BB -> N',
    'BC -> B',
    'CC -> N',
    'CN -> C',
]

def parse(lines):
    start = lines[0]
    rules = {}
    for line in lines[2:]:
        p = line.split()
        rules[p[0]] = p[2]
    return start, rules

def iterate(state, rules):
    build = []
    for pos in range(len(state) - 1):
        pair = state[pos:pos + 2]
        if pair in rules:
            v = rules[pair]
            build.extend([state[pos], v])
        else:
            build.append(state[pos])
    build.append(state[-1])
    return ''.join(build)

def part1(lines):
    """
    >>> part1(t1)
    1588
    """
    global rules
    state, rules = parse(lines)
    for _ in range(10):
        state = iterate(state, rules)
    c = Counter(state)
    f = c.most_common()
    return f[0][1] - f[-1][1]

def iterate2(c, rules):
    nc = Counter()
    for pair, v in c.items():
        if pair in rules:
            a = rules[pair]
            nc[pair[0] + a] += v
            nc[a + pair[1]] += v
        else:
            nc[pair] += c[pair]
    return nc

def part2(lines):
    """
    >>> part2(t1)
    2188189693529
    """
    state, rules = parse(lines)
    pairs = [state[p] + state[p + 1] for p in range(len(state) - 1)]
    c = Counter(pairs)
    for _ in range(40):
        c = iterate2(c, rules)
    ic = Counter()
    for k, v in c.items():
        ic[k[0]] += v
        ic[k[1]] += v
    ic[state[0]] += 1
    ic[state[-1]] += 1
    f = ic.most_common()
    return (f[0][1] - f[-1][1]) // 2

def main():
    puzzle_input = adventofcode.read_input(14)
    adventofcode.answer(1, 2937, part1(puzzle_input))
    adventofcode.answer(2, 3390034818249, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
