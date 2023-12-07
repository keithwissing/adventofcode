#!/usr/bin/env python3
from collections import Counter

import adventofcode

t1 = [
    '32T3K 765',
    'T55J5 684',
    'KK677 28',
    'KTJJT 220',
    'QQQJA 483',
]

order1 = '23456789TJQKA'
order2 = 'J23456789TQKA'

def rank(a):
    counts = Counter(a)
    common = counts.most_common(2)
    if common[0][1] == 5:
        return 7
    if common[0][1] == 4:
        return 6
    if common[0][1] == 3 and common[1][1] == 2:
        return 5
    if common[0][1] == 3:
        return 4
    if common[0][1] == 2 and common[1][1] == 2:
        return 3
    if common[0][1] == 2:
        return 2
    return 1

def rank2(a):
    if 'J' in a:
        return max(rank2(a.replace('J', x, 1)) for x in order2 if x != 'J')
    return rank(a)

def strength(a, rf, order):
    return tuple([rf(a)] + [order.index(x) for x in a])

def calculate(lines, rf, order):
    hands = []
    for line in lines:
        a, b = line.split()
        hands.append((strength(a, rf, order), int(b), a))
    hands.sort()
    # print('\n'.join(str(x) for x in hands))
    winnings = 0
    for i, hand in enumerate(hands):
        winnings += (i + 1) * hand[1]
    return winnings

def part1(lines):
    """
    >>> part1(t1)
    6440
    """
    return calculate(lines, rank, order1)

def part2(lines):
    """
    >>> part2(t1)
    5905
    """
    return calculate(lines, rank2, order2)

def main():
    puzzle_input = adventofcode.read_input(7)
    adventofcode.answer(1, 248105065, part1(puzzle_input))
    adventofcode.answer(2, 249515436, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
