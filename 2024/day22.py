#!/usr/bin/env python3

import adventofcode

def evolve(n):
    p = ((n * 64) ^ n) % 16777216
    p = ((p // 32) ^ p) % 16777216
    p = ((p * 2048) ^ p) % 16777216
    return p

def calc(n, rep):
    for _ in range(rep):
        n = evolve(n)
    return n

def part1(lines):
    """
    >>> part1([1, 10, 100, 2024])
    37327623
    """
    return sum(calc(x, 2000) for x in lines)

def bananas_for_sequences(n):
    results = {}
    ds = ()
    lp = n % 10
    for _ in range(2000):
        n = evolve(n)
        ds = ds[-3:] + tuple([(n % 10) - lp])
        if len(ds) == 4 and ds not in results:
            results[ds] = n % 10
        lp = n % 10
    return results

def part2(lines):
    """
    >>> part2([1, 2, 3, 2024])
    23
    """
    data = [bananas_for_sequences(x) for x in lines]
    keys = set()
    for d in data:
        keys.update(d.keys())

    return max(sum(d[k] for d in data if k in d) for k in keys)

def main():
    puzzle_input = adventofcode.read_input(22)
    puzzle_input = [int(x) for x in puzzle_input]
    adventofcode.answer(1, 12979353889, part1(puzzle_input))
    adventofcode.answer(2, 1449, part2(puzzle_input))

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
