#!/usr/bin/env python

import re

def find_bot_with_two_values(values):
    bots = [x for x in values.itervalues()]
    bots.sort()
    for pos in range(1,len(bots)):
        if bots[pos] == bots[pos-1]:
            return bots[pos]
    return -1

def part1(puzzle_input):
    """
    >>> part1([ "value 5 goes to bot 2", "bot 2 gives low to bot 1 and high to bot 0", "value 3 goes to bot 1", "bot 1 gives low to output 1 and high to bot 0", "bot 0 gives low to output 2 and high to output 0", "value 2 goes to bot 2" ])
    {0: 5, 1: 2, 2: 3}
    """
    inputs = []
    rules = []
    bots = {}
    outputs = {}
    values = {}

    in_pat = re.compile("value (\d+) goes to bot (\d+)")
    in_rule = re.compile("bot (\d+) gives low to (.+) (\d+) and high to (.+) (\d+)")

    for row in puzzle_input:
        if row.startswith("value"):
            inputs.append(in_pat.findall(row)[0])
        if row.startswith("bot"):
            rules.append(in_rule.findall(row)[0])
    inputs = [(int(a),int(b)) for a,b in inputs]
    rules = [(int(a),b,int(c),d,int(e)) for a,b,c,d,e in rules]
    for inp in inputs:
        values.update({inp[0]: inp[1]})
    while True:
        next_bot = find_bot_with_two_values(values)
        if next_bot == -1:
            break
        rule = next(x for x in rules if x[0] == next_bot)
        bot_has = [x[0] for x in values.iteritems() if x[1] == next_bot]
        bot_has.sort()
        if bot_has == [17,61]:
            print next_bot
        if rule[1] == 'bot':
            values[bot_has[0]] = rule[2]
        else:
            outputs.update({rule[2]: bot_has[0]})
            del values[bot_has[0]]

        if rule[3] == 'bot':
            values[bot_has[1]] = rule[4]
        else:
            outputs.update({rule[4]: bot_has[1]})
            del values[bot_has[1]]
    return outputs

def main():
    puzzle_input = [line.rstrip('\n') for line in open("day10_input.txt")]
    print "Part 1 Answer",
    out = part1(puzzle_input)
    print "Part 2 Answer", out[0] * out[1] * out[2]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()

