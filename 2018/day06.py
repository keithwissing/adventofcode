#!/usr/bin/env python

import adventofcode

def part1(puzzle_input):
    """
    >>> part1([ (1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9) ])
    17
    """
    fs = 400
    counts = [0] * len(puzzle_input)
    for cx in range(fs):
        for cy in range(fs):
            md = 32767
            mi = -1
            for ti in range(len(puzzle_input)):
                td = distance((cx, cy), puzzle_input[ti])
                if td == md:
                    mi = -1
                if td < md:
                    md = td
                    mi = ti
            if mi != -1 and counts[mi] != -1:
                counts[mi] += 1
                if cx == 0 or cx == fs-1 or cy == 0 or cy == fs-1:
                    counts[mi] = -1
    return max(counts)

def part2(puzzle_input, max_distance):
    """
    >>> part2([ (1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9) ], 32)
    16
    """
    fs = 400
    total = 0
    for cx in range(fs):
        for cy in range(fs):
            if included((cx, cy), puzzle_input, max_distance):
                total += 1
    return total

def included(point, puzzle_input, max_distance):
    total_distance = sum([distance(i, point) for i in puzzle_input])
    return total_distance < max_distance

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def parse_line(line):
    parts = line.split()
    return (int(parts[0][:-1]), int(parts[1]))

def main():
    puzzle_input = adventofcode.read_input(6)
    puzzle_input = map(parse_line, puzzle_input)
    adventofcode.answer(1, 4233, part1(puzzle_input))
    adventofcode.answer(2, 45290, part2(puzzle_input, 10000))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
