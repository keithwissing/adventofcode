#!/usr/bin/env python3

import heapq
import adventofcode

t1 = [
    '5483143223',
    '2745854711',
    '5264556173',
    '6141336146',
    '6357385478',
    '4167524645',
    '2176841721',
    '6882881134',
    '4846848554',
    '5283751526',
]

def parse(lines):
    return [[int(c) for c in r] for r in lines]

def adjacent(pos):
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dx != 0 or dy != 0:
                yield (pos[0] + dx, pos[1] + dy)

def iterate(grid):
    q = []
    f = 0
    for y in range(10):
        for x in range(10):
            grid[y][x] += 1
            if grid[y][x] == 10:
                f += 1
                for p in adjacent((x, y)):
                    heapq.heappush(q, p)
    while q:
        pos = heapq.heappop(q)
        if pos[0] >= 0 and pos[1] >= 0 and pos[0] < 10 and pos[1] < 10:
            if grid[pos[1]][pos[0]] < 10:
                grid[pos[1]][pos[0]] += 1
                if grid[pos[1]][pos[0]] == 10:
                    f += 1
                    for p in adjacent((pos[0], pos[1])):
                        heapq.heappush(q, p)
    for y in range(10):
        for x in range(10):
            if grid[y][x] == 10:
                grid[y][x] = 0
    return grid, f

def part1(lines):
    """
    >>> part1(t1)
    1656
    """
    count = 0
    grid = parse(lines)
    for _ in range(100):
        grid, f = iterate(grid)
        count += f
    return count

def part2(lines):
    """
    >>> part2(t1)
    195
    """
    grid = parse(lines)
    f = 0
    count = 0
    while f != 100:
        grid, f = iterate(grid)
        count += 1
    return count

def main():
    puzzle_input = adventofcode.read_input(11)
    adventofcode.answer(1, 1591, part1(puzzle_input))
    adventofcode.answer(2, 314, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
