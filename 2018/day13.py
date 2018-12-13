#!/usr/bin/env python

import collections
from string import maketrans
import adventofcode

test_input = [
    r'/->-\        ',
    '|   |  /----\\',
    r'| /-+--+-\  |',
    r'| | |  | v  |',
    r'\-+-/  \-+--/',
    r'  \------/   ']

def part1(puzzle_input):
    """
    >>> part1(test_input)
    (7, 3)
    """
    tracks, carts = parse_input(puzzle_input)
    crash = None
    while not crash:
        carts.sort()
        for pos, cart in enumerate(carts):
            carts[pos] = move_cart(cart, tracks)
            crash = detect_crash(carts)
            if crash:
                break
    return crash

test_input_2 = [
    r'/>-<\  ',
    r'|   |  ',
    '| /<+-\\',
    r'| | | v',
    r'\>+</ |',
    r'  |   ^',
    r'  \<->/']

def part2(puzzle_input):
    """
    >>> part2(test_input_2)
    (6, 4)
    """
    tracks, carts = parse_input(puzzle_input)
    crash = None
    while len(carts) > 1:
        carts.sort()
        for pos, cart in enumerate(carts):
            carts[pos] = move_cart(cart, tracks)
            crash = detect_crash(carts)
            if crash:
                for p, i in enumerate(carts):
                    if i[0] == crash[1] and i[1] == crash[0]:
                        carts[p] = (-1, -1, 0, 0)
        carts = [cart for cart in carts if cart[0] > -1]
    return (carts[0][1], carts[0][0])

def detect_crash(carts):
    locs = [(c[1], c[0]) for c in carts]
    crashes = [item for item, count in collections.Counter(locs).items() if count > 1]
    return crashes[0] if crashes else None

def move_cart(cart, tracks):
    (y, x, direction, next_turn) = cart
    if y < 0:
        return cart
    y += {0:-1, 1:0, 2:1, 3:0}[direction]
    x += {0:0, 1:1, 2:0, 3:-1}[direction]
    if tracks[y][x] == '/':
        direction = {0:1, 1:0, 2:3, 3:2}[direction]
    if tracks[y][x] == '\\':
        direction = {0:3, 1:2, 2:1, 3:0}[direction]
    if tracks[y][x] == '+':
        direction = (direction + next_turn + 3) % 4
        next_turn = (next_turn + 1) % 3
    return (y, x, direction, next_turn)

def parse_input(lines):
    tracks = [x.translate(maketrans("^>v<", "|-|-")) for x in lines]
    carts = []
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if line[x] in "^>v<":
                cart = (y, x, "^>v<".index(char), 0)
                carts.append(cart)
    return tracks, carts

def main():
    puzzle_input = adventofcode.read_input(13)
    adventofcode.answer(1, (26, 92), part1(puzzle_input))
    adventofcode.answer(2, (86, 18), part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
