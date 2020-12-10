#!/usr/bin/env python3

import adventofcode

t1 = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]

t2 = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47,
      24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25,
      35, 8, 17, 7, 9, 4, 2, 34, 10, 3, ]

def part1(ads):
    """
    >>> part1(t1)
    35
    >>> part1(t2)
    220
    """
    ads.sort()
    diffs = [0, 0, 0, 1]
    last = 0
    for x in ads:
        diffs[x - last] += 1
        last = x
    return diffs[1] * diffs[3]

def calc_diffs(ads):
    i = [0] + ads
    o = ads + [ads[-1] + 3]
    diffs = [b - a for a, b in zip(i, o)]
    return diffs

def is_valid(ads):
    diffs = calc_diffs(ads)
    for k in diffs:
        if k not in [1, 2, 3]:
            return False
    return True

def p2(ads, p):
    """
    I know this won't perform for the full puzzle input
    """
    tot = 0
    for x in range(p, len(ads) - 1):
        d = ads[:x] + ads[x + 1:]
        if is_valid(d):
            tot += 1
            tot += p2(d, x)
    return tot

def part2(lines):
    """
    >>> part2(t1)
    8
    >>> part2(t2) # 2^3 × 7^4
    19208
    """
    # lines.sort()
    # return p2(lines, 0) + 1

    ads = lines[:]
    ads.sort()
    i = [0] + ads
    o = ads + [ads[-1] + 3]
    diffs = [b - a for a, b in zip(i, o)]

    p = 0
    tot = 1
    for x in diffs:
        if x == 1:
            p += 1
        if x == 3:
            if p == 2:
                tot *= 2
            if p == 3:
                tot *= 4
            if p == 4:
                tot *= 7
            p = 0
    return tot

def main():
    puzzle_input = adventofcode.read_input(10)
    puzzle_input = [int(x) for x in puzzle_input]
    adventofcode.answer(1, 2775, part1(puzzle_input))
    adventofcode.answer(2, 518344341716992, part2(puzzle_input))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
