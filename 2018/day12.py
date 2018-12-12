#!/usr/bin/env python

import adventofcode

def part1(state, rules, generations):
    leftmost = 0
    for _ in range(generations):
        state, leftmost = iterate(state, leftmost, rules)
    return sum_of_pots(state, leftmost)

def iterate(state, leftmost, rules):
    state = '....' + state + '....'
    leftmost -= 4
    pots = []
    for p in range(2, len(state)-2):
        pots.append(rules[state[p-2:p+3]])
    leftmost += 2
    first = pots.index('#')
    last = max(loc for loc, val in enumerate(pots) if val == '#')
    pots = pots[first:last+1]
    leftmost += first
    state = ''.join(pots)
    return state, leftmost

def sum_of_pots(state, leftmost):
    total = 0
    for p in state:
        if p == '#':
            total += leftmost
        leftmost += 1
    return total

def part2(state, rules, generations):
    leftmost = 0
    seen = {}
    seen[state] = 0
    for g in xrange(generations):
        state, leftmost = iterate(state, leftmost, rules)
        #print leftmost, state
        if state in seen:
            #print "This state has been seen before"
            #print "At", g+1, "seen at", seen[state]
            loop_found_at = g
            break
        seen[state] = g+1
    # My input resulted in a pattern that moved to the right 1 pot per generation
    leftmost += generations - loop_found_at - 1
    return sum_of_pots(state, leftmost)

def parse(puzzle_input):
    state = puzzle_input[0][15:]
    rules = {}
    for line in puzzle_input[2:]:
        parts = line.split()
        rules[parts[0]] = parts[2]
    return state, rules

def main():
    puzzle_input = adventofcode.read_input(12)
    state, rules = parse(puzzle_input)
    adventofcode.answer(1, 3798, part1(state, rules, 20))
    adventofcode.answer(2, 3900000002212, part2(state, rules, 50000000000))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
