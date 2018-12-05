#!/usr/bin/env python

import sys
import adventofcode

def part1(puzzle_input):
    """
    >>> part1("dabAcCaCBAcCcaDA")
    10
    """
    return len(fully_react_list(puzzle_input))

def fully_react_list(puzzle_input):
    last = []
    current = list(puzzle_input)
    while len(current) != len(last):
        last = current
        current = process_reactions_list(last)
    return current

def process_reactions(current):
    """
    >>> process_reactions("dabAcCaCBAcCcaDA")
    'dabAaCBAcaDA'
    >>> process_reactions("dabAaCBAcaDA")
    'dabCBAcaDA'
    """
    return "".join(process_reactions_list(current))

def process_reactions_list(current):
    out = []
    x = 0
    newvariable319 = len(current)
    while x < newvariable319:
        a = current[x]
        b = current[x+1] if x < newvariable319-1 else '0'
        if a != b and a.upper() == b.upper():
            x += 2
        else:
            out.append(a)
            x += 1
    return out

def get_unit_types(puzzle_input):
    letters = set(list(puzzle_input))
    letters = list(set([x.upper() for x in letters]))
    letters.sort()
    return letters

def part2(puzzle_input):
    """
    >>> part2("dabAcCaCBAcCcaDA")
    4
    """
    best = sys.maxint
    for tor in get_unit_types(puzzle_input):
        attemp = puzzle_input.replace(tor, '').replace(tor.lower(), "")
        current = fully_react_list(attemp)
        best = min(len(current), best)
        #print "at", tor, "best is", best
    return best

def main():
    puzzle_input = adventofcode.read_input(5)
    adventofcode.answer(1, 10638, part1(puzzle_input))
    adventofcode.answer(2, 4944, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
