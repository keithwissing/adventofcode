#!/usr/bin/env python

import sys
import adventofcode

def part1(puzzle_input):
    """
    >>> part1("dabAcCaCBAcCcaDA")
    10
    """
    current = ""
    next = puzzle_input
    while current != next:
        current = next
        next = process_reactions(current)
    return len(current)

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
    while x < len(current):
        a = current[x]
        b = current[x+1] if x < len(current)-1 else '0'
        if a != b and a.upper() == b.upper():
            x += 2
        else:
            out.append(a)
            x += 1
    return out

def fully_react_list(puzzle_input):
    current = []
    next = puzzle_input
    while len(current) != len(next):
        current = next
        next = process_reactions_list(current)
    return current

def part2(puzzle_input):
    """
    >>> part2("dabAcCaCBAcCcaDA")
    4
    """
    aslist = list(puzzle_input)
    letters = set(aslist)
    letters = set([x.upper() for x in letters])
    best = sys.maxint
    for tor in letters:
        attemp = puzzle_input.replace(tor, '').replace(tor.lower(), "")
        current = fully_react_list(list(attemp))
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
