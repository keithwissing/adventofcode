#!/usr/bin/env python3

import re
import adventofcode

t1 = [
    '0: 4 1 5',
    '1: 2 3 | 3 2',
    '2: 4 4 | 5 5',
    '3: 4 5 | 5 4',
    '4: "a"',
    '5: "b"',
    '',
    'ababbb',
    'bababa',
    'abbbab',
    'aaabbb',
    'aaaabbb',
]

t2 = [
    '42: 9 14 | 10 1',
    '9: 14 27 | 1 26',
    '10: 23 14 | 28 1',
    '1: "a"',
    '11: 42 31',
    '5: 1 14 | 15 1',
    '19: 14 1 | 14 14',
    '12: 24 14 | 19 1',
    '16: 15 1 | 14 14',
    '31: 14 17 | 1 13',
    '6: 14 14 | 1 14',
    '2: 1 24 | 14 4',
    '0: 8 11',
    '13: 14 3 | 1 12',
    '15: 1 | 14',
    '17: 14 2 | 1 7',
    '23: 25 1 | 22 14',
    '28: 16 1',
    '4: 1 1',
    '20: 14 14 | 1 15',
    '3: 5 14 | 16 1',
    '27: 1 6 | 14 18',
    '14: "b"',
    '21: 14 1 | 1 14',
    '25: 1 1 | 1 14',
    '22: 14 14',
    '8: 42',
    '26: 14 22 | 1 20',
    '18: 15 15',
    '7: 14 5 | 1 21',
    '24: 14 1',
    '',
    'abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa',
    'bbabbbbaabaabba',
    'babbbbaabbbbbabbbbbbaabaaabaaa',
    'aaabbbbbbaaaabaababaabababbabaaabbababababaaa',
    'bbbbbbbaaaabbbbaaabbabaaa',
    'bbbababbbbaaaaaaaabbababaaababaabab',
    'ababaaaaaabaaab',
    'ababaaaaabbbaba',
    'baabbaaaabbaaaababbaababb',
    'abbbbabbbbaaaababbbbbbaaaababb',
    'aaaaabbaabaaaaababaa',
    'aaaabbaaaabbaaa',
    'aaaabbaabbaaaaaaabbbabbbaaabbaabaaa',
    'babaaabbbaaabaababbaabababaaab',
    'aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba',
]

def parse(lines):
    rules = {}
    messages = []
    s = 1
    for line in lines:
        if not line:
            s += 1
        elif s == 1:
            ps = line.split(':')
            rules[int(ps[0])] = ps[1].strip()
        elif s == 2:
            messages.append(line)
    return rules, messages

def rules_to_re(rules):
    expr = {}
    lc = -1
    while len(expr) > lc:
        lc = len(expr)
        for k, v in rules.items():
            if k in expr:
                continue
            if v[0] == '"':
                expr[k] = v[1]
            elif sum(1 for x in v.replace('|', ' ').split() if int(x) not in expr) == 0:
                b = ['|' if x == '|' else f'({expr[int(x)]})' for x in v.split()]
                expr[k] = ''.join(b)
    return expr

def part1(lines):
    """
    >>> part1(t1)
    2
    >>> part1(t2)
    3
    """
    rules, messages = parse(lines)
    exp = '^' + rules_to_re(rules)[0] + '$'
    return sum(1 for m in messages if re.match(exp, m) is not None)

def part2(lines):
    """
    >>> part2(t2)
    12
    """
    rules, messages = parse(lines)

    rules[8] = '42 | 42 8'
    rules[11] = '42 31 | 42 11 31'
    res = rules_to_re(rules)

    aa = set()
    for x in range(1, 6):
        e = f'^({res[42]}){{' + str(x + 1) + f',}}({res[31]}){{' + str(x) + '}$'
        a = {i for i, m in enumerate(messages) if re.match(e, m) is not None}
        aa |= a
    return len(aa)

def main():
    puzzle_input = adventofcode.read_input(19)
    adventofcode.answer(1, 156, part1(puzzle_input))
    adventofcode.answer(2, 363, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
