#!/usr/bin/env python3

import adventofcode

def path(tree, s):
    while s != 'COM':
        yield s
        s = tree[s]

def orbital_checksum(orbits):
    """
    >>> orbital_checksum(['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L'])
    42
    """
    tree = {m: s for s, m in [line.split(')') for line in orbits]}
    return sum(1 for s in tree for _ in path(tree, s))

def transfers(orbits):
    """
    >>> transfers(['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L', 'K)YOU', 'I)SAN'])
    4
    """
    tree = {m: s for s, m in [line.split(')') for line in orbits]}
    cnts = {n: c for c, n in enumerate(path(tree, 'YOU'))}
    for c, n in enumerate(path(tree, 'SAN')):
        if n in cnts:
            return c + cnts[n] - 2

def main():
    puzzle_input = adventofcode.read_input(6)
    adventofcode.answer(1, 119831, orbital_checksum(puzzle_input))
    adventofcode.answer(2, 322, transfers(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
