#!/usr/bin/env python3

from collections import defaultdict
from itertools import product
import adventofcode

t1 = [
    'sesenwnenenewseeswwswswwnenewsewsw',
    'neeenesenwnwwswnenewnwwsewnenwseswesw',
    'seswneswswsenwwnwse',
    'nwnwneseeswswnenewneswwnewseswneseene',
    'swweswneswnenwsewnwneneseenw',
    'eesenwseswswnenwswnwnwsewwnwsene',
    'sewnenenenesenwsewnenwwwse',
    'wenwwweseeeweswwwnwwe',
    'wsweesenenewnwwnwsenewsenwwsesesenwne',
    'neeswseenwwswnwswswnw',
    'nenwswwsewswnenenewsenwsenwnesesenew',
    'enewnwewneswsewnwswenweswnenwsenwsw',
    'sweneswneswneneenwnewenewwneswswnese',
    'swwesenesewenwneswnwwneseswwne',
    'enesenwswwswneneswsenwnewswseenwsese',
    'wnwnesenesenenwwnenwsewesewsesesew',
    'nenewswnwewswnenesenwnesewesw',
    'eneswnwswnwsenenwnwnwwseeswneewsenese',
    'neswnwewnwnwseenwseesewsenwsweewe',
    'wseweeenwnesenwwwswnew',
]

def coordinate_of(line):
    pos = 0
    dirs = {d: 0 for d in ['e', 'se', 'sw', 'w', 'nw', 'ne']}
    while pos < len(line):
        if line[pos] in ['e', 'w']:
            dirs[line[pos]] += 1
            pos += 1
        elif line[pos:pos + 2] in ['se', 'sw', 'ne', 'nw']:
            dirs[line[pos:pos + 2]] += 1
            pos += 2
    vec = (dirs['e'] - dirs['w'], dirs['ne'] - dirs['sw'], dirs['nw'] - dirs['se'])
    hid = (vec[0] - vec[2], vec[1] + vec[2])
    return hid

def starting_floor(lines):
    floor = {}
    for line in lines:
        hid = coordinate_of(line)
        if hid in floor:
            floor[hid] = 1 - floor[hid]
        else:
            floor[hid] = 1
    return floor

def part1(lines):
    """
    >>> part1(t1)
    10
    """
    floor = starting_floor(lines)
    return sum(floor.values())

def adjacent(pos):
    ds = ((-1, 1), (0, 1), (1, 0), (1, -1), (0, -1), (-1, 0))
    for d in ds:
        yield (pos[0] + d[0], pos[1] + d[1])

def iterate(floor):
    nf = defaultdict(lambda: 0)
    limits = [(min(c) - 1, max(c) + 2) for c in zip(*floor.keys())]
    ranges = map(lambda t: range(t[0], t[1]), limits)
    for pos in product(*ranges):
        nei = sum(floor[a] for a in adjacent(pos))
        if floor[pos] and nei in [1,2]:
            nf[pos] = 1
        if floor[pos] == 0 and nei == 2:
            nf[pos] = 1
    return nf

def part2(lines):
    """
    >>> part2(t1)
    2208
    """
    floor = defaultdict(lambda: 0, starting_floor(lines))
    for _ in range(100):
        floor = iterate(floor)
    return sum(floor.values())

def main():
    puzzle_input = adventofcode.read_input(24)
    adventofcode.answer(1, 244, part1(puzzle_input))
    adventofcode.answer(2, 3665, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
