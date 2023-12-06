#!/usr/bin/env python3

import adventofcode

t1 = [
    'Time:      7  15   30',
    'Distance:  9  40  200',
]

def parse(lines):
    l = [[int(x) for x in y.split()[1:]] for y in lines]
    return zip(l[0], l[1])

def part1(lines):
    """
    >>> part1(t1)
    288
    """
    races = list(parse(lines))
    ret = 1
    for race in races:
        won = 0
        for hold in range(1, race[0]):
            if hold * (race[0] - hold) > race[1]:
                won += 1
        ret *= won
    return ret

def part2(lines):
    """
    >>> part2(t1)
    71503
    """
    l = [[x for x in y if x.isdigit()] for y in lines]
    race = [int(''.join(x)) for x in l]
    won = 0
    for hold in range(1, race[0]):
        if hold * (race[0] - hold) > race[1]:
            won += 1
    return won

def main():
    puzzle_input = adventofcode.read_input(6)
    adventofcode.answer(1, 440000, part1(puzzle_input))
    adventofcode.answer(2, 26187338, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
