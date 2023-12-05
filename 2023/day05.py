#!/usr/bin/env python3
import re
import sys

import adventofcode

t1 = [
    'seeds: 79 14 55 13',
    '',
    'seed-to-soil map:',
    '50 98 2',
    '52 50 48',
    '',
    'soil-to-fertilizer map:',
    '0 15 37',
    '37 52 2',
    '39 0 15',
    '',
    'fertilizer-to-water map:',
    '49 53 8',
    '0 11 42',
    '42 0 7',
    '57 7 4',
    '',
    'water-to-light map:',
    '88 18 7',
    '18 25 70',
    '',
    'light-to-temperature map:',
    '45 77 23',
    '81 45 19',
    '68 64 13',
    '',
    'temperature-to-humidity map:',
    '0 69 1',
    '1 0 69',
    '',
    'humidity-to-location map:',
    '60 56 37',
    '56 93 4',
]

def parse(lines):
    seeds = [int(x) for x in lines[0][7:].split()]
    maps = {}
    for line in lines[2:]:
        if not line:
            continue
        if not line[0].isdigit():
            f, t = re.findall(r'(.+)-to-(.+) map:', line)[0]
            cur = (t, [])
            maps[f] = cur
        else:
            cur[1].append([int(x) for x in line.split()])
    return seeds, maps

def get_location(maps, seed):
    i, v = 'seed', seed
    n = sys.maxsize
    while i != 'location':
        m = maps[i]
        i = m[0]
        moved = False
        for t in m[1]:
            if v < t[1]:
                n = min(n, t[1] - v)
            if v < t[1] + t[2]:  # This was not necessary for my input
                n = min(n, t[1] + t[2] - v)
            if not moved and t[1] <= v < t[1] + t[2]:
                v = v - t[1] + t[0]
                moved = True
    return v, n

def part1(lines):
    """
    >>> part1(t1)
    35
    """
    seeds, maps = parse(lines)
    close = sys.maxsize
    for seed in seeds:
        v, _ = get_location(maps, seed)
        close = min(close, v)
    return close

def part2(lines):
    """
    >>> part2(t1)
    46
    """
    seeds, maps = parse(lines)
    close = sys.maxsize
    for p in range(0, len(seeds), 2):
        seed = seeds[p]
        while seed < seeds[p] + seeds[p + 1]:
            v, n = get_location(maps, seed)
            if v < close:
                close = min(close, v)
            seed += max(1, n)
    return close

def main():
    puzzle_input = adventofcode.read_input(5)
    adventofcode.answer(1, 457535844, part1(puzzle_input))
    adventofcode.answer(2, 41222968, part2(puzzle_input))
    puzzle_input = [line.rstrip('\n') for line in open("day05-input-nathan.txt")]
    adventofcode.answer(2, 7873084, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
