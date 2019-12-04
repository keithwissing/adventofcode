#!/usr/bin/env python3

import adventofcode

def meets_rules(val):
    """
    >>> meets_rules(111111)
    True
    >>> meets_rules(223450)
    False
    >>> meets_rules(123789)
    False
    """
    if val < 111111 or val > 999999:
        return False
    strval = str(val)
    has_double = False
    for t in ['11', '22', '33', '44', '55', '66', '77', '88', '99', '00']:
        if t in strval:
            has_double = True
    if not has_double:
        return False
    for p in range(1, 6):
        if int(strval[p]) < int(strval[p-1]):
            return False
    return True

def meets_rules2(val):
    """
    >>> meets_rules2(112233)
    True
    >>> meets_rules2(123444)
    False
    >>> meets_rules2(111122)
    True
    """
    if val < 111111 or val > 999999:
        return False
    strval = str(val)
    has_double = False
    for t in ['11', '22', '33', '44', '55', '66', '77', '88', '99', '00']:
        if t in strval:
            if t+t[0] not in strval:
                has_double = True
    if not has_double:
        return False
    for p in range(1, 6):
        if int(strval[p]) < int(strval[p-1]):
            return False
    return True

def part1(inp):
    return sum(1 for t in range(inp[0], inp[1]+1) if meets_rules(t))

def part2(inp):
    return sum(1 for t in range(inp[0], inp[1]+1) if meets_rules2(t))

def main():
    puzzle_input = adventofcode.read_input(4)
    puzzle_input = [int(x) for x in puzzle_input.split('-')]
    adventofcode.answer(1, 1919, part1(puzzle_input))
    adventofcode.answer(2, 1291, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()