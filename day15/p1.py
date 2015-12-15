#!/usr/bin/env python

import itertools

def dumb_parse(line):
    """
    >>> dumb_parse("Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8")
    [-1, -2, 6, 3]
    """
    words = line.split()
    return [int(words[x][:-1]) for x in [2, 4, 6, 8]]

def just_calories(line):
    words = line.split()
    return int(words[10])

def meal_replacement(lines):
    """
    >>> meal_replacement([\
            "Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8",\
            "Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"])
    (62842880, 57600000)
    """
    mscore = 0
    p2score = 0
    values = [dumb_parse(x) for x in lines]
    calories = [just_calories(x) for x in lines]
    for amounts in itertools.product(range(0, 101), repeat=len(values)):
        if sum(amounts) != 100:
            continue
        #s1 = map(lambda a, b: a*b, values, amounts)
        c = max(0, sum([amounts[x] * values[x][0] for x in range(0, len(amounts))]))
        d = max(0, sum([amounts[x] * values[x][1] for x in range(0, len(amounts))]))
        f = max(0, sum([amounts[x] * values[x][2] for x in range(0, len(amounts))]))
        t = max(0, sum([amounts[x] * values[x][3] for x in range(0, len(amounts))]))
        total = c*d*f*t
        mscore = max(mscore, total)
        tcal = sum([amounts[x] * calories[x] for x in range(0, len(amounts))])
        if tcal == 500:
            p2score = max(p2score, total)
    return (mscore, p2score)

def main():
    puzzle_input = [line.strip() for line in open('input.txt')]
    results = meal_replacement(puzzle_input)
    print results[0]
    print results[1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()

