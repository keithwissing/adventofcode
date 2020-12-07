#!/usr/bin/env python3

import re
import adventofcode

t1 = [
    'light red bags contain 1 bright white bag, 2 muted yellow bags.',
    'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
    'bright white bags contain 1 shiny gold bag.',
    'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
    'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
    'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
    'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
    'faded blue bags contain no other bags.',
    'dotted black bags contain no other bags.',
]

t2 = [
    'shiny gold bags contain 2 dark red bags.',
    'dark red bags contain 2 dark orange bags.',
    'dark orange bags contain 2 dark yellow bags.',
    'dark yellow bags contain 2 dark green bags.',
    'dark green bags contain 2 dark blue bags.',
    'dark blue bags contain 2 dark violet bags.',
    'dark violet bags contain no other bags.',
]

def parse_line(line):
    m = re.match(r'^([\w\s]+) bags contain ([\w\s,]+).$', line)
    outer = m[1]
    i = m[2].replace('bags', '').replace('bag', '')
    if i == 'no other ':
        inner = []
    else:
        inner = [x.strip().split(' ', 1) for x in i.split(',')]
    return outer, inner

def can_contain_shiny_gold(color, rules):
    rule = rules[color]
    if 'shiny gold' in [x[1] for x in rule]:
        return True
    for c in rule:
        if can_contain_shiny_gold(c[1], rules):
            return True
    return False

def part1(lines):
    """
    >>> part1(t1)
    4
    """
    rules = dict(parse_line(l) for l in lines)
    return sum(1 for color in rules if can_contain_shiny_gold(color, rules))

def must_contain(color, rules):
    tot = 0
    for c in rules[color]:
        tot += int(c[0]) * (1 + must_contain(c[1], rules))
    return tot

def part2(lines):
    """
    >>> part2(t1)
    32
    >>> part2(t2)
    126
    """
    rules = dict(parse_line(l) for l in lines)
    return must_contain('shiny gold', rules)

def main():
    puzzle_input = adventofcode.read_input(7)
    adventofcode.answer(1, 278, part1(puzzle_input))
    adventofcode.answer(2, 45157, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
