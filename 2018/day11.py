#!/usr/bin/env python

import adventofcode

def part1(puzzle_input):
    """
    >>> part1(18)
    (33, 45)
    """
    grid = [[0 for _ in range(300)] for _ in range(300)]
    for y in range(300):
        for x in range(300):
            grid[x][y] = cell_power_level(x+1, y+1, puzzle_input)
    power = [[0 for _ in range(300)] for _ in range(300)]
    for y in range(300-3):
        for x in range(300-3):
            power[x][y] = sum([sum([grid[c][u] for u in range(y, y+3)]) for c in range(x, x+3)])
    top = max([max([b for b in v]) for v in power])
    for y in range(300-3):
        for x in range(300-3):
            if power[x][y] == top:
                return (x+1, y+1)

def cell_power_level(x, y, serial):
    rack_id = x + 10
    level = rack_id * y
    level += serial
    level *= rack_id
    level = (level % 1000) / 100
    level -= 5
    return level

def part2(puzzle_input):
    """
    #>>> part2(18)
    (90, 269, 16)
    #>>> part2(42)
    (232, 251, 12)
    """
    fudge = 12

    grid = [[0 for _ in range(300)] for _ in range(300)]
    for y in range(300):
        for x in range(300):
            grid[x][y] = cell_power_level(x+1, y+1, puzzle_input)
    top = 0
    ident = (0, 0, 0)
    for y in range(300):
        for x in range(300):
            for s in range(1, min(fudge, 300-(max(x, y)))):
                power = sum([sum([grid[c][u] for u in range(y, y+s)]) for c in range(x, x+s)])
                if power > top:
                    top = power
                    ident = (x+1, y+1, s)
    return ident

def main():
    puzzle_input = int(adventofcode.read_input(11))
    adventofcode.answer(1, (20, 41), part1(puzzle_input))
    adventofcode.answer(2, (236, 270, 11), part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
