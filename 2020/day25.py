#!/usr/bin/env python3

import adventofcode

t1 = [
    5764801,
    17807724
]

def transform(value, subject):
    return (value * subject) % 20201227

def part1(lines):
    """
    >>> part1(t1)
    14897079
    """
    card_key = lines[0]
    door_key = lines[1]

    card_loop = 0
    tmp = 1
    while tmp != card_key:
        card_loop += 1
        tmp = transform(tmp, 7)

    door_loop = 0
    tmp = 1
    while tmp != door_key:
        door_loop += 1
        tmp = transform(tmp, 7)

    enc1 = 1
    for _ in range(card_loop):
        enc1 = transform(enc1, door_key)

    enc2 = 1
    for _ in range(door_loop):
        enc2 = transform(enc2, card_key)

    assert enc1 == enc2
    return enc1

def main():
    puzzle_input = adventofcode.read_input(25)
    puzzle_input = [int(x) for x in puzzle_input]
    adventofcode.answer(1, 11328376, part1(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
