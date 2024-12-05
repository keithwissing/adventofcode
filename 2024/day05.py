#!/usr/bin/env python3

import adventofcode

t1 = [
    '47|53',
    '97|13',
    '97|61',
    '97|47',
    '75|29',
    '61|13',
    '75|53',
    '29|13',
    '97|29',
    '53|29',
    '61|53',
    '97|53',
    '61|29',
    '47|13',
    '75|47',
    '97|75',
    '47|61',
    '75|61',
    '47|29',
    '75|13',
    '53|13',
    '',
    '75,47,61,53,29',
    '97,61,53,29,13',
    '75,29,13',
    '75,97,47,61,53',
    '61,13,29',
    '97,13,75,29,47',
]

def parse(lines):
    rules = []
    updates = []
    for line in lines:
        if '|' in line:
            rules.append(tuple(int(x) for x in line.split('|')))
        if ',' in line:
            updates.append(tuple(int(x) for x in line.split(',')))
    return rules, updates

def find(t, v):
    return t.index(v) if v in t else None

def invalid_rule(rules, update):
    for rule in rules:
        pos = tuple(find(update, x) for x in rule)
        if not None in pos and pos[0] >= pos[1]:
            return pos
    return None

def valid_update(rules, update):
    return invalid_rule(rules, update) is None

def fixed_update(rules, update):
    fixed = list(update)
    while bad := invalid_rule(rules, fixed):
        temp = fixed[bad[0]]
        fixed[bad[0]] = fixed[bad[1]]
        fixed[bad[1]] = temp
    return fixed

def part1(lines):
    """
    >>> part1(t1)
    143
    """
    rules, updates = parse(lines)
    total = 0
    for update in updates:
        if valid_update(rules, update):
            total += update[len(update) // 2]
    return total

def part2(lines):
    """
    >>> part2(t1)
    123
    """
    rules, updates = parse(lines)
    total = 0
    for update in updates:
        if not valid_update(rules, update):
            total += fixed_update(rules, update)[len(update) // 2]
    return total

def main():
    puzzle_input = adventofcode.read_input(5)
    adventofcode.answer(1, 4959, part1(puzzle_input))
    adventofcode.answer(2, 4655, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
