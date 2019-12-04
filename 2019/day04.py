#!/usr/bin/env python3

import adventofcode

def meets_rules(val, p2=False):
    """
    >>> meets_rules(111111)
    True
    >>> meets_rules(223450)
    False
    >>> meets_rules(123789)
    False
    >>> meets_rules(112233, True)
    True
    >>> meets_rules(123444, True)
    False
    >>> meets_rules(111122, True)
    True
    """
    strval = str(val)
    has_double = False
    for t in ['11', '22', '33', '44', '55', '66', '77', '88', '99', '00']:
        if t in strval:
            if not p2 or t+t[0] not in strval:
                has_double = True
    if not has_double:
        return False
    for p in range(1, 6):
        if strval[p] < strval[p-1]:
            return False
    return True

# Alternate implementation
def meets_rules_2(val, p2=False):
    strval = str(val)
    doubles = ['11', '22', '33', '44', '55', '66', '77', '88', '99', '00']
    return sum(1 for p in range(1, 6) if strval[p] < strval[p-1]) == 0 \
        and sum(1 for t in doubles if t in strval and (not p2 or t+t[0] not in strval)) > 0

def part1(inp):
    return sum(1 for t in range(inp[0], inp[1]+1) if meets_rules(t))

def part2(inp):
    return sum(1 for t in range(inp[0], inp[1]+1) if meets_rules(t, True))

def main():
    puzzle_input = adventofcode.read_input(4)
    puzzle_input = [int(x) for x in puzzle_input.split('-')]
    adventofcode.answer(1, 1919, part1(puzzle_input))
    adventofcode.answer(2, 1291, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
