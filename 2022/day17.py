#!/usr/bin/env python3
from itertools import cycle

import adventofcode

t1 = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'

rocks = [
    set([(2, 0), (3, 0), (4, 0), (5, 0)]),
    set([(3, 0), (2, 1), (3, 1), (4, 1), (3, 2)]),
    set([(2, 0), (3, 0), (4, 0), (4, 1), (4, 2)]),
    set([(2, 0), (2, 1), (2, 2), (2, 3)]),
    set([(2, 0), (3, 0), (2, 1), (3, 1)]),
]

def add(a, b):
    return tuple(x + y for x, y in zip(a, b))

def add_all(s, delta):
    return set([add(i, delta) for i in s])

def push(falling, d):
    if d == '>':
        if all(x < 6 for x, y in falling):
            return add_all(falling, (1, 0))
    if d == '<':
        if all(x > 0 for x, y in falling):
            return add_all(falling, (-1, 0))
    return falling

def drop(chamber, jets, rock):
    max_height = max(y for _, y in chamber)
    falling = add_all(rock, (0, max_height + 4))
    while True:
        test = push(falling, next(jets))
        if not test.intersection(chamber):
            falling = test
        test = add_all(falling, (0, -1))
        if not test.intersection(chamber):
            falling = test
        else:
            break
    chamber.update(falling)

def show(chamber):
    max_height = max(y for _, y in chamber)
    for y in range(max_height, -1, -1):
        print(''.join('#' if (x, y) in chamber else '.' for x in range(7)))
    print('-' * 7)

def part1(line):
    """
    >>> part1(t1)
    3068
    """
    chamber = set([(x, 0) for x in range(7)])
    jets = cycle(line)
    for i in range(2022):
        drop(chamber, jets, rocks[i % len(rocks)])
    return max(y for _, y in chamber)

def part2(line):
    """
    >>> part2(t1)
    1514285714288
    """
    goal = 1000000000000
    print(f'{len(line) = }')
    chamber = set([(x, 0) for x in range(7)])
    jets = cycle(line)
    last = 0
    diffs = []
    for i in range(40):
        drop(chamber, jets, rocks[i % len(rocks)])
        max_height = max(y for _, y in chamber)
        diffs.append(max_height - last)
        last = max_height
    print(diffs)

def main():
    puzzle_input = adventofcode.read_input(17)
    adventofcode.answer(1, 3239, part1(puzzle_input))
    # adventofcode.answer(2, 0, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
