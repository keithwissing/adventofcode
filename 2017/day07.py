#!/usr/bin/env python

import adventofcode

def parse_input_line(line):
    """
    >>> parse_input_line("pbga (66)")
    ('pbga', 66, [])
    >>> parse_input_line("fwft (72) -> ktlj, cntj, xhth")
    ('fwft', 72, ['ktlj', 'cntj', 'xhth'])
    """
    a = line.split(" ")
    name = a[0]
    weight = int(a[1].lstrip("(").rstrip(")"))
    if len(a) > 2:
        c = [x.rstrip(",") for x in a[3:]]
    else:
        c = []
    return (name, weight, c)

def find_bottom(programs):
    non = []
    for x in programs:
        non.extend(x[2])
    uniq = [x for x in [n[0] for n in programs] if not x in non]
    return uniq[0]

def find_incorrect_weight(programs):
    weights = {}
    more = True
    while more:
        more = False
        for p in programs:
            cws = [weights.get(x) for x in p[2]]
            if len(p[2]) == 0:
                weights[p[0]] = p[1]
            elif all(cws):
                weights[p[0]] = p[1] + sum(cws)
            else:
                more = True
    possibles = []
    for p in programs:
        if len(p[2]) > 0:
            bal = [weights[x] for x in p[2]]
            if bal.count(bal[0]) != len(bal):
                ndx = [bal.count(x) for x in bal].index(1)
                bad = bal[ndx]
                good = bal[(ndx+1)%len(bal)]
                tar = next( tp for tp in programs if tp[0] == p[2][ndx] )
                possibles.append( (good, tar[1] - bad + good) )
    low = min( x[0] for x in possibles )
    winner = [x for x in possibles if x[0] == low][0]
    return winner[1]

def main():
    puzzle_input = adventofcode.read_input(7)
    programs = [parse_input_line(x) for x in puzzle_input]
    adventofcode.answer(1, 'hlhomy', find_bottom(programs))
    adventofcode.answer(2, 1505, find_incorrect_weight(programs))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
