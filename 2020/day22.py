#!/usr/bin/env python3

import adventofcode

t1 = [
    'Player 1:',
    '9',
    '2',
    '6',
    '3',
    '1',
    '',
    'Player 2:',
    '5',
    '8',
    '4',
    '7',
    '10',
]

def parse(lines):
    decks = [[], []]
    s = 0
    for line in lines:
        if not line:
            s += 1
        elif line[0] != 'P':
            decks[s].append(int(line))
    return decks

def iterate(decks):
    c0 = decks[0].pop(0)
    c1 = decks[1].pop(0)
    if c0 > c1:
        decks[0].append(max(c0, c1))
        decks[0].append(min(c0, c1))
    if c1 > c0:
        decks[1].append(max(c0, c1))
        decks[1].append(min(c0, c1))

def part1(lines):
    """
    >>> part1(t1)
    306
    """
    decks = parse(lines)
    while len(decks[0]) != 0 and len(decks[1]) != 0:
        iterate(decks)
    winner = 0 if decks[0] else 1
    t = decks[winner][::-1]
    return sum((i + 1) * c for i, c in enumerate(t))

def main():
    puzzle_input = adventofcode.read_input(22)
    adventofcode.answer(1, 34255, part1(puzzle_input))
    # adventofcode.answer(2, 0, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
