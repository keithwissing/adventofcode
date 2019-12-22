#!/usr/bin/env python3

import adventofcode

testdata1 = [
    'deal with increment 7',
    'deal into new stack',
    'deal into new stack'
]

testdata2 = [
    'cut 6',
    'deal with increment 7',
    'deal into new stack'
]

testdata3 = [
    'deal with increment 7',
    'deal with increment 9',
    'cut -2'
]

testdata4 = [
    'deal into new stack',
    'cut -2',
    'deal with increment 7',
    'cut 8',
    'cut -4',
    'deal with increment 7',
    'cut 3',
    'deal with increment 9',
    'deal with increment 3',
    'cut -1'
]

def test1(lines, size):
    """
    >>> test1(testdata1, 10)
    [0, 3, 6, 9, 2, 5, 8, 1, 4, 7]
    >>> test1(testdata2, 10)
    [3, 0, 7, 4, 1, 8, 5, 2, 9, 6]
    >>> test1(testdata3, 10)
    [6, 3, 0, 7, 4, 1, 8, 5, 2, 9]
    >>> test1(testdata4, 10)
    [9, 2, 5, 8, 1, 4, 7, 0, 3, 6]
    """
    return shuffle_new_deck(lines, size)

def shuffle_new_deck(lines, size):
    deck = list(range(size))
    return shuffle(lines, deck)

def shuffle(lines, deck):
    for line in lines:
        if line == 'deal into new stack':
            deck.reverse()
        if line.startswith('deal with increment'):
            incr = int(line.split()[3])
            nd = [0] * len(deck)
            for n, c in enumerate(deck):
                nd[n*incr%len(deck)] = c
            deck = nd
        if line.startswith('cut'):
            cut = int(line.split()[1])
            deck = deck[cut:] + deck[:cut]
    return deck

def part1(lines):
    deck = shuffle_new_deck(lines, 10007)
    return deck.index(2019)

def part2_naive(lines):
    size = 119315717514047
    repeat = 101741582076661
    deck = list(range(size))
    for _ in range(repeat):
        deck = shuffle_new_deck(lines, deck)
    return deck[2020]

def main():
    puzzle_input = adventofcode.read_input(22)
    adventofcode.answer(1, 2939, part1(puzzle_input))
    # adventofcode.answer(2, 0, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
