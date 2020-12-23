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

t2 = [
    'Player 1:',
    '43',
    '19',
    '',
    'Player 2:',
    '2',
    '29',
    '14',
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

prev_wins = {}

def recursive(decks, level=0):
    tcards = '|'.join([','.join([str(x) for x in d]) for d in decks])
    if tcards in prev_wins:
        return prev_wins[tcards], []
    prev = set()
    r = 0
    while len(decks[0]) > 0 and len(decks[1]) > 0:
        r += 1
        # print(f'l {level} round {r} {decks}')
        cards = '|'.join([','.join([str(x) for x in d]) for d in decks])
        if cards in prev:
            prev_wins[tcards] = 0
            return (0, decks[0])
        prev.add(cards)
        c = [decks[x].pop(0) for x in [0, 1]]
        if len(decks[0]) >= c[0] and len(decks[1]) >= c[1]:
            winner, _ = recursive([decks[0][:c[0]], decks[1][:c[1]]], level + 1)
        else:
            winner = c.index(max(c))
        decks[winner].append(c[winner])
        decks[winner].append(c[1 - winner])
    twin = 0 if decks[0] else 1
    prev_wins[tcards] = twin
    return (twin, decks[0] if twin == 0 else decks[1])

def part2(lines):
    """
    >>> part2(t1)
    291
    >>> part2(t2)
    105
    """
    decks = parse(lines)
    _, d = recursive(decks)
    return sum((i + 1) * c for i, c in enumerate(d[::-1]))

def main():
    puzzle_input = adventofcode.read_input(22)
    adventofcode.answer(1, 34255, part1(puzzle_input))
    adventofcode.answer(2, 33369, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
