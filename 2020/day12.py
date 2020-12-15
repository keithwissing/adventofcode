#!/usr/bin/env python3

import adventofcode

t1 = ['F10', 'N3', 'F7', 'R90', 'F11', ]

def step(state, l):
    i, arg = l[0], int(l[1:])
    if i == 'F':
        m = {0: (1, 0, 0), 90: (0, -1, 0), 180: (-1, 0, 0), 270: (0, 1, 0)}[state[2]]
    else:
        m = {'N': (0, 1, 0), 'S': (0, -1, 0), 'E': (1, 0, 0), 'W': (-1, 0, 0), 'R': (0, 0, 1), 'L': (0, 0, -1)}[i]
    return (state[0] + m[0] * arg, state[1] + m[1] * arg, (state[2] + m[2] * arg) % 360)

def part1(lines):
    """
    >>> part1(t1)
    25
    """
    state = (0, 0, 0)
    for l in lines:
        state = step(state, l)
    return abs(state[0]) + abs(state[1])

def rotate(x, y, a):
    if a == 90:
        return [-y, x]
    if a == 180:
        return [-x, -y]
    if a == 270:
        return [y, -x]

def step2(state, l):
    i, arg = l[0], int(l[1:])
    if i == 'N':
        state[3] += arg
    if i == 'S':
        state[3] -= arg
    if i == 'E':
        state[2] += arg
    if i == 'W':
        state[2] -= arg
    if i == 'F':
        state[0] += state[2] * arg
        state[1] += state[3] * arg
    if i == 'L':
        r = rotate(state[2], state[3], arg)
        state[2] = r[0]
        state[3] = r[1]
    if i == 'R':
        r = rotate(state[2], state[3], 360 - arg)
        state[2] = r[0]
        state[3] = r[1]
    return state

def part2(lines):
    """
    >>> part2(t1)
    286
    """
    state = [0, 0, 10, 1]
    for l in lines:
        state = step2(state, l)
    return abs(state[0]) + abs(state[1])

def main():
    puzzle_input = adventofcode.read_input(12)
    adventofcode.answer(1, 1152, part1(puzzle_input))
    adventofcode.answer(2, 58637, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
