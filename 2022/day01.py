#!/usr/bin/env python3
from itertools import groupby

import adventofcode

def split_on_blank_lines(lines):
    yield from [list(sub) for ele, sub in groupby(lines, key=bool) if ele]

def part1(lines):
    return max(sum(int(x) for x in carry) for carry in split_on_blank_lines(lines))

def part2(lines):
    return sum(sorted(sum(int(x) for x in carry) for carry in split_on_blank_lines(lines))[-3:])

def main():
    puzzle_input = adventofcode.read_input(1)
    adventofcode.answer(1, 69693, part1(puzzle_input))
    adventofcode.answer(2, 200945, part2(puzzle_input))

if __name__ == '__main__':
    main()
