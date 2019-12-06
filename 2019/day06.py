#!/usr/bin/env python3

import adventofcode

def orbital_checksum(orbits):
    """
    >>> orbital_checksum(['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L'])
    42
    """
    tree = {}
    for line in orbits:
        s, m = line.split(')')
        tree[m] = s
    cnt = 0
    for s in tree:
        while s != 'COM':
            cnt += 1
            s = tree[s]
    return cnt

def transfers(orbits):
    """
    >>> transfers(['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L', 'K)YOU', 'I)SAN'])
    4
    """
    tree = {}
    for line in orbits:
        s, m = line.split(')')
        tree[m] = s
    cnts = {}
    s = 'YOU'
    cnt = 0
    while s != 'COM':
        cnts[s] = cnt
        cnt += 1
        s = tree[s]
    s = 'SAN'
    cnt = 0
    while s != 'COM':
        if s in cnts:
            return cnt + cnts[s] - 2
        cnt += 1
        s = tree[s]

def part1(orbits):
    return orbital_checksum(orbits)

def part2(orbits):
    return transfers(orbits)

def main():
    puzzle_input = adventofcode.read_input(6)
    adventofcode.answer(1, 119831, part1(puzzle_input))
    adventofcode.answer(2, 322, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
