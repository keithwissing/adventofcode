#!/usr/bin/env python3

import adventofcode

def parse(line):
    r, l, p = line.split()
    i, a = r.split('-')
    l = l[0]
    return int(i), int(a), l, p

def part1(entries):
    """
    >>> part1(['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc'])
    2
    """
    valid = 0
    for line in entries:
        i, a, l, p = parse(line)
        if i <= p.count(l) <= a:
            valid += 1
    return valid

def part2(entries):
    """
    >>> part2(['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc'])
    1
    """
    valid = 0
    for line in entries:
        i, a, l, p = parse(line)
        if (p[i-1] + p[a-1]).count(l) == 1:
            valid += 1
    return valid

def main():
    puzzle_input = adventofcode.read_input(2)
    adventofcode.answer(1, 655, part1(puzzle_input))
    adventofcode.answer(2, 673, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
