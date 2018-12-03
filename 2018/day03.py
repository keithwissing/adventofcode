#!/usr/bin/env python

import collections
from string import maketrans
import adventofcode

Claim = collections.namedtuple('Claim', 'id x y width height')

def add_claim(claim_map, claim):
    for x in range(claim.x, claim.x+claim.width):
        for y in range(claim.y, claim.y+claim.height):
            square = (x,y)
            if square in claim_map:
                claim_map[square] += 1
            else:
                claim_map[square] = 1

def parse_input_line(line):
    """
    >>> parse_input_line("#1 @ 1,3: 4x4")
    Claim(id=1, x=1, y=3, width=4, height=4)
    """
    line = line.translate(maketrans("#@,:x", "     "))
    parts = line.split()
    parts = [int(x) for x in parts]
    return Claim( id=parts[0], x=parts[1], y=parts[2], width=parts[3], height=parts[4])

def add_all_claims(claim_map, claims):
    for claim in claims:
        add_claim(claim_map, claim)

def build_claim_map(claims):
    claim_map = {}
    add_all_claims(claim_map, claims)
    return claim_map

def find_multi_claimed_area(claim_map):
    return len([x for _, x in claim_map.items() if x > 1])

def test1(input):
    """
    >>> test1(["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"])
    4
    """
    claims = [parse_input_line(x) for x in input]
    claim_map = build_claim_map(claims)
    return find_multi_claimed_area(claim_map)

def does_claim_overlap(claim_map, claim):
    for x in range(claim.x, claim.x+claim.width):
        for y in range(claim.y, claim.y+claim.height):
            if claim_map[(x,y)] > 1:
                return True
    return False

def find_non_overlapped_claim(claim_map, claims):
    for claim in claims:
        if not does_claim_overlap(claim_map, claim):
            return claim.id

def main():
    puzzle_input = adventofcode.read_input(3)
    puzzle_input = [parse_input_line(x) for x in puzzle_input]
    claim_map = build_claim_map(puzzle_input)
    adventofcode.answer(1, 104241, find_multi_claimed_area(claim_map))
    adventofcode.answer(2, 806, find_non_overlapped_claim(claim_map, puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
