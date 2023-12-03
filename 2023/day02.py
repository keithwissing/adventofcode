#!/usr/bin/env python3

import adventofcode

t1 = [
    'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
    'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
    'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
    'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
    'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green',
]

def part1(lines):
    """
    >>> part1(t1)
    8
    """
    limits = [12, 13, 14]
    sum = 0
    for line in lines:
        game, hands = line.split(':')
        game = int(game[4:])
        for hand in hands.split(';'):
            for show in hand.split(','):
                n, c = show.split()
                n = int(n)
                if c == 'red' and n > limits[0]:
                    game = 0
                if c == 'green' and n > limits[1]:
                    game = 0
                if c == 'blue' and n > limits[2]:
                    game = 0
        sum += game
    return sum

def part2(lines):
    """
    >>> part2(t1)
    2286
    """
    sum = 0
    for line in lines:
        mins = [0, 0, 0]
        game, hands = line.split(':')
        for hand in hands.split(';'):
            for show in hand.split(','):
                n, c = show.split()
                n = int(n)
                if c == 'red' and n > mins[0]:
                    mins[0] = n
                if c == 'green' and n > mins[1]:
                    mins[1] = n
                if c == 'blue' and n > mins[2]:
                    mins[2] = n
        sum += mins[0] * mins[1] * mins[2]
    return sum

def main():
    puzzle_input = adventofcode.read_input(2)
    adventofcode.answer(1, 2563, part1(puzzle_input))
    adventofcode.answer(2, 70768, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
